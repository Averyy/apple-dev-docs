# NegativeAppShortcutPhrase

**Framework**: App Intents  
**Kind**: struct

An object that represents a negative phrase.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct NegativeAppShortcutPhrase
```

#### Overview

Each negative phrase will be used to populate an app-level negative training set. This set will contain phrases that will completely bypass your app.

## Topics

### Structures
- [NegativeAppShortcutPhrase.StringInterpolation](negativeappshortcutphrase/stringinterpolation.md)
  A string you construct using literal values, content from intent parameters, and other interpolated values.
### Initializers
- [init(String)](negativeappshortcutphrase/init(_:).md)
- [init(stringInterpolation: NegativeAppShortcutPhrase.StringInterpolation)](negativeappshortcutphrase/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [init(stringLiteral: StringLiteralType)](negativeappshortcutphrase/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
### Type Aliases
- [NegativeAppShortcutPhrase.ExtendedGraphemeClusterLiteralType](negativeappshortcutphrase/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [NegativeAppShortcutPhrase.StringLiteralType](negativeappshortcutphrase/stringliteraltype.md)
  A type that represents a string literal.
- [NegativeAppShortcutPhrase.UnicodeScalarLiteralType](negativeappshortcutphrase/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](negativeappshortcutphrase/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](negativeappshortcutphrase/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [struct AppShortcut](appshortcut.md)
  A type that defines a preconfigured shortcut for a specific app intent.
- [struct AppShortcutPhrase](appshortcutphrase.md)
  A spoken phrase that causes the system to run the corresponding App Shortcut.
- [struct NegativeAppShortcutPhrases](negativeappshortcutphrases.md)
  This is a set of negative phrases, which will all be added to the app-level negative training set. All the training data specified here, will be used to completely bypass your app
- [NSAppIconActionTintColorName](../BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon/NSAppIconActionTintColorName.md)
  The tint color to apply to text and symbols in the App Shortcuts platter.
- [NSAppIconComplementingColorNames](../BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon/NSAppIconComplementingColorNames.md)
  The names of the colors to use for the background of the App Shortcuts platter.
- [enum AppShortcutsBuilder](appshortcutsbuilder.md)
  A result builder that allows you to declaratively describe the App Shortcuts that your app provides.
- [enum ShortcutTileColor](shortcuttilecolor.md)
  Describes the colors a shortcut tile in the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/negativeappshortcutphrase)*