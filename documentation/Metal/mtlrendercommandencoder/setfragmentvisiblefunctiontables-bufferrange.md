# setFragmentVisibleFunctionTables(_:bufferRange:)

**Framework**: Metal  
**Kind**: method

Assigns multiple visible function tables to a range of entries in the fragment shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setFragmentVisibleFunctionTables(_ functionTables: [(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)
```

#### Discussion

By default, the visible function table at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setFragmentVisibleFunctionTables:withBufferRange:`](mtlrendercommandencoder/setfragmentvisiblefunctiontables:withbufferrange:.md).

 The Objective-C version of this method is [`setFragmentVisibleFunctionTables:withBufferRange:`](mtlrendercommandencoder/setfragmentvisiblefunctiontables:withbufferrange:.md).

## Parameters

- `functionTables`: An array of   instances the command assigns to entries in the fragment shader argument table for visible function tables.
- `bufferRange`: A span of integers that represent the entries in the fragment shader argument table for visible function tables. Each entry stores a record of the corresponding element in  .

## See Also

- [func setFragmentVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/setfragmentvisiblefunctiontable(_:bufferindex:).md)
  Assigns a visible function table to an entry in the fragment shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontables(_:bufferrange:))*