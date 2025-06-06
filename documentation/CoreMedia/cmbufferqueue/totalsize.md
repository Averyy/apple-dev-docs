# totalSize

**Framework**: Core Media  
**Kind**: property

The total size of all buffers in the queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var totalSize: Int { get }
```

## See Also

- [var duration: CMTime](cmbufferqueue/duration.md)
  The sum of all durations of buffers in the queue.
- [var firstDecodeTimeStamp: CMTime](cmbufferqueue/firstdecodetimestamp.md)
  The decode timestamp of the first buffer in the queue.
- [var firstPresentationTimeStamp: CMTime](cmbufferqueue/firstpresentationtimestamp.md)
  The presentation timestamp of the first buffer in the queue.
- [var endPresentationTimeStamp: CMTime](cmbufferqueue/endpresentationtimestamp.md)
  The greatest end presentation timestamp.
- [var minDecodeTimeStamp: CMTime](cmbufferqueue/mindecodetimestamp.md)
  The earliest decode timestamp.
- [var minPresentationTimeStamp: CMTime](cmbufferqueue/minpresentationtimestamp.md)
  The earliest presentation timestamp.
- [var maxPresentationTimeStamp: CMTime](cmbufferqueue/maxpresentationtimestamp.md)
  The greatest presentation timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/totalsize)*