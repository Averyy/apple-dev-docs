# setBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setBuffer:(id<MTLBuffer>) buffer offset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

## Parameters

- `buffer`: The [`MTLBuffer`](../mtlbuffer.md) object to set in the argument table.
- `offset`: Where the data begins, in bytes, from the start of the buffer.
- `index`: An index in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setbuffers%28_,offsets,range%29.md)
  Sets a range of buffers for the intersection functions.
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./setvisiblefunctiontable%28_,bufferindex%29.md)
  Sets a visible function table for the intersection functions.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](./setvisiblefunctiontables%28_,bufferrange%29.md)
  Sets a range of visible function tables for the intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setbuffer(_:offset:index:))*