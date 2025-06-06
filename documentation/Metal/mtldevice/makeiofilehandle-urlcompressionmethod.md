# makeIOFileHandle(url:compressionMethod:)

**Framework**: Metal  
**Kind**: method  
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

#### Return Value

A new [`MTLIOFileHandle`](mtliofilehandle.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

#### Discussion

For information about using input/output command queues and file handles, see [`Resource Loading`](resource-loading.md).

## Parameters

- `url`: A location URL to a compressed file in the file system.
- `compressionMethod`: The file’s compression format.

## See Also

- [func makeIOFileHandle(url: URL) throws -> any MTLIOFileHandle](mtldevice/makeiofilehandle(url:).md)
  Creates an input/output file handle instance that represents a file at a URL.
- [func makeIOHandle(url: URL) throws -> any MTLIOFileHandle](mtldevice/makeiohandle(url:).md)
  Creates an input/output file handle instance that represents a file at a URL.
- [func makeIOHandle(url: URL, compressionMethod: MTLIOCompressionMethod) throws -> any MTLIOFileHandle](mtldevice/makeiohandle(url:compressionmethod:).md)
  Creates an input/output file handle instance that represents a compressed file at a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeiofilehandle(url:compressionmethod:))*