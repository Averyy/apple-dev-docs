# setIntersectionFunctionTables:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setIntersectionFunctionTables:(id<MTLIntersectionFunctionTable> const[]) intersectionFunctionTables withRange:(NSRange) range;
```

## Parameters

- `intersectionFunctionTables`: An array of intersection-function tables the method encodes.
- `range`: A range of indices within the argument buffer for each element in `intersectionFunctionTables`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [`index`](../mtlargumentdescriptor/index.md) property of [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding function tables
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, index: Int)](./setvisiblefunctiontable%28_,index%29.md)
  Encodes a reference to a visible-function table into the argument buffer.
- [- setVisibleFunctionTables:withRange:](./setvisiblefunctiontables_withrange_.md)
  Encodes references to an array of visible function tables into the argument buffer.
- [func setIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, index: Int)](./setintersectionfunctiontable%28_,index%29.md)
  Encodes a reference to a ray-tracing intersection-function table into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setintersectionfunctiontables:withrange:)*