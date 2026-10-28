# canImportFileExtension(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the [`MDLAsset`](../mdlasset.md) class can read asset data from files with the specified extension.

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

```objc
+ (BOOL) canImportFileExtension:(NSString *) extension;
```

## Return Value

[`true`](../../Swift/true.md) if the [`MDLAsset`](../mdlasset.md) class can read asset data from files with the specified extension; otherwise, [`false`](../../Swift/false.md).

## Discussion

If this method returns [`true`](../../Swift/true.md), you can use the [`init(url:)`](./init%28url%29-1f4ym.md) or [`init(url:vertexDescriptor:bufferAllocator:)`](./init%28url,vertexdescriptor,bufferallocator%29-1tchi.md) initializer to import an asset with the specified filename extension.

The set of supported extensions and formats includes:

- **`.abc`**: Alembic
- **`.usd`, `.usda`, `.usdc`**: Universal Scene Description
- **`.usdz`**: Universal Scene Description (Mobile)
- **`.ply`**: Polygon
- **`.obj`**: Wavefront Object
- **`.stl`**: Standard Tessellation Language

Additional formats may be supported as well.

## Parameters

- `extension`: The filename extension identifying an asset file format.

## See Also

### Creating an Asset
- [init(url: URL)](./init%28url%29-1f4ym.md)
  Initializes an asset from the file at the specified URL.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](./init%28bufferallocator%29.md)
  Initializes an empty asset, using the specified buffer allocator.
- [init(url: URL?, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?)](./init%28url,vertexdescriptor,bufferallocator%29-1tchi.md)
  Initializes an asset from the file at the specified URL, using the specified vertex descriptor and buffer allocator.
- [init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?, preserveTopology: Bool, error: NSErrorPointer)](./init%28url,vertexdescriptor,bufferallocator,preservetopology,error%29-510xi.md)
  Initializes an asset from the file at the specified URL, using the specified options for allocating and transforming data during import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/canimportfileextension(_:))*