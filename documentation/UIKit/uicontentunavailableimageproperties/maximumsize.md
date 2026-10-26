# maximumSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A maximum size for the image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic) CGSize maximumSize;
```

#### Discussion

The default value is [`CGSizeZero`](../../CoreGraphics/cgsizezero.md). Setting a [`width`](../../CoreFoundation/cgsize/width.md) or [`height`](../../CoreFoundation/cgsize/height.md) of zero makes the size unconstrained on that dimension. If the image exceeds [`maximumSize`](../uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/maximumsize.md) size on either dimension, the view reduces its size proportionately, maintaining aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentunavailableimageproperties/maximumsize)*