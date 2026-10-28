# toMemory()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an initialized output stream that will write stream data to memory.

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
class func toMemory() -> Self
```

```objc
+ (instancetype) outputStreamToMemory;
```

## Return Value

An initialized output stream that will write stream data to memory.

## Discussion

The stream must be opened before it can be used.

You retrieve the contents of the memory stream by sending the message [`property(forKey:)`](../stream/property%28forkey%29.md) to the receiver with an argument of `NSStreamDataWrittenToMemoryStreamKey`.

## See Also

### Related Documentation
- [Stream Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i)
- [+ outputStreamToBuffer:capacity:](../nsoutputstream/outputstreamtobuffer_capacity_.md)
  Creates and returns an initialized output stream that can write to a provided buffer.
- [+ outputStreamToFileAtPath:append:](../nsoutputstream/outputstreamtofileatpath_append_.md)
  Creates and returns an initialized output stream for writing to a specified file.
### Creating Streams
- [init(toMemory: ())](./init%28tomemory%29.md)
  Returns an initialized output stream that will write to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](./init%28tobuffer,capacity%29.md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](./init%28tofileatpath,append%29.md)
  Returns an initialized output stream for writing to a specified file.
- [init?(url: URL, append: Bool)](./init%28url,append%29-5soau.md)
  Returns an initialized output stream for writing to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream/tomemory())*