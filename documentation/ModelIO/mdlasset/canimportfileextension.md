# canImportFileExtension(_:)

**Framework**: Model I/O  
**Kind**: method

Returns a Boolean value that indicates whether the [`MDLAsset`](mdlasset.md) class can read asset data from files with the specified extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func canImportFileExtension(_ extension: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the [`MDLAsset`](mdlasset.md) class can read asset data from files with the specified extension; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If this method returns [`true`](https://developer.apple.com/documentation/swift/true), you can use the [`init(url:)`](mdlasset/init(url:).md) or [`init(url:vertexDescriptor:bufferAllocator:)`](mdlasset/init(url:vertexdescriptor:bufferallocator:).md) initializer to import an asset with the specified filename extension.

The set of supported extensions and formats includes:

Additional formats may be supported as well.

## Parameters

- `extension`: The filename extension identifying an asset file format.

## See Also

- [init(url: URL)](mdlasset/init(url:).md)
  Initializes an asset from the file at the specified URL.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlasset/init(bufferallocator:).md)
  Initializes an empty asset, using the specified buffer allocator.
- [init(url: URL?, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlasset/init(url:vertexdescriptor:bufferallocator:).md)
  Initializes an asset from the file at the specified URL, using the specified vertex descriptor and buffer allocator.
- [init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?, preserveTopology: Bool, error: NSErrorPointer)](mdlasset/init(url:vertexdescriptor:bufferallocator:preservetopology:error:).md)
  Initializes an asset from the file at the specified URL, using the specified options for allocating and transforming data during import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/canimportfileextension(_:))*