# outputStreamToBuffer:capacity:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an initialized output stream that can write to a provided buffer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) outputStreamToBuffer:(uint8_t *) buffer capacity:(NSUInteger) capacity;
```

#### Return Value

An initialized output stream that can write to `buffer`.

#### Discussion

The stream must be opened before it can be used.

When the number of bytes written to `buffer` has reached `capacity`, the stream’s [`streamStatus`](../stream/streamstatus.md) will return `NSStreamStatusAtEnd`.

## Parameters

- `buffer`: The buffer the output stream will write to.
- `capacity`: The size of the buffer in bytes.

## See Also

### Creating Streams
- [class func toMemory() -> Self](../outputstream/tomemory%28%29.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [+ outputStreamToFileAtPath:append:](./outputstreamtofileatpath_append_.md)
  Creates and returns an initialized output stream for writing to a specified file.
- [init(toMemory: ())](../outputstream/init%28tomemory%29.md)
  Returns an initialized output stream that will write to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](../outputstream/init%28tobuffer,capacity%29.md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](../outputstream/init%28tofileatpath,append%29.md)
  Returns an initialized output stream for writing to a specified file.
- [init?(url: URL, append: Bool)](../outputstream/init%28url,append%29-5soau.md)
  Returns an initialized output stream for writing to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsoutputstream/outputstreamtobuffer:capacity:)*