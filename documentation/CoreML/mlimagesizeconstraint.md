# MLImageSizeConstraint

**Framework**: Core ML  
**Kind**: class

A list or range of sizes that augment an image constraint’s default size.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MLImageSizeConstraint
```

#### Overview

You use an `MLImageSizeConstraint` to express what image sizes of an image feature a model will accept as input or produce as output.

Use [`type`](mlimagesizeconstraint/type.md) to determine which properties describe what image sizes the model’s image feature expects as input or produces as output.

If `type` is:

- [`MLImageSizeConstraintType.range`](mlimagesizeconstrainttype/range.md), the image feature accepts any image that has a width in [`pixelsWideRange`](mlimagesizeconstraint/pixelswiderange.md) and a height in [`pixelsHighRange`](mlimagesizeconstraint/pixelshighrange.md).
- [`MLImageSizeConstraintType.enumerated`](mlimagesizeconstrainttype/enumerated.md), the image feature accepts any image size listed in [`enumeratedImageSizes`](mlimagesizeconstraint/enumeratedimagesizes.md).
- [`MLImageSizeConstraintType.unspecified`](mlimagesizeconstrainttype/unspecified.md), the `MLImageSizeConstraint` instance is not configured and should be ignored. Instead, use the image feature’s default image size constraint, defined by [`pixelsWide`](mlimageconstraint/pixelswide.md) and [`pixelsHigh`](mlimageconstraint/pixelshigh.md).

![Graph diagram showing the constraint’s rectangle defined by the width and height ranges of the constraint, and a blue rectangle, representing a valid image size. The diagram’s X-axis spans from 0 to 250 pixels and the Y-axis spans from 0 to 200 pixels. The constraint rectangle, which has a dashed outline, has a width that spans from 50 to 250 pixels, and a height that spans from 100 to 200 pixels. The sample image size has its lower-left corner at the graph’s origin and its upper-right corner is within the bounds of the constraint rectangle, at 150 pixels wide by 180 pixels high.](https://docs-assets.developer.apple.com/published/d99ccb61d4b994effa121d2a119b98ff/media-3027121%402x.png)

## Topics

### Determining Relevant Constraints
- [var type: MLImageSizeConstraintType](mlimagesizeconstraint/type.md)
  Indicator of which properties to inspect for this image size constraint.
- [enum MLImageSizeConstraintType](mlimagesizeconstrainttype.md)
  The modes that determine how the model defines a feature’s image size constraint.
### Accessing the Image Size Ranges
- [var pixelsWideRange: NSRange](mlimagesizeconstraint/pixelswiderange.md)
  The range of widths a model’s image feature accepts as input or produces as output.
- [var pixelsHighRange: NSRange](mlimagesizeconstraint/pixelshighrange.md)
  The range of heights a model’s image feature accepts as input or produces as output.
### Accessing the Enumerated Image Sizes
- [var enumeratedImageSizes: [MLImageSize]](mlimagesizeconstraint/enumeratedimagesizes.md)
  An array of image sizes a model’s image feature accepts as input or produces as output.
- [class MLImageSize](mlimagesize.md)
  The width and height of an image feature size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var sizeConstraint: MLImageSizeConstraint](mlimageconstraint/sizeconstraint.md)
  Additional sizes this image feature supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlimagesizeconstraint)*