# setVisibleFunctionTables(_:bufferRange:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets a range of visible function tables for the intersection functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
func setVisibleFunctionTables(_ functionTables: [(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)
```

## Parameters

- `functionTables`: The function tables to insert.
- `bufferRange`: A range of indices in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setbuffer%28_,offset,index%29.md)
  Sets a buffer for the intersection functions.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setbuffers%28_,offsets,range%29.md)
  Sets a range of buffers for the intersection functions.
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./setvisiblefunctiontable%28_,bufferindex%29.md)
  Sets a visible function table for the intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontables(_:bufferrange:))*