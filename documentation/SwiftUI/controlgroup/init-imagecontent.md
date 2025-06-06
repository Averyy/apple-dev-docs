# init(_:image:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new control group with the specified content that generates its label from a string and image name.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<C, S>(_ title: S, image: ImageResource, @ViewBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol
```

## Parameters

- `title`: A string that describes the contents of the group.

## See Also

- [init(_:systemImage:content:)](controlgroup/init(_:systemimage:content:).md)
  Creates a new control group with the specified content that generates its label from a string and image name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(_:image:content:))*