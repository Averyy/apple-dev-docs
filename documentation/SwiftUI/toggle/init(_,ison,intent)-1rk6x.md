# init(_:isOn:intent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle that generates its label from a string.

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
init<S>(_ title: S, isOn: Bool, intent: some AppIntent) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isOn: Bool, intent: some AppIntent)
```

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, isOn: Bool, intent: some AppIntent)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29-9d1g4.md). See `Text` for more information about localizing strings.

To initialize a toggle with a localized string key, use [`init(_:isOn:intent:)`](./init%28_,ison,intent%29.md) instead.

## Parameters

- `title`: A string that describes the purpose of the toggle.
- `isOn`: Whether the toggle is on or off.
- `intent`: The `AppIntent` to be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:ison:intent:)-1rk6x)*