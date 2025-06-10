# MTLCaptureDestination

**Framework**: Metal  
**Kind**: enum

The kinds of destinations for captured command data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLCaptureDestination
```

## Topics

### Choosing a Destination
- [MTLCaptureDestination.developerTools](mtlcapturedestination/developertools.md)
  An option specifying that data should be captured to Xcode and that execution should stop in Xcode after the data is captured.
- [MTLCaptureDestination.gpuTraceDocument](mtlcapturedestination/gputracedocument.md)
  An option specifying that the captured command data should be saved to a GPU trace document.
### Initializers
- [init?(rawValue: Int)](mtlcapturedestination/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTLCaptureDescriptor](mtlcapturedescriptor.md)
  A configuration for a Metal capture session.
- [class MTLCaptureManager](mtlcapturemanager.md)
  An instance you use to capture Metal command data in your app.
- [protocol MTLCaptureScope](mtlcapturescope.md)
  A protocol that defines custom boundaries for a GPU frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturedestination)*