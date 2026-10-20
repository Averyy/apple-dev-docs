# connections

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The capture output object’s connections.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var connections: [AVCaptureConnection] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVCaptureConnection *> * connections;
```

#### Discussion

Each connection object in the array describes the mapping between the output and the capture input ports.

## See Also

### Accessing connections
- [func connection(with: AVMediaType) -> AVCaptureConnection?](./connection%28with%29.md)
  Returns the first connection with an input port of a specified media type.
- [AVCaptureOutput.DataDroppedReason](./datadroppedreason.md)
  Constants that define reasons for why the system dropped a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/connections)*