# setVertexIntersectionFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assigns an intersection function table to an entry in the vertex shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setVertexIntersectionFunctionTable(_ intersectionFunctionTable: (any MTLIntersectionFunctionTable)?, bufferIndex: Int)
```

```objc
- (void) setVertexIntersectionFunctionTable:(id<MTLIntersectionFunctionTable>) intersectionFunctionTable atBufferIndex:(NSUInteger) bufferIndex;
```

#### Discussion

By default, the intersection function table at each index is `nil`.

## Parameters

- `intersectionFunctionTable`: An [`MTLIntersectionFunctionTable`](../mtlintersectionfunctiontable.md) instance the command assigns to an entry in the vertex shader argument table for intersection function tables.
- `bufferIndex`: An integer that represents the entry in the vertex shader argument table for intersection function tables that stores a record of `intersectionFunctionTable`.

## See Also

### Assigning intersection function tables
- [func setVertexIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](./setvertexintersectionfunctiontables%28_,bufferrange%29.md)
  Assigns multiple intersection function tables to a range of entries in the vertex shader argument table.
- [- setVertexIntersectionFunctionTables:withBufferRange:](./setvertexintersectionfunctiontables_withbufferrange_.md)
  Assigns multiple intersection function tables to a range of entries in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexintersectionfunctiontable(_:bufferindex:))*