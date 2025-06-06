# CLKComplicationTemplateCircularSmallSimpleImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a single image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateCircularSmallSimpleImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.circularSmall`](clkcomplicationfamily/circularsmall.md) family.

![A diagram showing the layout of the small simple image complication. This diagram shows three examples, each displaying a single, small image.](https://docs-assets.developer.apple.com/published/15a48345c3a1c9f364f2d68dbe51816e/media-2933735%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 32 pixels | 32 pixels |
| 40 mm | 36 pixels | 36 pixels |
| 41 mm | 38 pixels | 38 pixels |
| 42 mm | 36 pixels | 36 pixels |
| 44 mm | 40 pixels | 40 pixels |
| 45 mm | 43 pixels | 43 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKImageProvider)](clkcomplicationtemplatecircularsmallsimpleimage/init(imageprovider:).md)
  Creates a new template from the provided image.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](clkcomplicationtemplatecircularsmallsimpleimage/imageprovider.md)
  The image to display in the complication.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateCircularSmallRingImage](clkcomplicationtemplatecircularsmallringimage.md)
  A template for displaying a single image surrounded by a configurable progress ring.
- [class CLKComplicationTemplateCircularSmallStackImage](clkcomplicationtemplatecircularsmallstackimage.md)
  A template for displaying an image with a line of text below it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallsimpleimage)*