# colorPrimaries

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The color primaries used for video composition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var colorPrimaries: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * colorPrimaries;
```

## Mentions

- [Tagging media with video color information](../tagging-media-with-video-color-information.md)

## Discussion

The default value is `nil`. When the value of this property is `nil`, the source’s color primaries are propagated and used. Valid values are those suitable for [`AVVideoColorPrimariesKey`](../avvideocolorprimarieskey.md).

## See Also

### Configuring color
- [var colorTransferFunction: String?](./colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](./colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/colorprimaries)*