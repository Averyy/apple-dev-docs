# timestamp

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time at which this synchronized data was captured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var timestamp: CMTime { get }
```

```objc
@property (readonly) CMTime timestamp;
```

#### Discussion

Synchronized data is always synchronized to the [`masterClock`](../avcapturesession/masterclock.md) time of the [`AVCaptureSession`](../avcapturesession.md) object to which the data output is connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddata/timestamp)*