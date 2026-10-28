# ports

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<AVCaptureInputPort *> * ports;
```

## Discussion

Individual ports post an [`formatDescriptionDidChangeNotification`](./port/formatdescriptiondidchangenotification.md) notification when their [`formatDescription`](./port/formatdescription.md) changes.

## See Also

### Accessing ports
- [AVCaptureInput.Port](./port.md)
  An object that represents a stream of data that a capture input provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/ports)*