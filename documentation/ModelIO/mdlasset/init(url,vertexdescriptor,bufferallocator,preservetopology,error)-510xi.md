# init(url:vertexDescriptor:bufferAllocator:preserveTopology:error:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

Initializes an asset from the file at the specified URL, using the specified options for allocating and transforming data during import.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(url URL: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?, preserveTopology: Bool, error: NSErrorPointer)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL vertexDescriptor:(MDLVertexDescriptor *) vertexDescriptor bufferAllocator:(id<MDLMeshBufferAllocator>) bufferAllocator preserveTopology:(BOOL) preserveTopology error:(NSError **) error;
```

## Return Value

A new asset object.

## Discussion

Use this initializer when you need to ensure that mesh data from the asset is allocated and formatted correctly for your intended use. For example, to use the MetalKit framework for loading vertex data into GPU buffers for rendering using Metal, pass a [`MTKMeshBufferAllocator`](../../MetalKit/mtkmeshbufferallocator.md) object for the `bufferAllocator` parameter. If you specify a [`MDLVertexDescriptor`](../mdlvertexdescriptor.md) object for the `vertexDescriptor` parameter, Model I/O automatically transforms mesh data to the specified vertex format upon loading. If you specify [`false`](../../Swift/false.md) for the `preserveTopology` parameter, Model I/O automatically transforms submesh data to create triangle meshes (the optimal format for rendering on most GPUs). By using these parameters, you ensure that mesh data is copied and transformed a minimal number of times between being read from a file and being loaded into GPU memory for rendering.

Use the [`canImportFileExtension(_:)`](./canimportfileextension%28_%29.md) method to determine whether Model I/O  can import an asset.

## Parameters

- `URL`: A URL specifying the location an asset file.
- `vertexDescriptor`: An object describing the vertex data format to be loaded from the asset, or `nil` to use the asset’s vertex buffers as found in the file.
- `bufferAllocator`: The allocator object to use for loading mesh data from the asset, or `nil` to use a default allocator.
- `preserveTopology`: If [`true`](../../Swift/true.md), Model I/O uses the asset’s submesh index buffers as found in the file, using the appropriate [`MDLGeometryType`](../mdlgeometrytype.md) value for each submesh and generating [`MDLSubmeshTopology`](../mdlsubmeshtopology.md) buffers as needed for variable-topology submeshes. If [`false`](../../Swift/false.md), Model I/O reformats index buffers to create triangle submeshes.
- `error`: Upon return, an object describing any errors that occur while loading the asset.

## See Also

### Creating an Asset
- [class func canImportFileExtension(String) -> Bool](./canimportfileextension%28_%29.md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](../mdlasset.md) class can read asset data from files with the specified extension.
- [init(url: URL)](./init%28url%29-1f4ym.md)
  Initializes an asset from the file at the specified URL.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](./init%28bufferallocator%29.md)
  Initializes an empty asset, using the specified buffer allocator.
- [init(url: URL?, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?)](./init%28url,vertexdescriptor,bufferallocator%29-1tchi.md)
  Initializes an asset from the file at the specified URL, using the specified vertex descriptor and buffer allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/init(url:vertexdescriptor:bufferallocator:preservetopology:error:)-510xi)*