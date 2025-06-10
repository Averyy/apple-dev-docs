# init(Yp_bias:CbCr_bias:YpRangeMax:CbCrRangeMax:YpMax:YpMin:CbCrMax:CbCrMin:)

**Framework**: Accelerate  
**Kind**: init

Returns a structure describing range and clamping information for Y’CbCr pixel formats.

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
init(Yp_bias: Int32, CbCr_bias: Int32, YpRangeMax: Int32, CbCrRangeMax: Int32, YpMax: Int32, YpMin: Int32, CbCrMax: Int32, CbCrMin: Int32)
```

#### Return Value

A structure describing range and clamping information for Y’CbCr pixel formats.

## Parameters

- `Yp_bias`: The encoding for   for this video format (varies by bit depth).
- `CbCr_bias`: The encoding for   for this video format. This is usually the middle of the range of CbCr, not the low end.
- `YpRangeMax`: The encoding for   for this video format. For video range, this is typically less than the maximum representable value.
- `CbCrRangeMax`: The encoding for   for this video format. This is usually near the high end of the encodable range (e.g.  ), if not the maximum encodable value (e.g.  ).
- `YpMax`: The encoding for the maximum allowed Y’ value. All values larger than this will be clamped to this value.
- `YpMin`: The encoding of the minimum allowed Y’ value. All values less than this will be clamped to this value.
- `CbCrMax`: The encoding of the maximum allowed   value. All chroma values greater than this value will be clamped to this value.
- `CbCrMin`: The encoding of the minimum allowed   value. All chroma values less than this value will be clamped to this value.

## See Also

- [init()](vimage_ypcbcrpixelrange/init.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_ypcbcrpixelrange/init(yp_bias:cbcr_bias:yprangemax:cbcrrangemax:ypmax:ypmin:cbcrmax:cbcrmin:))*