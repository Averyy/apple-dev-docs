# duration

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The sum of all durations of buffers in the queue.

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
var duration: CMTime { get }
```

## See Also

### Inspecting Duration and Timing
- [var totalSize: Int](./totalsize.md)
  The total size of all buffers in the queue.
- [var firstDecodeTimeStamp: CMTime](./firstdecodetimestamp.md)
  The decode timestamp of the first buffer in the queue.
- [var firstPresentationTimeStamp: CMTime](./firstpresentationtimestamp.md)
  The presentation timestamp of the first buffer in the queue.
- [var endPresentationTimeStamp: CMTime](./endpresentationtimestamp.md)
  The greatest end presentation timestamp.
- [var minDecodeTimeStamp: CMTime](./mindecodetimestamp.md)
  The earliest decode timestamp.
- [var minPresentationTimeStamp: CMTime](./minpresentationtimestamp.md)
  The earliest presentation timestamp.
- [var maxPresentationTimeStamp: CMTime](./maxpresentationtimestamp.md)
  The greatest presentation timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/duration)*