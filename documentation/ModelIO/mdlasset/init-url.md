# init(url:)

**Framework**: Model I/O  
**Kind**: init

Initializes an asset from the file at the specified URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(url URL: URL)
```

#### Return Value

A new asset object.

#### Discussion

Use the [`canImportFileExtension(_:)`](mdlasset/canimportfileextension(_:).md) method to determine whether Model I/O  can import an asset.

## Parameters

- `URL`: A URL specifying the location an asset file.

## See Also

- [class func canImportFileExtension(String) -> Bool](mdlasset/canimportfileextension(_:).md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](mdlasset.md) class can read asset data from files with the specified extension.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlasset/init(bufferallocator:).md)
  Initializes an empty asset, using the specified buffer allocator.
- [init(url: URL?, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlasset/init(url:vertexdescriptor:bufferallocator:).md)
  Initializes an asset from the file at the specified URL, using the specified vertex descriptor and buffer allocator.
- [init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?, preserveTopology: Bool, error: NSErrorPointer)](mdlasset/init(url:vertexdescriptor:bufferallocator:preservetopology:error:).md)
  Initializes an asset from the file at the specified URL, using the specified options for allocating and transforming data during import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/init(url:))*