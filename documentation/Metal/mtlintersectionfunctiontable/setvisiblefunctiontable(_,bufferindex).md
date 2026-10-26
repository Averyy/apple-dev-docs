# setVisibleFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets a visible function table for the intersection functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setVisibleFunctionTable(_ functionTable: (any MTLVisibleFunctionTable)?, bufferIndex: Int)
```

```objc
- (void) setVisibleFunctionTable:(id<MTLVisibleFunctionTable>) functionTable atBufferIndex:(NSUInteger) bufferIndex;
```

## Parameters

- `functionTable`: A visible function table.
- `bufferIndex`: An index in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setbuffer%28_,offset,index%29.md)
  Sets a buffer for the intersection functions.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setbuffers%28_,offsets,range%29.md)
  Sets a range of buffers for the intersection functions.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](./setvisiblefunctiontables%28_,bufferrange%29.md)
  Sets a range of visible function tables for the intersection functions.
- [- setBuffers:offsets:withRange:](./setbuffers_offsets_withrange_.md)
  Sets a range of buffers for the intersection functions.
- [- setVisibleFunctionTables:withBufferRange:](./setvisiblefunctiontables_withbufferrange_.md)
  Sets a range of visible function tables for the intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontable(_:bufferindex:))*