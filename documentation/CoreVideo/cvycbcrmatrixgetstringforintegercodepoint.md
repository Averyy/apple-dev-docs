# CVYCbCrMatrixGetStringForIntegerCodePoint(_:)

**Framework**: Core Video  
**Kind**: func

Returns the Core Video YCbCr matrix string corresponding to the standard integer code point that you specify.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func CVYCbCrMatrixGetStringForIntegerCodePoint(_ yCbCrMatrixCodePoint: Int32) -> Unmanaged<CFString>?
```

#### Return Value

The YCbCr matrix string corresponding to the code point (See [`Image Buffer YCbCr Matrix Constants`](image-buffer-ycbcr-matrix-constants.md) for possible values.), or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if the code point is `2` (unknown) or the system doesn’t recognize it.

## Parameters

- `yCbCrMatrixCodePoint`: The standard integer code point.

## See Also

- [func CVColorPrimariesGetIntegerCodePointForString(CFString?) -> Int32](cvcolorprimariesgetintegercodepointforstring(_:).md)
  Returns the standard integer code point corresponding to the Core Video color primaries constant string that you specify.
- [func CVColorPrimariesGetStringForIntegerCodePoint(Int32) -> Unmanaged<CFString>?](cvcolorprimariesgetstringforintegercodepoint(_:).md)
  Returns the Core Video color primaries string corresponding to the standard integer code point that you specify.
- [func CVTransferFunctionGetIntegerCodePointForString(CFString?) -> Int32](cvtransferfunctiongetintegercodepointforstring(_:).md)
  Returns the standard integer code point corresponding to the Core Video transfer function string that you specify.
- [func CVTransferFunctionGetStringForIntegerCodePoint(Int32) -> Unmanaged<CFString>?](cvtransferfunctiongetstringforintegercodepoint(_:).md)
  Returns the Core Video transfer function string corresponding to the standard integer code point that you specify.
- [func CVYCbCrMatrixGetIntegerCodePointForString(CFString?) -> Int32](cvycbcrmatrixgetintegercodepointforstring(_:).md)
  Returns the standard integer code point corresponding to the Core Video YCbCr matrix string that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvycbcrmatrixgetstringforintegercodepoint(_:))*