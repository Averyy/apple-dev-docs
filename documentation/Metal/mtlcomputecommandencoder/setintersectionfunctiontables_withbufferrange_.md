# setIntersectionFunctionTables:withBufferRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setIntersectionFunctionTables:(id<MTLIntersectionFunctionTable> const[]) intersectionFunctionTables withBufferRange:(NSRange) range;
```

#### Discussion

> ⚠️ **Warning**:  This method requires that the number of instances in `visibleFunctionTables` be the same as the length of `range`.

## Parameters

- `intersectionFunctionTables`: An array of [`MTLIntersectionFunctionTable`](../mtlintersectionfunctiontable.md) instances to bind.
- `range`: The argument buffer table indices to bind each of the `intersectionFunctionTables` to, in the order they appear.

## See Also

### Binding function tables
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./setvisiblefunctiontable%28_,bufferindex%29.md)
  Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [- setVisibleFunctionTables:withBufferRange:](./setvisiblefunctiontables_withbufferrange_.md)
  Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontables:withbufferrange:)*