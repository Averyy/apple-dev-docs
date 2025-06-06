# setTileIntersectionFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns an intersection function table to an entry in the tile shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setTileIntersectionFunctionTable(_ intersectionFunctionTable: (any MTLIntersectionFunctionTable)?, bufferIndex: Int)
```

#### Discussion

By default, the intersection function table at each index is `nil`.

## Parameters

- `intersectionFunctionTable`: An   instance the command assigns to an entry in the tile shader argument table for intersection function tables.
- `bufferIndex`: An integer that represents the entry in the tile shader argument table for intersection function tables that stores a record of  .

## See Also

- [func setTileIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/settileintersectionfunctiontables(_:bufferrange:).md)
  Assigns multiple intersection function tables to a range of entries in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settileintersectionfunctiontable(_:bufferindex:))*