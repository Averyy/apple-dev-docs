# outputStreamToFileAtPath:append:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an initialized output stream for writing to a specified file.

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
+ (instancetype) outputStreamToFileAtPath:(NSString *) path append:(BOOL) shouldAppend;
```

## Return Value

An initialized output stream that can write to `path`.

## Discussion

The stream must be opened before it can be used.

## Parameters

- `path`: The path to the file the output stream will write to.
- `shouldAppend`: [`true`](../../Swift/true.md) if newly written data should be appended to any existing file contents, otherwise [`false`](../../Swift/false.md).

## See Also

### Creating Streams
- [class func toMemory() -> Self](../outputstream/tomemory%28%29.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [+ outputStreamToBuffer:capacity:](./outputstreamtobuffer_capacity_.md)
  Creates and returns an initialized output stream that can write to a provided buffer.
- [init(toMemory: ())](../outputstream/init%28tomemory%29.md)
  Returns an initialized output stream that will write to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](../outputstream/init%28tobuffer,capacity%29.md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](../outputstream/init%28tofileatpath,append%29.md)
  Returns an initialized output stream for writing to a specified file.
- [init?(url: URL, append: Bool)](../outputstream/init%28url,append%29-5soau.md)
  Returns an initialized output stream for writing to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsoutputstream/outputstreamtofileatpath:append:)*