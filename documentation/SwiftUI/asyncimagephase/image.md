# image

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The loaded image, if any.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var image: Image? { get }
```

#### Discussion

If this value isn’t `nil`, the image load operation has finished, and you can use the image to update the view. You can use the image directly, or you can modify it in some way. For example, you can add a [`resizable(capInsets:resizingMode:)`](../image/resizable%28capinsets,resizingmode%29.md) modifier to make the image resizable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/asyncimagephase/image)*