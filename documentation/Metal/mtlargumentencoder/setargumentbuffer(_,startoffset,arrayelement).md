# setArgumentBuffer(_:startOffset:arrayElement:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Specifies an array element within a buffer where the encoder writes argument data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setArgumentBuffer(_ argumentBuffer: (any MTLBuffer)?, startOffset: Int, arrayElement: Int)
```

```objc
- (void) setArgumentBuffer:(id<MTLBuffer>) argumentBuffer startOffset:(NSUInteger) startOffset arrayElement:(NSUInteger) arrayElement;
```

## Parameters

- `argumentBuffer`: The destination buffer that represents an argument buffer.
- `startOffset`: The starting byte offset of the buffer data.
- `arrayElement`: The desired element of the argument buffer array targeted by encoding.

## See Also

### Creating an argument buffer
- [func setArgumentBuffer((any MTLBuffer)?, offset: Int)](./setargumentbuffer%28_,offset%29.md)
  Specifies the position in a buffer where the encoder writes argument data.
- [var encodedLength: Int](./encodedlength.md)
  The number of bytes required to store the encoded resources of an argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setargumentbuffer(_:startoffset:arrayelement:))*