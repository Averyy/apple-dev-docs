# showSystemUserInterface(_:)

**Framework**: AVFoundation  
**Kind**: method

Displays the system’s user interface to configure video effects or microphone modes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
class func showSystemUserInterface(_ systemUserInterface: AVCaptureDevice.SystemUserInterface)
```

#### Discussion

Use this method to prompt the user to make changes to Video Effects (such as Center Stage or Portrait Effect) or Microphone Modes. It presents the system user interface and deep links to the appropriate module.

Calling this method isn’t a blocking operation. After the system presents the indicated user interface, control returns immediately to the app.

## Parameters

- `systemUserInterface`: The system user interface to present.

## See Also

- [AVCaptureDevice.SystemUserInterface](avcapturedevice/systemuserinterface.md)
  Constants that describe the capture device configuration user interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/showsystemuserinterface(_:))*