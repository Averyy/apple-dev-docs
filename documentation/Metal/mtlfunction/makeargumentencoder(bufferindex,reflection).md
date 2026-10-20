# makeArgumentEncoder(bufferIndex:reflection:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates an argument encoder and returns reflection information for an argument buffer that’s one of this function’s arguments

**Availability**:
- iOS 11.0+ - Deprecated in 16.0
- iPadOS 11.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.13+ - Deprecated in 13.0
- tvOS 11.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`makeArgumentEncoder(bufferBinding:)`](../mtldevice/makeargumentencoder%28bufferbinding%29.md) method of an [`MTLDevice`](../mtldevice.md) instance.

## Declaration

```swift
func makeArgumentEncoder(bufferIndex: Int, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedArgument?>?) -> any MTLArgumentEncoder
```

```objc
- (id<MTLArgumentEncoder>) newArgumentEncoderWithBufferIndex:(NSUInteger) bufferIndex reflection:(MTLAutoreleasedArgument*) reflection;
```

#### Discussion

Resources encoded into an argument buffer by the [`MTLArgumentEncoder`](../mtlargumentencoder.md) object need to match the structure of the argument buffer located at the function’s specified buffer index.

## Parameters

- `bufferIndex`: The index of an argument buffer in the function’s argument list. This method fails if the specified index doesn’t correspond to an argument buffer.
- `reflection`: A pointer that Metal populates with the function reflection data in the argument buffer at `bufferIndex`.

## See Also

### Creating argument encoders
- [func makeArgumentEncoder(bufferIndex: Int) -> any MTLArgumentEncoder](./makeargumentencoder%28bufferindex%29.md)
  Creates an argument encoder for an argument buffer that’s one of this function’s arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/makeargumentencoder(bufferindex:reflection:))*