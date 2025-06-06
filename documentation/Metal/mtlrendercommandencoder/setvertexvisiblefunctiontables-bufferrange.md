# setVertexVisibleFunctionTables(_:bufferRange:)

**Framework**: Metal  
**Kind**: method

Assigns multiple visible function tables to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setVertexVisibleFunctionTables(_ functionTables: [(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)
```

#### Discussion

By default, the visible function table at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setVertexVisibleFunctionTables:withBufferRange:`](mtlrendercommandencoder/setvertexvisiblefunctiontables:withbufferrange:.md).

## Parameters

- `functionTables`: An array of   instances the command assigns to entries in the vertex shader argument table for visible function tables.
- `bufferRange`: A span of integers that represent the entries in the vertex shader argument table for visible function tables. Each entry stores a record of the corresponding element in  .

## See Also

- [func setVertexVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/setvertexvisiblefunctiontable(_:bufferindex:).md)
  Assigns a visible function table to an entry in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexvisiblefunctiontables(_:bufferrange:))*