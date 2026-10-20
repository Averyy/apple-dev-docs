# center

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

The content is horizontally and vertically centered in the bounds rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let center: CALayerContentsGravity
```

```c
extern CALayerContentsGravity const kCAGravityCenter;
```

## See Also

### Constants
- [static let top: CALayerContentsGravity](./top.md)
  The content is horizontally centered at the top-edge of the bounds rectangle.
- [static let bottom: CALayerContentsGravity](./bottom.md)
  The content is horizontally centered at the bottom-edge of the bounds rectangle.
- [static let left: CALayerContentsGravity](./left.md)
  The content is vertically centered at the left-edge of the bounds rectangle.
- [static let right: CALayerContentsGravity](./right.md)
  The content is vertically centered at the right-edge of the bounds rectangle.
- [static let topLeft: CALayerContentsGravity](./topleft.md)
  The content is positioned in the top-left corner of the bounds rectangle.
- [static let topRight: CALayerContentsGravity](./topright.md)
  The content is positioned in the top-right corner of the bounds rectangle.
- [static let bottomLeft: CALayerContentsGravity](./bottomleft.md)
  The content is positioned in the bottom-left corner of the bounds rectangle.
- [static let bottomRight: CALayerContentsGravity](./bottomright.md)
  The content is positioned in the bottom-right corner of the bounds rectangle.
- [static let resize: CALayerContentsGravity](./resize.md)
  The content is resized to fit the entire bounds rectangle.
- [static let resizeAspect: CALayerContentsGravity](./resizeaspect.md)
  The content is resized to fit the bounds rectangle, preserving the aspect of the content. If the content does not completely fill the bounds rectangle, the content is centered in the partial axis.
- [static let resizeAspectFill: CALayerContentsGravity](./resizeaspectfill.md)
  The content is resized to completely fill the bounds rectangle, while still preserving the aspect of the content. The content is centered in the axis it exceeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayercontentsgravity/center)*