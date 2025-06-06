# setArgumentBuffer(_:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Specifies the position in a buffer where the encoder writes argument data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setArgumentBuffer(_ argumentBuffer: (any MTLBuffer)?, offset: Int)
```

## Parameters

- `argumentBuffer`: The destination buffer that represents an argument buffer.
- `offset`: The byte offset of the buffer.

## See Also

- [func setArgumentBuffer((any MTLBuffer)?, startOffset: Int, arrayElement: Int)](mtlargumentencoder/setargumentbuffer(_:startoffset:arrayelement:).md)
  Specifies an array element within a buffer where the encoder writes argument data.
- [var encodedLength: Int](mtlargumentencoder/encodedlength.md)
  The number of bytes required to store the encoded resources of an argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setargumentbuffer(_:offset:))*