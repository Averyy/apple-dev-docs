# notify(_:onChannel:isEnabled:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

Enables or disables a profile and notifies all connected initiators.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
func notify(_ aProfile: MIDICIProfile, onChannel channel: MIDIChannelNumber, isEnabled enabledState: Bool) -> Bool
```

```objc
- (BOOL) notifyProfile:(MIDICIProfile *) aProfile onChannel:(MIDIChannelNumber) channel isEnabled:(BOOL) enabledState;
```

## Parameters

- `aProfile`: The profile to update.
- `channel`: The MIDI channel.
- `enabledState`: A Boolean value that indicates whether to enable the profile.

## See Also

### Broadcasting Profile Changes
- [func send(MIDICIProfile, onChannel: MIDIChannelNumber, profileData: Data) -> Bool](./send%28_,onchannel,profiledata%29.md)
  Sends profile-specific data to all connected initiators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder/notify(_:onchannel:isenabled:))*