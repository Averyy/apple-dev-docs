# init(R_Yp:G_Yp:B_Yp:R_Cb:G_Cb:B_Cb_R_Cr:G_Cr:B_Cr:)

**Framework**: Accelerate  
**Kind**: init

Creates a 3 x 3 matrix for converting RGB to Y’CbCr.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(R_Yp: Float, G_Yp: Float, B_Yp: Float, R_Cb: Float, G_Cb: Float, B_Cb_R_Cr: Float, G_Cr: Float, B_Cr: Float)
```

#### Discussion

The 3 x 3 matrix is given by:

![None](https://docs-assets.developer.apple.com/published/cd4c896355cac49fedbe25a83dcb644c/media-2941901%402x.png)

## Parameters

- `R_Yp`: The   in the conversion matrix.
- `G_Yp`: The   in the conversion matrix.
- `B_Yp`: The   in the conversion matrix.
- `R_Cb`: The   in the conversion matrix.
- `G_Cb`: The   in the conversion matrix.
- `B_Cb_R_Cr`: The   in the conversion matrix.
- `G_Cr`: The   in the conversion matrix.
- `B_Cr`: The   in the conversion matrix.

## See Also

- [init()](vimage_argbtoypcbcrmatrix/init.md)
  Creates a 3 x 3 zero matrix for converting RGB to Y’CbCr.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_argbtoypcbcrmatrix/init(r_yp:g_yp:b_yp:r_cb:g_cb:b_cb_r_cr:g_cr:b_cr:))*