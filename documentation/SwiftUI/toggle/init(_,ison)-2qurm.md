# init(_:isOn:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle that generates its label from a string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, isOn: Binding<Bool>) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, isOn: Binding<Bool>)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isOn: Binding<Bool>)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the toggle.
- `isOn`: A binding to a property that indicates whether the toggle is on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:ison:)-2qurm)*