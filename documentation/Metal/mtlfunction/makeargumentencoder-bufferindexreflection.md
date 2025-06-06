# makeArgumentEncoder(bufferIndex:reflection:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates an argument encoder and returns reflection information for an argument buffer that’s one of this function’s arguments

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func makeArgumentEncoder(bufferIndex: Int, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedArgument?>?) -> any MTLArgumentEncoder
```

#### Discussion

Resources encoded into an argument buffer by the [`MTLArgumentEncoder`](mtlargumentencoder.md) object must match the structure of the argument buffer located at the function’s specified buffer index.

## Parameters

- `bufferIndex`: The index of an argument buffer in the function’s argument list. This method fails if the specified index doesn’t correspond to an argument buffer.
- `reflection`: A pointer that Metal populates with the function reflection data in the argument buffer at  .

## See Also

- [func makeArgumentEncoder(bufferIndex: Int) -> any MTLArgumentEncoder](mtlfunction/makeargumentencoder(bufferindex:).md)
  Creates an argument encoder for an argument buffer that’s one of this function’s arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/makeargumentencoder(bufferindex:reflection:))*