# setTileVisibleFunctionTables(_:bufferRange:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple visible function tables to a range of entries in the tile shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
func setTileVisibleFunctionTables(_ functionTables: [(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)
```

## Discussion

By default, the visible function table at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setTileVisibleFunctionTables:withBufferRange:`](./settilevisiblefunctiontables_withbufferrange_.md).

## Parameters

- `functionTables`: An array of [`MTLVisibleFunctionTable`](../mtlvisiblefunctiontable.md) instances the command assigns to entries in the tile shader argument table for visible function tables.
- `bufferRange`: A span of integers that represent the entries in the tile shader argument table for visible function tables. Each entry stores a record of the corresponding element in `functionTables`.

## See Also

### Assigning visible function tables
- [func setTileVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./settilevisiblefunctiontable%28_,bufferindex%29.md)
  Assigns a visible function table to an entry in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilevisiblefunctiontables(_:bufferrange:))*