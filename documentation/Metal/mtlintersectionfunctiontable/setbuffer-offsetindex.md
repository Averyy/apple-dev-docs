# setBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets a buffer for the intersection functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Parameters

- `buffer`: The   object to set in the argument table.
- `offset`: Where the data begins, in bytes, from the start of the buffer.
- `index`: An index in the function table’s buffer argument table.

## See Also

- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlintersectionfunctiontable/setbuffers(_:offsets:range:).md)
  Sets a range of buffers for the intersection functions.
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlintersectionfunctiontable/setvisiblefunctiontable(_:bufferindex:).md)
  Sets a visible function table for the intersection functions.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlintersectionfunctiontable/setvisiblefunctiontables(_:bufferrange:).md)
  Sets a range of visible function tables for the intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setbuffer(_:offset:index:))*