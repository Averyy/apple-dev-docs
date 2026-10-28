# init(url:vertexDescriptor:bufferAllocator:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithURL:(NSURL *) URL vertexDescriptor:(MDLVertexDescriptor *) vertexDescriptor bufferAllocator:(id<MDLMeshBufferAllocator>) bufferAllocator;
```

## Return Value

A new asset object.

## Discussion

Using this initializer is equivalent to using the [`init(url:vertexDescriptor:bufferAllocator:preserveTopology:error:)`](./init%28url,vertexdescriptor,bufferallocator,preservetopology,error%29-510xi.md) initializer, passing [`false`](../../Swift/false.md) for the `preserveTopology` parameter and ignoring errors.

## Parameters

- `URL`: A URL specifying the location an asset file.
- `vertexDescriptor`: An object describing the vertex data format to be loaded from the asset, or `nil` to use the asset’s vertex buffers as found in the file.
- `bufferAllocator`: The allocator object to use for loading mesh data from the asset, or `nil` to use a default allocator.

## See Also

### Creating an Asset
- [class func canImportFileExtension(String) -> Bool](./canimportfileextension%28_%29.md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](../mdlasset.md) class can read asset data from files with the specified extension.
- [init(url: URL)](./init%28url%29-1f4ym.md)
  Initializes an asset from the file at the specified URL.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](./init%28bufferallocator%29.md)
  Initializes an empty asset, using the specified buffer allocator.
- [init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?, preserveTopology: Bool, error: NSErrorPointer)](./init%28url,vertexdescriptor,bufferallocator,preservetopology,error%29-510xi.md)
  Initializes an asset from the file at the specified URL, using the specified options for allocating and transforming data during import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/init(url:vertexdescriptor:bufferallocator:)-1tchi)*