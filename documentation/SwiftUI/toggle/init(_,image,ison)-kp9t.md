# init(_:image:isOn:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle that generates its label from a string and image resource.

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
nonisolated
init<S>(_ title: S, image: ImageResource, isOn: Binding<Bool>) where S : StringProtocol
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, isOn: Binding<Bool>)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, isOn: Binding<Bool>)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf.  See `Text` for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the toggle.
- `image`: The name of the image resource to lookup.
- `isOn`: A binding to a property that indicates whether the toggle is on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:image:ison:)-kp9t)*