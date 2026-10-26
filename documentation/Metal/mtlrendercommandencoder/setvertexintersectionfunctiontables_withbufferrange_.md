# setVertexIntersectionFunctionTables:withBufferRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple intersection function tables to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setVertexIntersectionFunctionTables:(id<MTLIntersectionFunctionTable> const[]) intersectionFunctionTables withBufferRange:(NSRange) range;
```

#### Discussion

By default, the intersection function table at each index is `nil`.

> **Note**:  The Swift version of this method is [`setVertexIntersectionFunctionTables(_:bufferRange:)`](./setvertexintersectionfunctiontables%28_,bufferrange%29.md).

## Parameters

- `intersectionFunctionTables`: A pointer to a C array of [`MTLIntersectionFunctionTable`](../mtlintersectionfunctiontable.md) instances the command assigns to entries in the vertex shader argument table for intersection function tables.
- `range`: A span of integers that represent the entries in the vertex shader argument table for intersection function tables. Each entry stores a record of the corresponding element in `intersectionFunctionTables`.

## See Also

### Assigning intersection function tables
- [func setVertexIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](./setvertexintersectionfunctiontable%28_,bufferindex%29.md)
  Assigns an intersection function table to an entry in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexintersectionfunctiontables:withbufferrange:)*