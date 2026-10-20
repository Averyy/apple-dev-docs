# CVTransferFunctionGetIntegerCodePointForString(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the standard integer code point corresponding to the Core Video transfer function string that you specify.

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
func CVTransferFunctionGetIntegerCodePointForString(_ transferFunctionString: CFString?) -> Int32
```

```c
extern int CVTransferFunctionGetIntegerCodePointForString(CFStringRef transferFunctionString);
```

#### Return Value

The code point corresponding to the transfer function string, or `2` (unknown) if the string is [`nil`](../ObjectiveC/nil-227m0.md) or the system doesn’t recognize it.

## Parameters

- `transferFunctionString`: A Core Video transfer function string. See [Image Buffer Transfer Function Constants](./image-buffer-transfer-function-constants.md) for possible values.

## See Also

### Converting between strings and integer code points
- [func CVColorPrimariesGetIntegerCodePointForString(CFString?) -> Int32](./cvcolorprimariesgetintegercodepointforstring%28_%29.md)
  Returns the standard integer code point corresponding to the Core Video color primaries constant string that you specify.
- [func CVColorPrimariesGetStringForIntegerCodePoint(Int32) -> Unmanaged<CFString>?](./cvcolorprimariesgetstringforintegercodepoint%28_%29.md)
  Returns the Core Video color primaries string corresponding to the standard integer code point that you specify.
- [func CVTransferFunctionGetStringForIntegerCodePoint(Int32) -> Unmanaged<CFString>?](./cvtransferfunctiongetstringforintegercodepoint%28_%29.md)
  Returns the Core Video transfer function string corresponding to the standard integer code point that you specify.
- [func CVYCbCrMatrixGetIntegerCodePointForString(CFString?) -> Int32](./cvycbcrmatrixgetintegercodepointforstring%28_%29.md)
  Returns the standard integer code point corresponding to the Core Video YCbCr matrix string that you specify.
- [func CVYCbCrMatrixGetStringForIntegerCodePoint(Int32) -> Unmanaged<CFString>?](./cvycbcrmatrixgetstringforintegercodepoint%28_%29.md)
  Returns the Core Video YCbCr matrix string corresponding to the standard integer code point that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtransferfunctiongetintegercodepointforstring(_:))*