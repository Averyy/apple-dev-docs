# Image.DynamicRange

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

A high dynamic range image stores highlights brighter than white. Pass a value of this type to [`allowedDynamicRange(_:)`](./alloweddynamicrange%28_%29.md) to say how much of that extra brightness reaches the display:

```swift
Image("sunset")
    .allowedDynamicRange(.constrainedHigh)
```

Use [`high`](./dynamicrange/high.md) when the image is the subject of the screen and you want it at full brightness. Prefer [`constrainedHigh`](./dynamicrange/constrainedhigh.md) when the image appears next to an ordinary interface, because an unrestricted image can make the content around it look dim. [`standard`](./dynamicrange/standard.md) holds the image to the same range as the rest of the interface.

## Topics

### Getting dynamic range values
- [static let standard: Image.DynamicRange](./dynamicrange/standard.md)
  Restrict the image content dynamic range to the standard range.
- [static let high: Image.DynamicRange](./dynamicrange/high.md)
  Allow image content to use an unrestricted extended range.
- [static let constrainedHigh: Image.DynamicRange](./dynamicrange/constrainedhigh.md)
  Allow image content to use some extended range. This is appropriate for placing HDR content next to SDR content.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying dynamic range
- [func allowedDynamicRange(Image.DynamicRange?) -> Image](./alloweddynamicrange%28_%29.md)
  Returns a new image configured with the specified allowed dynamic range.
- [var allowedDynamicRange: Image.DynamicRange?](../environmentvalues/alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/dynamicrange)*