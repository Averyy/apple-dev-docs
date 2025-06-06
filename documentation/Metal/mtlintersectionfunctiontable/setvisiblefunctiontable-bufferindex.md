# setVisibleFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
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

## Parameters

- `functionTable`: A visible function table.
- `bufferIndex`: An index in the function table’s buffer argument table.

## See Also

- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlintersectionfunctiontable/setbuffer(_:offset:index:).md)
  Sets a buffer for the intersection functions.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlintersectionfunctiontable/setbuffers(_:offsets:range:).md)
  Sets a range of buffers for the intersection functions.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlintersectionfunctiontable/setvisiblefunctiontables(_:bufferrange:).md)
  Sets a range of visible function tables for the intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontable(_:bufferindex:))*