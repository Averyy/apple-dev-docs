# deviceBrowserView(_:didEncounterError:)

**Framework**: Quartz  
**Kind**: method

Invoked when the device browser encounters an error.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func deviceBrowserView(_ deviceBrowserView: IKDeviceBrowserView!, didEncounterError error: (any Error)!)
```

#### Discussion

The user should handle the error in some fashion, for example, presenting an error panel to the user.

## Parameters

- `deviceBrowserView`: The object that sent the message.
- `error`: The error the device browser encountered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikdevicebrowserviewdelegate/devicebrowserview(_:didencountererror:))*