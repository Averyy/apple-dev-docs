# setOpaqueTriangleIntersectionFunction(signature:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets an entry in the intersection table to point to a system-defined opaque triangle intersection function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, index: Int)
```

```objc
- (void) setOpaqueTriangleIntersectionFunctionWithSignature:(MTLIntersectionFunctionSignature) signature atIndex:(NSUInteger) index;
```

## Parameters

- `signature`: The signature of the function.
- `index`: The index in the table to change.

## See Also

### Specifying opaque triangle intersection testing
- [func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, range: NSRange)](./setopaquetriangleintersectionfunction%28signature,range%29.md)
  Sets a range of entries in the intersection table to point to a system-defined opaque triangle intersection function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:index:))*