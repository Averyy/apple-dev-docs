# formatDescriptionDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property

A notification the system posts when the capture input port’s format description changes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
class let formatDescriptionDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification’s [`object`](https://developer.apple.com/documentation/foundation/notification/1779839-object) property contains the [`AVCaptureInput.Port`](avcaptureinput/port.md) object whose format changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification)*