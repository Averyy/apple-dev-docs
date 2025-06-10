# AppShortcutsBuilder

**Framework**: App Intents  
**Kind**: enum

A result builder that allows you to declaratively describe the App Shortcuts that your app provides.

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
@resultBuilder
enum AppShortcutsBuilder
```

## Topics

### Building App Shortcuts
- [static func buildBlock() -> [AppShortcut]](appshortcutsbuilder/buildblock.md)
- [static func buildBlock(AppShortcut...) -> [AppShortcut]](appshortcutsbuilder/buildblock(_:)-110ow.md)
- [static func buildBlock([AppShortcut]...) -> [AppShortcut]](appshortcutsbuilder/buildblock(_:)-8xfbe.md)
- [static func buildExpression(AppShortcut) -> AppShortcut](appshortcutsbuilder/buildexpression(_:)-31qci.md)
- [static func buildExpression(AppShortcut) -> [AppShortcut]](appshortcutsbuilder/buildexpression(_:)-9u47j.md)
- [static func buildLimitedAvailability([AppShortcut]) -> any _AppShortcutsContentMarker & _LimitedAvailabilityAppShortcutsContentMarker](appshortcutsbuilder/buildlimitedavailability(_:).md)
- [static func buildOptional((any _AppShortcutsContentEmitterMarker & _AppShortcutsContentMarker & _LimitedAvailabilityAppShortcutsContentMarker)?) -> [AppShortcut]](appshortcutsbuilder/buildoptional(_:)-3pbr9.md)
- [static func buildOptional((any _AppShortcutsContentMarker & _LimitedAvailabilityAppShortcutsContentMarker)?) -> [AppShortcut]](appshortcutsbuilder/buildoptional(_:)-4urzx.md)

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
- [enum ShortcutTileColor](shortcuttilecolor.md)
  Describes the colors a shortcut tile in the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutsbuilder)*