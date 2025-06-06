# ports

**Framework**: AVFoundation  
**Kind**: property

The ports available on a capture input.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var ports: [AVCaptureInput.Port] { get }
```

#### Discussion

Individual ports post an [`formatDescriptionDidChangeNotification`](avcaptureinput/port/formatdescriptiondidchangenotification.md) notification when their [`formatDescription`](avcaptureinput/port/formatdescription.md) changes.

## See Also

- [AVCaptureInput.Port](avcaptureinput/port.md)
  An object that represents a stream of data that a capture input provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/ports)*