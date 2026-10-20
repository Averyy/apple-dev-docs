# setBuffers(_:offsets:range:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets a range of buffers for the intersection functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
func setBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

## Parameters

- `buffers`: An array of buffers to insert into the table.
- `offsets`: An array of offsets to insert into the table.
- `range`: A range of indices in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setbuffer%28_,offset,index%29.md)
  Sets a buffer for the intersection functions.
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./setvisiblefunctiontable%28_,bufferindex%29.md)
  Sets a visible function table for the intersection functions.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](./setvisiblefunctiontables%28_,bufferrange%29.md)
  Sets a range of visible function tables for the intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setbuffers(_:offsets:range:))*