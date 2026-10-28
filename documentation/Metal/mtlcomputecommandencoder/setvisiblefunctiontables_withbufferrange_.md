# setVisibleFunctionTables:withBufferRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setVisibleFunctionTables:(id<MTLVisibleFunctionTable> const[]) visibleFunctionTables withBufferRange:(NSRange) range;
```

## Discussion

> ⚠️ **Warning**:  This method requires that the number of instances in `visibleFunctionTables` be the same as the length of `range`.

## Parameters

- `visibleFunctionTables`: An array of [`MTLVisibleFunctionTable`](../mtlvisiblefunctiontable.md) instances to bind.
- `range`: The buffer argument table indices to bind each of the `visibleFunctionTables` to, in the order they appear.

## See Also

### Binding function tables
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./setvisiblefunctiontable%28_,bufferindex%29.md)
  Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [- setIntersectionFunctionTables:withBufferRange:](./setintersectionfunctiontables_withbufferrange_.md)
  Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontables:withbufferrange:)*