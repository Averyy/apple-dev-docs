# setFragmentIntersectionFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns an intersection function table to an entry in the fragment shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setFragmentIntersectionFunctionTable(_ intersectionFunctionTable: (any MTLIntersectionFunctionTable)?, bufferIndex: Int)
```

#### Discussion

By default, the intersection function table at each index is `nil`.

## Parameters

- `intersectionFunctionTable`: An   instance the command assigns to an entry in the fragment shader argument table for intersection function tables.
- `bufferIndex`: An integer that represents the entry in the fragment shader argument table for intersection function tables that stores a record of  .

## See Also

- [func setFragmentIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/setfragmentintersectionfunctiontables(_:bufferrange:).md)
  Assigns multiple intersection function tables to a range of entries in the fragment shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentintersectionfunctiontable(_:bufferindex:))*