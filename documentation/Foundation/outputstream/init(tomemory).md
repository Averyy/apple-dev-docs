# init(toMemory:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an initialized output stream that will write to memory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(toMemory: ())
```

```objc
- (instancetype) initToMemory;
```

## Return Value

An initialized output stream that will write stream data to memory.

## Discussion

The stream must be opened before it can be used.

The contents of the memory stream are retrieved by passing the constant `NSStreamDataWrittenToMemoryStreamKey` to [`property(forKey:)`](../stream/property%28forkey%29.md).

## See Also

### Creating Streams
- [class func toMemory() -> Self](./tomemory%28%29.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](./init%28tobuffer,capacity%29.md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](./init%28tofileatpath,append%29.md)
  Returns an initialized output stream for writing to a specified file.
- [init?(url: URL, append: Bool)](./init%28url,append%29-5soau.md)
  Returns an initialized output stream for writing to a specified URL.
- [+ outputStreamToBuffer:capacity:](../nsoutputstream/outputstreamtobuffer_capacity_.md)
  Creates and returns an initialized output stream that can write to a provided buffer.
- [+ outputStreamToFileAtPath:append:](../nsoutputstream/outputstreamtofileatpath_append_.md)
  Creates and returns an initialized output stream for writing to a specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream/init(tomemory:))*