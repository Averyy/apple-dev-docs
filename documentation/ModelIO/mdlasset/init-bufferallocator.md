# init(bufferAllocator:)

**Framework**: Model I/O  
**Kind**: init

Initializes an empty asset, using the specified buffer allocator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(bufferAllocator: (any MDLMeshBufferAllocator)?)
```

#### Return Value

A new asset object.

#### Discussion

Use this initializer when you want to programmatically populate an asset with content (for example, for use in exporting to a file) while controlling the allocation of mesh data buffers associated with the asset. For example, to use the MetalKit framework for loading vertex data into GPU buffers for rendering using Metal, pass a [`MTKMeshBufferAllocator`](https://developer.apple.com/documentation/MetalKit/MTKMeshBufferAllocator) object for the `bufferAllocator` parameter.

## Parameters

- `bufferAllocator`: The allocator object to use for loading or creating mesh data associated with the asset, or   to use a default allocator.

## See Also

- [class func canImportFileExtension(String) -> Bool](mdlasset/canimportfileextension(_:).md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](mdlasset.md) class can read asset data from files with the specified extension.
- [init(url: URL)](mdlasset/init(url:).md)
  Initializes an asset from the file at the specified URL.
- [init(url: URL?, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlasset/init(url:vertexdescriptor:bufferallocator:).md)
  Initializes an asset from the file at the specified URL, using the specified vertex descriptor and buffer allocator.
- [init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?, preserveTopology: Bool, error: NSErrorPointer)](mdlasset/init(url:vertexdescriptor:bufferallocator:preservetopology:error:).md)
  Initializes an asset from the file at the specified URL, using the specified options for allocating and transforming data during import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/init(bufferallocator:))*