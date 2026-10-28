# maxBufferLength

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var maxBufferLength: Int { get }
```

```objc
@property (readonly) NSUInteger maxBufferLength;
```

## Discussion

The property’s value is at least 256 MB (268,435,456 bytes).

## See Also

### Creating buffers
- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](./makebuffer%28length,options%29.md)
  Creates a buffer the method clears with zero values.
- [func makeBuffer(bytes: UnsafeRawPointer, length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](./makebuffer%28bytes,length,options%29.md)
  Allocates a new buffer of a given length and initializes its contents by copying existing data into it.
- [func makeBuffer(bytesNoCopy: UnsafeMutableRawPointer, length: Int, options: MTLResourceOptions, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?) -> (any MTLBuffer)?](./makebuffer%28bytesnocopy,length,options,deallocator%29.md)
  Creates a buffer that wraps an existing contiguous memory allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maxbufferlength)*