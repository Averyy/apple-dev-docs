# NSLocalizedString(_:tableName:bundle:value:comment:)

**Framework**: Foundation  
**Kind**: func

Returns a localized string from a table that Xcode generates for you when exporting localizations.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSLocalizedString(_ key: String, tableName: String? = nil, bundle: Bundle = Bundle.main, value: String = "", comment: String) -> String
```

#### Return Value

The result of sending [`localizedString(forKey:value:table:)`](bundle/localizedstring(forkey:value:table:).md) to `bundle`, passing the specified `key`, `value`, and `tableName`.

#### Discussion

Use this function to automatically generate a strings files named `[tableName].strings` located in `bundle` from your code when exporting localizations from Xcode or the `genstrings` utility.

For information about inserting plural nouns and units into localized strings, see [`Localizing strings that contain plurals`](https://developer.apple.com/documentation/Xcode/localizing-strings-that-contain-plurals).

> ❗ **Important**:  The values for `key`, `tableName`, `value`, and `comment` must be string literal values. Xcode can read these values from source code to automatically create localization tables when exporting localizations, but it doesn’t resolve string variables. If you want to use string variables, manually create a strings file and use [`localizedString(forKey:value:table:)`](bundle/localizedstring(forkey:value:table:).md) instead. For more information on strings files, see [`String Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6).

##### Choose Meaningful Keys

Words can often have multiple different meanings depending on the context in which they’re used. For example, the word “Book” can be a noun referring to a printed literary work or a verb for the action of making a reservation. Words with different meanings that share the same spelling are heteronyms.

Different languages often have different heteronyms. “Book” is a heteronym in English, but not in French, where the noun translates to “Livre,” and the verb translates to “Réserver.” For this reason, it’s important to translate each phrase appropriately for its semantics and not its phrasing. Assign unique keys to each string, and add a comment describing the context where it appears to the user.

```swift
NSLocalizedString("book-tag-title",
                  value: "Book",
                  comment: "noun: A label attached to literary items in the library.")

NSLocalizedString("book-button-title",
                  value: "Book",
                  comment: "verb: Title of the button that makes a reservation.")
```

For the previous example, the table for the French locale in `fr.lproj/Localized.strings` includes the following lines:

```other
/* noun: A label attached to literary items in the library. */
"book-tag-title" = "Livre";

/* verb: Title of the button that makes a reservation. */
"book-button-title" = "Réserver";
```

##### Avoid String Interpolation

Xcode doesn’t evaluate interpolated strings and string variables when generating strings files from code. Attempting to localize interpolated strings causes Xcode to export something that resembles the original code expression instead of its expected value at runtime. Translators then translate that exported value—leaving international users with a localized string containing code.

The following code with an interpolated string literal has the translator localize the phrase, “The dominant color is (dominantColor)”:

```swift
NSLocalizedString("dominant-color-caption",
                  value: "The dominant color is \(dominantColor)."
                  comment: "Image caption identifying the color that stands-out the most.")
```

```other
/* Image caption identifying the color that stands-out the most. */
"dominant-color-caption" = "The dominant color is (dominantColor).";
```

Instead, to dynamically insert values within localized strings, set `value` to a format string, and use [`localizedStringWithFormat(_:_:)`](https://developer.apple.com/documentation/Swift/String/localizedStringWithFormat(_:_:)) to insert those values.

```swift
let format = NSLocalizedString("dominant-color-caption",
                               value: "The dominant color is %@.",
                               comment: "Image caption identifying the color that stands-out the most.")
let localizedString = String.localizedStringWithFormat(format, favoriteColor)
```

```other
/* Image caption identifying the color that stands-out the most. */
"dominant-color-copation" = "The dominant color is %@.";
```

For information about inserting plural nouns and units into localized strings, see [`Localizing strings that contain plurals`](https://developer.apple.com/documentation/Xcode/localizing-strings-that-contain-plurals).

##### Avoid Multiline String Literals

Using multiline string literals for strings with newlines can result in unexpected behavior when exporting localizations. Xcode inserts a new line before and after the body of text in the strings file, which translators preserve in their localizations.

```swift
NSLocalizedString("loading-screen.venus-flytrap-fact",
                  value: """
Did you know that venus flytraps have flowers atop very long stems?
The long stem keeps insects a safe distance away from their digestive leaves below.
""",
                  comment: "An interesting fact about venus flytraps shown on the loading screen.")
```

The previous code sample adds the following entry into `Localized.strings` when Xcode exports localizations:

```other
/* An interesting fact about venus flytraps shown on the loading screen. */
"loading-screen.venus-flytrap-fact" = "\nDid you know that venus flytraps have flowers atop very long stems?\nThe long stem keeps insects a safe distance away from their digestive leaves below.\n";
```

You can preserve the aesthetics of mirroring newlines in a string in their code representation by using string concatenation with [`+(_:_:)`](https://developer.apple.com/documentation/Swift/String/+(_:_:)).

```swift
NSLocalizedString("loading-screen.venus-flytrap-fact",
                  value: "Did you know that venus flytraps have flowers atop very long stems?"
                       + "\nThe long stem keeps insects a safe distance away from their digestive leaves below.",
                  comment: "An interesting fact about venus flytraps shown on the loading screen.")
```

```other
/* An interesting fact about venus flytraps shown on the loading screen. */
"loading-screen.venus-flytrap-fact" = "Did you know that venus flytraps have flowers atop very long stems?\nThe long stem keeps insects a safe distance away from their digestive leaves below.";
```

However, because comments aren’t localized, you can safely use multiline string literals with `comment`.

```swift
NSLocalizedString("balloon-image-caption", value: "A bazillion balloons!", comment: """
Caption for an image of a lot of balloons.
The word "bazillion" is intentionally used to invoke a sense of childish excitement.
""")
```

```other
/*
Caption for an image of a lot of balloons.
The word "bazillion" is intentionally used to invoke a sense of childish excitement.
*/
"balloon-image-caption" = "A bazillion balloons!";
```

## Parameters

- `key`: The key for a string in the specified table.
- `tableName`: The name of the table containing the key-value pairs. Also, the suffix for the strings file (a file with th  extension) to store the localized string. This defaults to the table in   when   is   or an empty string.
- `bundle`: The bundle containing the table’s strings file. The main bundle is used if one isn’t specified.
- `value`: The localized string for the development locale. For other locales, return this value if   isn’t found in the table.
- `comment`: The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.

## See Also

- [Exporting localizations](../Xcode/exporting-localizations.md)
  Provide the localizable files from your project to localizers.
- [Importing localizations](../Xcode/importing-localizations.md)
  Import the files that you translate or adapt for a language and region into your project.
- [struct Locale](locale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [class NSOrthography](nsorthography.md)
  A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.
- [protocol CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md)
  A type that provides an out-of-process localizable description.
- [struct URLResource](urlresource.md)
  A resource located at a particular file URL within a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocalizedstring(_:tablename:bundle:value:comment:))*