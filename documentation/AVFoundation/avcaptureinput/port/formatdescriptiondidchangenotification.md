# formatDescriptionDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSNotificationName const AVCaptureInputPortFormatDescriptionDidChangeNotification;
```

#### Discussion

The notification’s [`object`](../../../Foundation/notification/object.md) property contains the [`AVCaptureInput.Port`](../port.md) object whose format changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification)*