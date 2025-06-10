# init(Yp:Cr_R:Cr_G:Cb_G:Cb_B:)

**Framework**: Accelerate  
**Kind**: init

Creates a 3 x 3 matrix for converting Y’CbCr signals to RGB.

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
init(Yp: Float, Cr_R: Float, Cr_G: Float, Cb_G: Float, Cb_B: Float)
```

#### Return Value

A 3 x 3 matrix for converting Y’CbCr signals to RGB.

#### Discussion

The vImage library uses this matrix to convert from YpCbCr to RGB using the following multiplication:

```None
                    | R |   | Yp    0     Cr_R |   | Y' |
                    | G | = | Yp   Cb_G   Cr_G | * | Cb |
                    | B |   | Yp   Cb_B     0  |   | Cr |
```

## Parameters

- `Yp`: The   in the conversion matrix.
- `Cr_R`: The   in the conversion matrix.
- `Cr_G`: The   in the conversion matrix.
- `Cb_G`: The   in the conversion matrix.
- `Cb_B`: The   in the conversion matrix.

## See Also

- [init()](vimage_ypcbcrtoargbmatrix/init.md)
  Creates a 3 x 3 zero matrix for converting Y’CbCr signals to RGB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_ypcbcrtoargbmatrix/init(yp:cr_r:cr_g:cb_g:cb_b:))*