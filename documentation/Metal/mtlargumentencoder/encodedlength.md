# encodedLength

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The number of bytes required to store the encoded resources of an argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var encodedLength: Int { get }
```

#### Discussion

After creating an [`MTLArgumentEncoder`](mtlargumentencoder.md) instance, use this value to create the [`MTLBuffer`](mtlbuffer.md) instance that represents an argument buffer.

```swift
id <MTLArgumentEncoder> encoder = [_function newArgumentEncoderWithBufferIndex:0];
id <MTLBuffer> buffer = [_device newBufferWithLength:encoder.encodedLength options:_options];
[encoder setArgumentBuffer:buffer offset:0];
```

## See Also

- [func setArgumentBuffer((any MTLBuffer)?, offset: Int)](mtlargumentencoder/setargumentbuffer(_:offset:).md)
  Specifies the position in a buffer where the encoder writes argument data.
- [func setArgumentBuffer((any MTLBuffer)?, startOffset: Int, arrayElement: Int)](mtlargumentencoder/setargumentbuffer(_:startoffset:arrayelement:).md)
  Specifies an array element within a buffer where the encoder writes argument data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/encodedlength)*