# send(_:onChannel:profileData:)

**Framework**: Core MIDI  
**Kind**: method

Sends profile-specific data to all connected initiators.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func send(_ aProfile: MIDICIProfile, onChannel channel: MIDIChannelNumber, profileData profileSpecificData: Data) -> Bool
```

#### Return Value

A Boolean value that indicates whether the operation succeeded.

## Parameters

- `aProfile`: The profile to send.
- `channel`: The MIDI channel.
- `profileSpecificData`: The data to send.

## See Also

- [func notify(MIDICIProfile, onChannel: MIDIChannelNumber, isEnabled: Bool) -> Bool](midiciresponder/notify(_:onchannel:isenabled:).md)
  Enables or disables a profile and notifies all connected initiators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder/send(_:onchannel:profiledata:))*