# makeIOFileHandle(url:compressionMethod:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates an input/output file handle instance that represents a compressed file at a URL.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func makeIOFileHandle(url: URL, compressionMethod: MTLIOCompressionMethod) throws -> any MTLIOFileHandle
```

```objc
- (id<MTLIOFileHandle>) newIOFileHandleWithURL:(NSURL *) url compressionMethod:(MTLIOCompressionMethod) compressionMethod error:(NSError **) error;
```

#### Return Value

A new [`MTLIOFileHandle`](../mtliofilehandle.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

#### Discussion

For information about using input/output command queues and file handles, see [Resource loading](../resource-loading.md).

## Parameters

- `url`: A location URL to a compressed file in the file system.
- `compressionMethod`: The file’s compression format.

## See Also

### Creating I/O file handles
- [func makeIOFileHandle(url: URL) throws -> any MTLIOFileHandle](./makeiofilehandle%28url%29.md)
  Creates an input/output file handle instance that represents a file at a URL.
- [func makeIOHandle(url: URL) throws -> any MTLIOFileHandle](./makeiohandle%28url%29.md)
  Creates an input/output file handle instance that represents a file at a URL.
- [func makeIOHandle(url: URL, compressionMethod: MTLIOCompressionMethod) throws -> any MTLIOFileHandle](./makeiohandle%28url,compressionmethod%29.md)
  Creates an input/output file handle instance that represents a compressed file at a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeiofilehandle(url:compressionmethod:))*