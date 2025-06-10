# ShortcutTileColor

**Framework**: App Intents  
**Kind**: enum

Describes the colors a shortcut tile in the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum ShortcutTileColor
```

## Topics

### Getting the tile colors
- [ShortcutTileColor.blue](shortcuttilecolor/blue.md)
  A blue color.
- [ShortcutTileColor.grape](shortcuttilecolor/grape.md)
  A grape color.
- [ShortcutTileColor.grayBlue](shortcuttilecolor/grayblue.md)
  A grayish-blue color.
- [ShortcutTileColor.grayBrown](shortcuttilecolor/graybrown.md)
  A grayish-brown color.
- [ShortcutTileColor.grayGreen](shortcuttilecolor/graygreen.md)
  A grayish-green color.
- [ShortcutTileColor.lightBlue](shortcuttilecolor/lightblue.md)
  A light blue color.
- [ShortcutTileColor.lime](shortcuttilecolor/lime.md)
  A lime color.
- [ShortcutTileColor.navy](shortcuttilecolor/navy.md)
  A navy blue color.
- [ShortcutTileColor.orange](shortcuttilecolor/orange.md)
  An orange color.
- [ShortcutTileColor.pink](shortcuttilecolor/pink.md)
  A pink color.
- [ShortcutTileColor.purple](shortcuttilecolor/purple.md)
  A purple color.
- [ShortcutTileColor.red](shortcuttilecolor/red.md)
  A red color.
- [ShortcutTileColor.tangerine](shortcuttilecolor/tangerine.md)
  A tangerine color.
- [ShortcutTileColor.teal](shortcuttilecolor/teal.md)
  A teal color.
- [ShortcutTileColor.yellow](shortcuttilecolor/yellow.md)
  A yellow color.
### Operators
- [static func == (ShortcutTileColor, ShortcutTileColor) -> Bool](shortcuttilecolor/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](shortcuttilecolor/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](shortcuttilecolor/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](shortcuttilecolor/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AppShortcut](appshortcut.md)
  A type that defines a preconfigured shortcut for a specific app intent.
- [struct AppShortcutPhrase](appshortcutphrase.md)
  A spoken phrase that causes the system to run the corresponding App Shortcut.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcuttilecolor)*