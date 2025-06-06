# init(_:isOn:intent:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle performing an `AppIntent` and generates its label from a localized string key.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isOn: Bool, intent: some AppIntent)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See `Text` for more information about localizing strings.

To initialize a toggle with a string variable, use [`init(_:isOn:intent:)`](toggle/init(_:ison:intent:).md) instead.

## Parameters

- `titleKey`: The key for the toggle’s localized title, that describes   the purpose of the toggle.
- `isOn`: Whether the toggle is on or off.
- `intent`: The   to be performed.

## See Also

- [init<I>(isOn: Bool, intent: I, label: () -> Label)](toggle/init(ison:intent:label:).md)
  Creates a toggle performing an `AppIntent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:ison:intent:))*