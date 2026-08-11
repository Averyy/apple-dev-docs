# Fonts

**Framework**: Technology Overviews

Choose the right fonts for your app’s interface and content, and make custom fonts available across your app, its extensions, and other apps.

#### Overview

Fonts give text its visual identity. The right font makes your interface readable, conveys tone and brand, and supports the languages your app targets. Apple platforms provide a curated set of fonts that fall into one of three categories:

- **System fonts:** The fonts Apple provides for interface elements, optimized for legibility and adaptability.
- **Document fonts:** A library of fonts people choose for their own content, such as documents, messages, and layouts.
- **Custom fonts:** Fonts you bundle with your app to achieve a specific design or match your brand.

Many apps combine all three. Each framework provides font APIs suited to these categories, so use the APIs that match the framework you’re building with. Choosing the right category, and retrieving its fonts through the recommended API, results in better consistency across the system, better worldwide language support, and fewer surprises when the system evolves.

> ❗ **Important**: Don’t bundle fonts that Apple ships with the system, makes available for download, or distributes through other channels like [`Apple Fonts`](https://developer.apple.comhttps://developer.apple.com/fonts), such as SF Pro, SF Compact, SF Mono, and New York.

#### Apply the System Font to the Text in Your Views

The system font isn’t a single typeface but a family of related typefaces that the system selects based on the platform, the current locale, and the role of the text. It works best for labels and other text you display in the views of your interface. It supports an extensive range of weights, sizes, and languages, adapts automatically to Dynamic Type and accessibility settings, and updates when the system introduces typographic refinements. Retrieve the system font through the system font APIs rather than by name. Each design within the system font family suits a different purpose:

- SF Pro and SF Compact handle Latin, Cyrillic, and Greek scripts in different sizing contexts.
- SF Pro Rounded provides a softer alternative.
- SF Mono handles monospaced layouts.
- New York provides a serif option.
- Language-specific designs (like SF Arabic, SF Hebrew, SF Armenian, and SF Georgian) give matching scripts the same level of typographic care.

The system picks the appropriate typeface for the current context so your text looks right alongside the rest of the interface.

Each app-builder framework defines how you apply the system font to your text:

- In SwiftUI, retrieve the system font from the [`Font`](https://developer.apple.com/documentation/SwiftUI/Font) type.
- In UIKit, retrieve the system font using the methods of the [`UIFont`](https://developer.apple.com/documentation/UIKit/UIFont) type, or build it from a [`UIFontDescriptor`](https://developer.apple.com/documentation/UIKit/UIFontDescriptor).
- In AppKit, retrieve the system font using the methods of the [`NSFont`](https://developer.apple.com/documentation/AppKit/NSFont) type, or build it from an [`NSFontDescriptor`](https://developer.apple.com/documentation/AppKit/NSFontDescriptor).
- In WebKit, set the CSS `font-family` to one of the generic system identifiers: `system-ui`, `ui-sans-serif`, `ui-serif`, `ui-monospace`, or `ui-rounded`.

The following example applies system fonts to text using a text style and a fixed size:

**SwiftUI**:

```swift
// Scale with a text style and design variant.
Text("Welcome")
    .font(.system(.largeTitle, design: .rounded))

// Use a fixed size with a weight.
Text("Details")
    .font(.system(size: 13, weight: .semibold))
```

**UIKit**:

```swift
// Scale with a text style and design variant.
let descriptor = UIFont.preferredFont(forTextStyle: .largeTitle)
    .fontDescriptor.withDesign(.rounded)!
label.font = UIFont(descriptor: descriptor, size: 0)

// Use a fixed size with a weight.
label.font = UIFont.systemFont(ofSize: 13, weight: .semibold)
```

**AppKit**:

```swift
// Scale with a text style and design variant.
let descriptor = NSFont.preferredFont(forTextStyle: .largeTitle, options: [:])
    .fontDescriptor.withDesign(.rounded)!
textField.font = NSFont(descriptor: descriptor, size: 0)

// Use a fixed size with a weight.
textField.font = NSFont.systemFont(ofSize: 13, weight: .semibold)
```

The [`Font.Design`](https://developer.apple.com/documentation/SwiftUI/Font/Design) type has four cases that each select a different family of typefaces:

| Case | Typeface family |
| --- | --- |
| [`Font.Design.default`](https://developer.apple.com/documentation/SwiftUI/Font/Design/default) | SF Pro (Display and Text); SF Compact in watchOS; and the language-specific designs for matching scripts |
| [`Font.Design.monospaced`](https://developer.apple.com/documentation/SwiftUI/Font/Design/monospaced) | SF Mono |
| [`Font.Design.rounded`](https://developer.apple.com/documentation/SwiftUI/Font/Design/rounded) | SF Pro Rounded; SF Compact Rounded in watchOS |
| [`Font.Design.serif`](https://developer.apple.com/documentation/SwiftUI/Font/Design/serif) | New York |

The system provides dedicated APIs for retrieving system fonts, and those APIs ensure you receive a font that adapts correctly to different situations. If you retrieve system fonts by name, you receive a font with the same appearance but lose many of the dynamic properties that make system fonts so useful. For example, the font might not display correctly in all languages, or have different spacing or hyphenation.

> **Note**: SF Pro, SF Pro Rounded, SF Compact, SF Compact Rounded, SF Mono, SF Arabic, SF Hebrew, SF Armenian, SF Georgian, and New York are reserved for system use. Designers can download these fonts from [`Apple Fonts`](https://developer.apple.comhttps://developer.apple.com/fonts) to preview them in mockups; that’s a separate, design-time workflow that doesn’t change how your app retrieves fonts at runtime.

#### Retrieve Document Fonts By Name

Apple platforms ship with a large collection of document fonts — typefaces people choose for their own content, such as documents, messages, and layouts. Retrieve a document font by its PostScript name using the same font APIs your app uses for the system font:

- In UIKit and AppKit, use [`init(name:size:)`](https://developer.apple.com/documentation/UIKit/UIFont/init(name:size:)) or [`init(name:size:)`](https://developer.apple.com/documentation/AppKit/NSFont/init(name:size:)) to create a font from a name and size. For finer control over font traits and selection, use [`UIFontDescriptor`](https://developer.apple.com/documentation/UIKit/UIFontDescriptor) or [`NSFontDescriptor`](https://developer.apple.com/documentation/AppKit/NSFontDescriptor).
- In SwiftUI, use [`custom(_:fixedSize:)`](https://developer.apple.com/documentation/SwiftUI/Font/custom(_:fixedSize:)) or one of the related custom font initializers.
- In WebKit, include the desired font name as the first entry in the CSS `font-family` list.

The set of pre-installed document fonts varies by platform: macOS ships the full collection, while iOS, iPadOS, and visionOS pre-install a smaller set. The complete list is available at [`System Fonts`](https://developer.apple.comhttps://developer.apple.com/fonts/system-fonts/), and people can install the rest through Font Book in macOS or the Fonts settings in iOS.

#### Download Additional Fonts on Demand

Some fonts in Apple’s document font library don’t come installed by default, but you can download them on demand. These are the same Apple-provided fonts listed at [`System Fonts`](https://developer.apple.comhttps://developer.apple.com/fonts/system-fonts/) — you identify them by PostScript name. To make one available to your app, create a font descriptor for it and pass it to the font matching APIs in [`Core Text`](https://developer.apple.com/documentation/CoreText). After the download completes, the font behaves like any other installed font, and you can retrieve it by name. Downloadable fonts aren’t supported in watchOS or tvOS.

> ❗ **Important**: To use or enumerate downloaded fonts in iOS, your app must add the Fonts capability with the Use Installed Fonts option enabled. See [`Add the Fonts capability for iOS`](https://developer.apple.com#Add-the-Fonts-capability-for-iOS) for details.

The following example requests a download for a specific font and retrieves it on completion:

```swift
let attributes = [kCTFontNameAttribute: "Georgia"] as CFDictionary
let descriptor = CTFontDescriptorCreateWithAttributes(attributes)

CTFontDescriptorMatchFontDescriptorsWithProgressHandler([descriptor] as CFArray, nil) { state, _ in
    if state == .didFinish {
        // Font is now available; retrieve it by PostScript name.
        let font = CTFontCreateWithName("Georgia" as CFString, 17, nil)
    }
    return true
}
```

Don’t call [`CTFontManagerRegisterFontURLs(_:_:_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontManagerRegisterFontURLs(_:_:_:_:)) on fonts you download using [`CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_:_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_:_:_:)). Apple document fonts are system-managed, and after the download completes they’re available by PostScript name automatically. Use [`CTFontManagerRegisterFontURLs(_:_:_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontManagerRegisterFontURLs(_:_:_:_:)) only for fonts you own and bundle with your app.

#### Bundle a Custom Font with Your App

When the system and document fonts don’t include the typeface your design calls for, such as a brand-specific font your team licensed, bundle the font with your app. Bundled fonts live alongside your app’s other resources and are available only within the process that registers them. Other apps can’t see or use them.

Place your font files in your app’s bundle, an asset catalog, or an Apple-hosted asset pack, and register them at launch as described in [`Applying custom fonts to text`](https://developer.apple.com/documentation/SwiftUI/Applying-Custom-Fonts-to-Text) for SwiftUI or [`Adding a custom font to your app`](https://developer.apple.com/documentation/UIKit/adding-a-custom-font-to-your-app) for UIKit. After registration, you retrieve a bundled font by its PostScript name using the standard font APIs, and the font appears in system-provided pickers like the macOS Font Panel and [`UIFontPickerViewController`](https://developer.apple.com/documentation/UIKit/UIFontPickerViewController) in iOS.

To register a bundled font manually, use the font manager in Core Text at launch time, and pass the font file URL with `.process` scope. If your app downloads fonts itself, register them as soon as the download finishes. In macOS, you can also install a font your app downloads itself at the system level, as described in [`Install fonts for systemwide use`](https://developer.apple.com#Install-fonts-for-systemwide-use); that option isn’t available in iOS or visionOS.

```swift
if let fontURL = Bundle.main.url(forResource: "MyFont-Regular", withExtension: "ttf") {
    CTFontManagerRegisterFontURLs([fontURL] as CFArray, .process, true) { errors, done in
        // Handle any registration errors.
        return true
    }
}
```

Registration makes your bundled fonts visible in system font managers and pickers like the macOS Font Panel and [`UIFontPickerViewController`](https://developer.apple.com/documentation/UIKit/UIFontPickerViewController). If you want a font available to your app but not visible in those interfaces — for example, a font used internally for rendering — create a font descriptor directly from the file without registering it:

```swift
// From a file URL:
if let fontURL = Bundle.main.url(forResource: "MyFont-Regular", withExtension: "ttf"),
   let descriptors = CTFontManagerCreateFontDescriptorsFromURL(fontURL as CFURL) as? [CTFontDescriptor],
   let descriptor = descriptors.first {
    let font = CTFontCreateWithFontDescriptor(descriptor, 17, nil)
}

// From data:
if let fontData = NSDataAsset(name: "MyFont")?.data {
    let descriptors = CTFontManagerCreateFontDescriptorsFromData(fontData as CFData) as! [CTFontDescriptor]
    if let descriptor = descriptors.first {
        let font = CTFontCreateWithFontDescriptor(descriptor, 17, nil)
    }
}
```

Both functions return an array of [`CTFontDescriptor`](https://developer.apple.com/documentation/CoreText/CTFontDescriptor) objects you can use to construct fonts.

#### Share a Bundled Font with Your Widget Extension

Widget extensions, like other app extensions, package into an `.appex` bundle nested inside your app’s bundle (for example, at `MyApp.app/PlugIns/MyWidgetExtension.appex`), and the extension has read-access to the resources in that containing bundle. This means your widget can use a font your app bundles without installing that font systemwide, which would require the person’s explicit permission.

From your widget’s code, locate the font in the containing app’s bundle and register it for your widget’s own process:

```swift
import CoreText

enum SharedFont {
    private static var didRegister = false

    static func registerFromAppBundle() {
        guard !didRegister else { return }
        didRegister = true

        // `Bundle.main` is the widget's `.appex`, not the app's bundle; go up two levels to reach it.
        let appBundleURL = Bundle.main.bundleURL
            .deletingLastPathComponent()   // .app/PlugIns
            .deletingLastPathComponent()   // .app
        let fontURL = appBundleURL.appendingPathComponent("MyFont-Regular.ttf")

        var error: Unmanaged<CFError>?
        CTFontManagerRegisterFontsForURL(fontURL as CFURL, .process, &error)
    }
}
```

Call this method before your widget’s views render, such as from your widget bundle’s initializer.

Alternatively, put the font in a framework that both your app and your widget extension link against. Each target registers its own copy of the font from the framework’s bundle at launch, so neither target needs to read the other’s bundle.

#### Install Fonts for Systemwide Use

You can install a custom font at the system level to make it available to other, unrelated apps (for example, if you distribute a suite of apps that share a common typeface). Font management apps like Font Book in macOS and the Fonts pane in iOS Settings let people install fonts this way.

> 💡 **Tip**: To share a bundled font with your own widget extension, you don’t need to install it systemwide. See [`Share a bundled font with your widget extension`](https://developer.apple.com#Share-a-bundled-font-with-your-widget-extension) instead.

Use the same Core Text registration API your app uses for bundled fonts, but change the scope from [`CTFontManagerScope.process`](https://developer.apple.com/documentation/CoreText/CTFontManagerScope/process) to [`CTFontManagerScope.persistent`](https://developer.apple.com/documentation/CoreText/CTFontManagerScope/persistent):

```swift
public func CTFontManagerRegisterFontURLs(
    _ fontURLs: CFArray,
    _ scope: CTFontManagerScope, /* use .persistent */
    _ enabled: Bool,
    _ registrationHandler: ((CFArray, Bool) -> Bool)?)
```

Call this from your app at an appropriate time, such as when a person enables a feature that requires the font. In iOS and visionOS, when you call this, the system prompts the person to grant permission, similar to other system permission requests. In macOS, you don’t need to request permission first.

#### Add the Fonts Capability for Ios

To add this capability to your app, follow the steps in [`Configuring custom fonts`](https://developer.apple.com/documentation/Xcode/configuring-custom-fonts). Declaring it lets the system mediate your app’s access to installed fonts.

To let someone select an installed font, present a [`UIFontPickerViewController`](https://developer.apple.com/documentation/UIKit/UIFontPickerViewController) in iOS. The picker displays a system-provided interface, so your app never sees the complete list of fonts installed on the device, only the font the person selects. This protects the person’s privacy by keeping your app from using the full list of installed fonts to fingerprint their device.

If [`UIFontPickerViewController`](https://developer.apple.com/documentation/UIKit/UIFontPickerViewController) doesn’t fit your app’s needs, you can request the [`Font Enumeration entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/font-enumeration/) from Apple. The request requires a justification describing why the picker is insufficient and how your app avoids using the broader access — the ability to enumerate every installed font — to fingerprint or track the person, and limits it to the font-selection features your app actually needs.

#### Access Fonts From Third Party and Low Level Frameworks

When building apps with cross-platform frameworks, retrieve fonts using the underlying platform’s font APIs in SwiftUI, UIKit, AppKit, or Core Text and pass the result into the framework through whatever mechanism it provides for referencing platform-specific objects. This gives your app access to the full distinction between system fonts and document fonts, including fonts available for download on demand, and provides the same correctness, adaptability, and language coverage that apps built directly on Apple’s frameworks benefit from.

If you draw text using lower-level libraries, such as FreeType, your code typically references font files by their location on disk. Keep in mind that the system may move, replace, or update font files between releases, and the changes may not be backward-compatible with the library you’re using. Verify that each font your app needs is available before using it, and design a fallback path so your app continues to work when a font is missing or has changed.

###### Related Topics


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/fonts)*