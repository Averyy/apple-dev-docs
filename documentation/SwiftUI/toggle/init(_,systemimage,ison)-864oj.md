# init(_:systemImage:isOn:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle that generates its label from a string and system image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, isOn: Binding<Bool>) where S : StringProtocol
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, isOn: Binding<Bool>)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, isOn: Binding<Bool>)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the toggle.
- `systemImage`: The name of the image resource to lookup.
- `isOn`: A binding to a property that indicates whether the toggle is on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:systemimage:ison:)-864oj)*