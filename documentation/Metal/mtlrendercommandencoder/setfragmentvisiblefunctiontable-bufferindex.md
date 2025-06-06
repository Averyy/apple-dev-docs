# setFragmentVisibleFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a visible function table to an entry in the fragment shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setFragmentVisibleFunctionTable(_ functionTable: (any MTLVisibleFunctionTable)?, bufferIndex: Int)
```

#### Discussion

By default, the visible function table at each index is `nil`.

## Parameters

- `functionTable`: An   instance the command assigns to an entry in the fragment shader argument table for visible function tables.
- `bufferIndex`: An integer that represents the entry in the fragment shader argument table for visible function tables that stores a record of  .

## See Also

- [func setFragmentVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/setfragmentvisiblefunctiontables(_:bufferrange:).md)
  Assigns multiple visible function tables to a range of entries in the fragment shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontable(_:bufferindex:))*