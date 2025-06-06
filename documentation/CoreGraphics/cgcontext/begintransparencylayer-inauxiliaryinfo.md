# beginTransparencyLayer(in:auxiliaryInfo:)

**Framework**: Core Graphics  
**Kind**: method

Begins a transparency layer whose contents are bounded by the specified rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func beginTransparencyLayer(in rect: CGRect, auxiliaryInfo auxInfo: CFDictionary?)
```

#### Discussion

This function is identical to [`beginTransparencyLayer(auxiliaryInfo:)`](cgcontext/begintransparencylayer(auxiliaryinfo:).md) except that the content of the transparency layer is within the bounds of the provided rectangle.

## Parameters

- `rect`: The rectangle, specified in user space, that bounds the transparency layer.
- `auxInfo`: A dictionary that specifies any additional information, or  .

## See Also

- [func beginTransparencyLayer(auxiliaryInfo: CFDictionary?)](cgcontext/begintransparencylayer(auxiliaryinfo:).md)
  Begins a transparency layer.
- [func endTransparencyLayer()](cgcontext/endtransparencylayer.md)
  Ends a transparency layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/begintransparencylayer(in:auxiliaryinfo:))*