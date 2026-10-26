# setFragmentIntersectionFunctionTables:withBufferRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple intersection function tables to a range of entries in the fragment shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setFragmentIntersectionFunctionTables:(id<MTLIntersectionFunctionTable> const[]) intersectionFunctionTables withBufferRange:(NSRange) range;
```

#### Discussion

By default, the intersection function table at each index is `nil`.

> **Note**:  The Swift version of this method is [`setFragmentIntersectionFunctionTables(_:bufferRange:)`](./setfragmentintersectionfunctiontables%28_,bufferrange%29.md).

## Parameters

- `intersectionFunctionTables`: A pointer to a C array of [`MTLIntersectionFunctionTable`](../mtlintersectionfunctiontable.md) instances the command assigns to entries in the fragment shader argument table for intersection function tables.
- `range`: A span of integers that represent the entries in the fragment shader argument table for intersection function tables. Each entry stores a record of the corresponding element in `intersectionFunctionTables`.

## See Also

### Assigning intersection function tables
- [func setFragmentIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](./setfragmentintersectionfunctiontable%28_,bufferindex%29.md)
  Assigns an intersection function table to an entry in the fragment shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentintersectionfunctiontables:withbufferrange:)*