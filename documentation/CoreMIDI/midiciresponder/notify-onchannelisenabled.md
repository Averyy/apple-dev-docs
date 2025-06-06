# notify(_:onChannel:isEnabled:)

**Framework**: Core MIDI  
**Kind**: method

Enables or disables a profile and notifies all connected initiators.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func notify(_ aProfile: MIDICIProfile, onChannel channel: MIDIChannelNumber, isEnabled enabledState: Bool) -> Bool
```

## Parameters

- `aProfile`: The profile to update.
- `channel`: The MIDI channel.
- `enabledState`: A Boolean value that indicates whether to enable the profile.

## See Also

- [func send(MIDICIProfile, onChannel: MIDIChannelNumber, profileData: Data) -> Bool](midiciresponder/send(_:onchannel:profiledata:).md)
  Sends profile-specific data to all connected initiators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder/notify(_:onchannel:isenabled:))*