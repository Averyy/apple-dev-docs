# Image.DynamicRange

**Framework**: SwiftUI  
**Kind**: struct

The range of brightness that an image is allowed to draw.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct DynamicRange
```

#### Overview

A high dynamic range image stores highlights brighter than white. Pass a value of this type to [`allowedDynamicRange(_:)`](image/alloweddynamicrange(_:).md) to say how much of that extra brightness reaches the display:

```swift
Image("sunset")
    .allowedDynamicRange(.constrainedHigh)
```

Use [`high`](image/dynamicrange/high.md) when the image is the subject of the screen and you want it at full brightness. Prefer [`constrainedHigh`](image/dynamicrange/constrainedhigh.md) when the image appears next to an ordinary interface, because an unrestricted image can make the content around it look dim. [`standard`](image/dynamicrange/standard.md) holds the image to the same range as the rest of the interface.

## Topics

### Getting dynamic range values
- [static let standard: Image.DynamicRange](image/dynamicrange/standard.md)
  Restrict the image content dynamic range to the standard range.
- [static let high: Image.DynamicRange](image/dynamicrange/high.md)
  Allow image content to use an unrestricted extended range.
- [static let constrainedHigh: Image.DynamicRange](image/dynamicrange/constrainedhigh.md)
  Allow image content to use some extended range. This is appropriate for placing HDR content next to SDR content.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func allowedDynamicRange(Image.DynamicRange?) -> Image](image/alloweddynamicrange(_:).md)
  Returns a new image configured with the specified allowed dynamic range.
- [var allowedDynamicRange: Image.DynamicRange?](environmentvalues/alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/dynamicrange)*