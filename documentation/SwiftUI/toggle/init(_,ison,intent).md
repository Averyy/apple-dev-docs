# init(_:isOn:intent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle performing an `AppIntent` and generates its label from a localized string key.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isOn: Bool, intent: some AppIntent)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, isOn: Bool, intent: some AppIntent)
```

```swift
nonisolated
init<S>(_ title: S, isOn: Bool, intent: some AppIntent) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See `Text` for more information about localizing strings.

To initialize a toggle with a string variable, use [`init(_:isOn:intent:)`](./init%28_,ison,intent%29.md) instead.

## Parameters

- `titleKey`: The key for the toggle’s localized title, that describes the purpose of the toggle.
- `isOn`: Whether the toggle is on or off.
- `intent`: The `AppIntent` to be performed.

## See Also

### Creating a toggle for an App Intent
- [init<I>(isOn: Bool, intent: I, label: () -> Label)](./init%28ison,intent,label%29.md)
  Creates a toggle performing an `AppIntent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:ison:intent:))*