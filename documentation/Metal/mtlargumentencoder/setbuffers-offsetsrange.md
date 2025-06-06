# setBuffers(_:offsets:range:)

**Framework**: Metal  
**Kind**: method

Encodes references to an array of buffers into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
func setBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

## Parameters

- `buffers`: An array of buffers the method encodes.
- `offsets`: An array of byte offsets for each element in  .
- `range`: A range of indices within the argument buffer for each element in  .   The values correspond to either the index IDs of declarations in   Metal Shading Language (MSL) or the   property   of   instances.

## See Also

- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlargumentencoder/setbuffer(_:offset:index:).md)
  Encodes a reference to a buffer into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setbuffers(_:offsets:range:))*