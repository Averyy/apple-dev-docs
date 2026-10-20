# endPresentationTimeStamp

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The greatest end presentation timestamp.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var endPresentationTimeStamp: CMTime { get }
```

## See Also

### Inspecting Duration and Timing
- [var duration: CMTime](./duration.md)
  The sum of all durations of buffers in the queue.
- [var totalSize: Int](./totalsize.md)
  The total size of all buffers in the queue.
- [var firstDecodeTimeStamp: CMTime](./firstdecodetimestamp.md)
  The decode timestamp of the first buffer in the queue.
- [var firstPresentationTimeStamp: CMTime](./firstpresentationtimestamp.md)
  The presentation timestamp of the first buffer in the queue.
- [var minDecodeTimeStamp: CMTime](./mindecodetimestamp.md)
  The earliest decode timestamp.
- [var minPresentationTimeStamp: CMTime](./minpresentationtimestamp.md)
  The earliest presentation timestamp.
- [var maxPresentationTimeStamp: CMTime](./maxpresentationtimestamp.md)
  The greatest presentation timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/endpresentationtimestamp)*