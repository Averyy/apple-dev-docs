# colorYCbCrMatrix

**Framework**: AVFoundation  
**Kind**: property

The YCbCr matrix used for video composition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var colorYCbCrMatrix: String? { get set }
```

## Mentions

- [Tagging media with video color information](tagging-media-with-video-color-information.md)

#### Discussion

The default value is `nil`. When the value of this property is `nil`, the source’s matrix is propagated and used. Valid values are those suitable for [`AVVideoYCbCrMatrixKey`](avvideoycbcrmatrixkey.md).

## See Also

- [var colorPrimaries: String?](avmutablevideocomposition/colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](avmutablevideocomposition/colortransferfunction.md)
  The transfer function used for video composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/colorycbcrmatrix)*