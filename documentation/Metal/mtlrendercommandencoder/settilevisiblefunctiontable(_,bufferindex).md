# setTileVisibleFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assigns a visible function table to an entry in the tile shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setTileVisibleFunctionTable(_ functionTable: (any MTLVisibleFunctionTable)?, bufferIndex: Int)
```

```objc
- (void) setTileVisibleFunctionTable:(id<MTLVisibleFunctionTable>) functionTable atBufferIndex:(NSUInteger) bufferIndex;
```

#### Discussion

By default, the visible function table at each index is `nil`.

## Parameters

- `functionTable`: An [`MTLVisibleFunctionTable`](../mtlvisiblefunctiontable.md) instance the command assigns to an entry in the tile shader argument table for visible function tables.
- `bufferIndex`: An integer that represents the entry in the tile shader argument table for visible function tables that stores a record of `functionTable`.

## See Also

### Assigning visible function tables
- [func setTileVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](./settilevisiblefunctiontables%28_,bufferrange%29.md)
  Assigns multiple visible function tables to a range of entries in the tile shader argument table.
- [- setTileVisibleFunctionTables:withBufferRange:](./settilevisiblefunctiontables_withbufferrange_.md)
  Assigns multiple visible function tables to a range of entries in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilevisiblefunctiontable(_:bufferindex:))*