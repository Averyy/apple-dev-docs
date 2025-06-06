# init(url:vertexDescriptor:bufferAllocator:)

**Framework**: Model I/O  
**Kind**: init

Initializes an asset from the file at the specified URL, using the specified vertex descriptor and buffer allocator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(url URL: URL?, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?)
```

#### Return Value

A new asset object.

#### Discussion

Using this initializer is equivalent to using the [`init(url:vertexDescriptor:bufferAllocator:preserveTopology:error:)`](mdlasset/init(url:vertexdescriptor:bufferallocator:preservetopology:error:).md) initializer, passing [`false`](https://developer.apple.com/documentation/swift/false) for the `preserveTopology` parameter and ignoring errors.

## Parameters

- `URL`: A URL specifying the location an asset file.
- `vertexDescriptor`: An object describing the vertex data format to be loaded from the asset, or   to use the asset’s vertex buffers as found in the file.
- `bufferAllocator`: The allocator object to use for loading mesh data from the asset, or   to use a default allocator.

## See Also

- [class func canImportFileExtension(String) -> Bool](mdlasset/canimportfileextension(_:).md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](mdlasset.md) class can read asset data from files with the specified extension.
- [init(url: URL)](mdlasset/init(url:).md)
  Initializes an asset from the file at the specified URL.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlasset/init(bufferallocator:).md)
  Initializes an empty asset, using the specified buffer allocator.
- [init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?, preserveTopology: Bool, error: NSErrorPointer)](mdlasset/init(url:vertexdescriptor:bufferallocator:preservetopology:error:).md)
  Initializes an asset from the file at the specified URL, using the specified options for allocating and transforming data during import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/init(url:vertexdescriptor:bufferallocator:))*