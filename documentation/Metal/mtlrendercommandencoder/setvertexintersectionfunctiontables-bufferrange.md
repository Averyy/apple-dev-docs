# setVertexIntersectionFunctionTables(_:bufferRange:)

**Framework**: Metal  
**Kind**: method

Assigns multiple intersection function tables to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setVertexIntersectionFunctionTables(_ functionTables: [(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)
```

#### Discussion

By default, the intersection function table at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setVertexIntersectionFunctionTables:withBufferRange:`](mtlrendercommandencoder/setvertexintersectionfunctiontables:withbufferrange:.md).

 The Objective-C version of this method is [`setVertexIntersectionFunctionTables:withBufferRange:`](mtlrendercommandencoder/setvertexintersectionfunctiontables:withbufferrange:.md).

## Parameters

- `functionTables`: An array of   instances the command assigns to entries in the vertex shader argument table for intersection function tables.
- `bufferRange`: A span of integers that represent the entries in the vertex shader argument table for intersection function tables. Each entry stores a record of the corresponding element in  .

## See Also

- [func setVertexIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/setvertexintersectionfunctiontable(_:bufferindex:).md)
  Assigns an intersection function table to an entry in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexintersectionfunctiontables(_:bufferrange:))*