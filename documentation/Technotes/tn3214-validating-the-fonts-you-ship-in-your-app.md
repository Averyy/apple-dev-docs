# TN3214: Validating the fonts you ship in your app

**Framework**: Technotes

Understand the App Store’s font validation, reproduce the check, and fix any issues it reports.

#### Overview

The App Store validates every font in your app’s payload, and a font can fail that check even though it renders fine on your Mac or device.

This happens because a font file stores its outlines, metrics, character mappings, and names as binary tables. Tools that generate, subset, or convert fonts can update one part of a table without updating a related part to match. For example, removing glyphs but leaving the old count in place, or moving data without adjusting the offset that points to it.

A font parser that never touches the broken data can still render the font without issue. But the same file can fail elsewhere: it can cause visible failures in your app, or make the font parser read past the end of the table, which can crash your app or expose unrelated memory.

macOS includes `FontValidator`, the tool [`Font Book`](https://developer.apple.comhttps://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac) and the App Store’s validation both use to read a font file and report what it finds.

This technote covers what it checks, how to run the same check on your Mac, and how to resolve each kind of failure it reports.

#### Understand What the App Store Checks

During app ingestion, the App Store validates every font in your app’s payload at one of two levels, based on how your app uses its fonts. If your app only uses a font to display text, it just needs to be readable, so validation uses `minimum`, which allows a font file format that the target OS (macOS, iOS, tvOS, visionOS, or watchOS) can’t install. If your app requests the [`Configuring custom fonts`](https://developer.apple.com/documentation/xcode/configuring-custom-fonts), each font needs to be in a file format the OS can install, so validation uses `strict`.

> **Note**: If your app bundles or redistributes a font licensed to Apple, the font will fail validation even at `minimum`.

A font that passes at `minimum` can still return an error at `strict`. If you’re adding the Install fonts capability to an app you already shipped, validate against `strict` first.

Here are the font file formats each platform can and can’t install:

**Accepted formats:**

- macOS: `.ttf`, `.otf`, `.ttc`, `.otc`, `.dfont` or font suitcase (legacy Mac font containers), LWFN (classic Mac OS Type 1 font), Type 1 housed in an sfnt.
- iOS, tvOS, visionOS, watchOS: `.ttf`, `.otf`, `.ttc`, `.otc`.

**Rejected formats (on all platforms):**

- `.woff`, `.woff2`, `.pfa`, `.pfb`, bare CFF/CFF2, bitmap-only.

`.woff` and `.woff2` are web-delivery containers, and `.pfa`/`.pfb` are PostScript Type 1 files. None of these are installable font formats on any Apple platform.

> ❗ **Important**: - Starting October 1, 2026, the App Store will reject asset pack uploads that bundle or redistribute a font Apple designs or licenses.
- Starting October 1, 2027, the App Store will reject app uploads that bundle or redistribute a font Apple designs or licenses.
- The App Store will reject font provider or WidgetKit apps that contain a font that fails `strict` validation.

#### Reproduce the Check on Your Mac

This technote describes `FontValidator` 3.5 or later, which ships with macOS 27.2 and later. Run the tool with `-version` to see which one you have. Earlier versions don’t accept these options, lack some of the capabilities this technote describes, and might report more findings than the App Store acts on. If you have an earlier version, update to macOS 27.2 or later.

macOS includes `FontValidator`, but it isn’t on your `PATH`. Run it using its full path:

```bash
/System/Library/Frameworks/ApplicationServices.framework/Frameworks/ATS.framework/Support/FontValidator \
    -progress -platform iOS -level strict -reportType full -appleFonts MyApp.app
```

The command above is similar to the one the App Store runs. You can adjust the following:

- `-platform`: The platform your app targets. For example: `macOS`, `iOS`, `tvOS`, `visionOS`, or `watchOS`.
- `-level`: Use `strict` if your app requests the Fonts capability, or `minimum` if it doesn’t.
- `-reportType`: Controls how much detail the report includes: - `summary`: Includes the result, the `max_code`, and whether the format is installable.
- `detailed`: Adds each finding’s code and messages.
- `full`: Adds the warnings and the font’s format.

Use the `full` report type when you’re diagnosing why the App Store rejected a font.

For the last argument, give `FontValidator` one or more paths to scan — the `.app` bundle you built, your project’s source folder, or individual font files. It searches recursively through any directory you point it at, including inside app and framework bundles, so it finds every font without you having to list each one.

> **Note**: If your app stores fonts in an asset catalog, validate your project sources instead of the `.app` bundle you built. Xcode compiles the catalog into a binary resource file that `FontValidator` can’t read. If it delivers fonts in an asset pack, point `FontValidator` at the font files in your asset pack sources instead, since they ship separately from the app bundle.

`FontValidator` has the following command-line behaviors:

- It matches option values exactly, and they’re case-sensitive. For example, `-level strict` works, but `-level Strict` is an error.
- Option names are more flexible. For example: `-reportType`, `-report-type`, and `-report_type` all refer to the same option.
- It writes the JSON report to standard output. You can add `-reportOutput report.json` to send it to a file, or `-onlyFailures` to list only the files that failed.
- Its exit status tells you the outcome: `0` for success, `255` when one or more files failed, and `252` if you mistyped an option.
- For the full list of options and codes, run `-help`.

#### Read the Report

`FontValidator` writes its findings as JSON. Here’s an example, with what each key means explained below:

```json
{
  "Failures" : 1,
  "FilesProcessed" : 1,
  "FontFiles" : 1,
  "Details" : [
    {
      "path" : "MyApp.app/Contents/Resources/MyAppBrandingFont.woff2",
      "result" : false,
      "fonts" : [
        {
          "issues" : [
            {
              "issue" : "Font not supported by platform",
              "code" : -102,
              "messages" : [
                "'woff': The woff2_TrueTypeMemoryFontKind format is not one the target platform will install."
              ]
            }
          ],
          "format" : "woff2_TrueTypeMemoryFontKind",
          "fontname" : "MyAppBrandingFont",
          "warnings" : [

          ]
        }
      ],
      "max_code" : -102,
      "os_installable" : false,
      "format" : "woff2_TrueTypeMemoryFontKind"
    }
  ]
}
```

- `result`: A value of `false` means the file failed and the App Store won’t accept it. Don’t infer the `result` from a `code`, since the same code can appear in both a pass and a failure.
- `issue`: Names the rule that found the problem.
- `messages`: Describes what it found. For a few findings, such as a bundled Apple font, the rule name alone fully describes the issue and there’s no message.
- `max_code`: The most severe issue found in the file.
- `os_installable`: Says whether the file’s format is one the platform installs, regardless of the level you validated at.
- `code`: Describes what kind of finding it is, and takes one of the following values:

| Code | Meaning |
| --- | --- |
| `0` | No issues found. |
| `-101` | The font violates the font specification in a way that fails validation. |
| `-102` | The font’s format isn’t one the platform installs or its data lives only in the resource fork. |
| `-103` | An Apple-designed font. |
| `-104` | A font licensed to Apple. |
| `-201` | A failure this level relaxed. Address it, because a parser could have a memory-safety problem here. |
| `-202` | A failure this level relaxed. It’s a specification violation with no memory-safety concern. |
| `-301` | A warning. |

#### Fix the Issue

Each finding names one of the codes above. Look up the one that matches your report below.

##### 101 the Font Violates the Specification

Fonts that reach this are almost always the output of a tool that rewrote part of the file without updating the rest. The most common shapes are:

| Rule | Issue | Cause |
| --- | --- | --- |
| `'sfnt' required tables` | A required table is missing. | Subsetting removed too much. |
| `'cmap' table usability` | No subtable usable as a Unicode encoding. | An icon-font generator. |
| `'name' table usability` | No PostScript, full, family, or style name. | A subsetter kept only some name records. |
| `'name' table usability` | Text isn’t valid in the encoding its own record declares. | UTF-8 written into a UTF-16 record. |
| `'glyf' table structure` | A `'loca'` offset points past the end of `'glyf'`. | A truncated `'glyf'`/`'loca'` pair. |
| `'glyf' table instructions` | A point-flag repeat count overruns the glyph’s point count. | A hand-rolled outline writer. |
| `'post' table usability` | The glyph-name pool runs past the end of the table. | A subsetter trimmed the glyph count but not the names. |
| `'head' table structure` | The table is too short, or `indexToLocFormat` is neither 0 nor 1. | A long `'loca'` written with the short format declared. |
| Font basic parsability | Two tables overlap, or a table offset or length is out of bounds. | A tool patched one table without re-laying out the file. |

Most of these are bookkeeping errors that a font tool recomputes for you. To fix them, open and re-save the font in a font editor or another font-development tool. Re-saving rebuilds the table directory, offsets, lengths, and checksums.

Re-run the validator on the result. If the same finding still appears after re-saving, the defect is in the font’s actual content rather than its layout. Regenerate the font from source with a current version of your font editor, or go back to your font vendor with the message text from the report.

##### 102 the Target Platform Doesnt Accept This Font

This code has two distinct causes, and the message in the report tells you which one applies.

When the font’s format isn’t installable, you likely shipped a web font or legacy desktop font in your app bundle. See the accepted and rejected formats above. How you fix it depends on the format:

- `.woff`/`.woff2`: Convert the font to an installable format. These are compressed wrappers around an ordinary font, so converting back is lossless. Many font editors and font-development tools export the wrapped `.ttf` or `.otf` directly. Ship that file instead. If your app requests the Fonts capability, remove the web font from your bundle after you’ve shipped the installable version. Don’t just rename the file extension: the validator identifies formats by content, so it still rejects a `.woff2` file renamed to `.ttf`.
- `.pfa`/`.pfb`: Ask your font vendor for an OpenType version instead of converting it yourself. Unlike a `.woff`/`.woff2` wrapper, Type 1 outlines don’t convert losslessly, so a self-converted font can render differently.

This same format requirement applies to font collections: if a single font file bundles multiple styles together, such as Regular, Bold, and Italic, every style inside it must also be in an installable format.

macOS stores a resource fork as the `com.apple.ResourceFork` extended attribute. A font stored this way works on macOS but the file becomes empty if a copy operation drops its extended attributes. For example, copying the file to a platform that doesn’t support resource forks removes the attribute. Unlike a format rejection, this error makes the font fail at every validation level. It fails your submission whether or not you request the Fonts capability, and it applies only when your app targets iOS, tvOS, visionOS, or watchOS.

To fix this, re-save the font as an ordinary data-fork `.ttf` or `.otf` file.

##### 103 and 104 the App Redistributes a Font Apple Designs or Licenses

Your app can’t redistribute fonts Apple designs, such as the San Francisco and New York families, or fonts Apple licenses from a third party. They’re already present on the device or available for download. Remove the bundled copies and access these fonts directly through the system font APIs. For more information, see [`Fonts`](https://developer.apple.com/documentation/technologyoverviews/fonts) in the Technology Overviews.

`FontValidator` identifies a font Apple designs or fonts licensed to Apple by content markers in the file. Sharing a name with one of these fonts, such as your own build of a face you licensed independently, doesn’t trigger this error.

`FontValidator` reports these findings at every level, so your submission fails whether or not your app requests the Fonts capability.

#### Revision History

- **2026-10-01** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3214-validating-the-fonts-you-ship-in-your-app)*