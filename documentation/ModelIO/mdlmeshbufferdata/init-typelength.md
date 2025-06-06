# init(type:length:)

**Framework**: Model I/O  
**Kind**: init

Initializes a buffer of the specified length.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(type: MDLMeshBufferType, length: Int)
```

#### Return Value

A new memory buffer for mesh data.

#### Discussion

All bytes in the newly created buffer are zero.

## Parameters

- `type`:   to create a buffer for a mesh’s vertex attribute data, or   to create a buffer for a submesh’s index data.
- `length`: The size, in bytes, of the buffer to create.

## See Also

- [init(type: MDLMeshBufferType, data: Data?)](mdlmeshbufferdata/init(type:data:).md)
  Initializes a buffer containing the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferdata/init(type:length:))*