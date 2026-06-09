# canGroupWithCurrentlyActivatedDevices

**Framework**: Media Device  
**Kind**: property

Indicates whether this device can be grouped with devices that are currently activated.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let canGroupWithCurrentlyActivatedDevices: Bool
```

#### Discussion

When `true`, this device supports being added to a group with other devices via [`activateDevice(_:session:for:)`](mediadeviceextension/activatedevice(_:session:for:).md)

When `false`, the device must be activated independently and cannot join ongoing playback sessions on other devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/cangroupwithcurrentlyactivateddevices)*