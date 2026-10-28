# init(_:intent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that performs an `AppIntent` and generates its label from a string.

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
init<S>(_ title: S, intent: some AppIntent) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, intent: some AppIntent)
```

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, intent: some AppIntent)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29-9d1g4.md). See [`Text`](../text.md) for more information about localizing strings.

To initialize a button with a localized string key, use [`init(_:intent:)`](./init%28_,intent%29.md) instead.

## Parameters

- `title`: A string that describes the purpose of the button’s `intent`.
- `intent`: The `AppIntent` to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:intent:)-1aqo4)*