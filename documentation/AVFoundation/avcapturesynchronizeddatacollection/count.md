# count

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The number of synchronized data objects in the collection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var count: Int { get }
```

```objc
@property (readonly) NSUInteger count;
```

## See Also

### Accessing synchronized data
- [func synchronizedData(for: AVCaptureOutput) -> AVCaptureSynchronizedData?](./synchronizeddata%28for%29.md)
  Returns synchronized data captured by the specified capture output.
- [subscript(AVCaptureOutput) -> AVCaptureSynchronizedData?](./subscript%28_%29.md)
  Returns data captured by the specified capture output, using subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection/count)*