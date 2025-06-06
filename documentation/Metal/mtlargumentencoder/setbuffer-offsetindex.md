# setBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a reference to a buffer into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Parameters

- `buffer`: A buffer the method encodes.
- `offset`: A byte offset for  .
- `index`: The index of a buffer within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.

## See Also

- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlargumentencoder/setbuffers(_:offsets:range:).md)
  Encodes references to an array of buffers into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setbuffer(_:offset:index:))*