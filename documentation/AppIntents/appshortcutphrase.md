# AppShortcutPhrase

**Framework**: App Intents  
**Kind**: struct

A spoken phrase that causes the system to run the corresponding App Shortcut.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct AppShortcutPhrase<Intent> where Intent : AppIntent
```

## Topics

### Creating a shortcut phrase
- [init(String)](appshortcutphrase/init(_:).md)
- [init(stringLiteral: String)](appshortcutphrase/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(stringInterpolation: AppShortcutPhrase<Intent>.StringInterpolation)](appshortcutphrase/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [AppShortcutPhrase.StringInterpolation](appshortcutphrase/stringinterpolation.md)
  The type each segment of a string literal containing interpolations should be appended to.
- [enum AppShortcutPhraseToken](appshortcutphrasetoken.md)
  Dynamic values you can include in the spoken phrases that run your shortcut.
### Type Aliases
- [AppShortcutPhrase.ExtendedGraphemeClusterLiteralType](appshortcutphrase/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [AppShortcutPhrase.StringLiteralType](appshortcutphrase/stringliteraltype.md)
  A type that represents a string literal.
- [AppShortcutPhrase.UnicodeScalarLiteralType](appshortcutphrase/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](appshortcutphrase/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](appshortcutphrase/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [struct AppShortcut](appshortcut.md)
  A type that defines a preconfigured shortcut for a specific app intent.
- [struct NegativeAppShortcutPhrase](negativeappshortcutphrase.md)
  An object that represents a negative phrase.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrase)*