# init(deviceInfo:profileDelegate:profileStates:supportProperties:)

**Framework**: Core MIDI  
**Kind**: init

Creates a new responder.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(deviceInfo: MIDICIDeviceInfo, profileDelegate delegate: any MIDICIProfileResponderDelegate, profileStates profileList: [MIDICIProfileState], supportProperties propertiesSupported: Bool)
```

## Parameters

- `deviceInfo`: The MIDI-CI device information.
- `delegate`: The responder’s delegate object.
- `profileList`: The list of profile state objects.
- `propertiesSupported`: A Boolean value that indicates whether the responder supports properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder/init(deviceinfo:profiledelegate:profilestates:supportproperties:))*