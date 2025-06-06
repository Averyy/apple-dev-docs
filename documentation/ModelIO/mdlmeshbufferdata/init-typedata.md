# init(type:data:)

**Framework**: Model I/O  
**Kind**: init

Initializes a buffer containing the specified data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(type: MDLMeshBufferType, data: Data?)
```

#### Return Value

A new memory buffer for mesh data.

## Parameters

- `type`:   to create a buffer for a mesh’s vertex attribute data, or   to create a buffer for a submesh’s index data.
- `data`: The initial data to copy into the buffer.

## See Also

- [init(type: MDLMeshBufferType, length: Int)](mdlmeshbufferdata/init(type:length:).md)
  Initializes a buffer of the specified length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferdata/init(type:data:))*