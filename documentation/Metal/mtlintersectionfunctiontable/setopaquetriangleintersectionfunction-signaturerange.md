# setOpaqueTriangleIntersectionFunction(signature:range:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets a range of entries in the intersection table to point to a system-defined opaque triangle intersection function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, range: NSRange)
```

## Parameters

- `signature`: The signature of the function.
- `range`: A range of indices to change in the table.

## See Also

- [func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, index: Int)](mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:index:).md)
  Sets an entry in the intersection table to point to a system-defined opaque triangle intersection function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:range:))*