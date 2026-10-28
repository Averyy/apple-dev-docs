# send(_:onChannel:profileData:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

Sends profile-specific data to all connected initiators.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
func send(_ aProfile: MIDICIProfile, onChannel channel: MIDIChannelNumber, profileData profileSpecificData: Data) -> Bool
```

```objc
- (BOOL) sendProfile:(MIDICIProfile *) aProfile onChannel:(MIDIChannelNumber) channel profileData:(NSData *) profileSpecificData;
```

## Return Value

A Boolean value that indicates whether the operation succeeded.

## Parameters

- `aProfile`: The profile to send.
- `channel`: The MIDI channel.
- `profileSpecificData`: The data to send.

## See Also

### Broadcasting Profile Changes
- [func notify(MIDICIProfile, onChannel: MIDIChannelNumber, isEnabled: Bool) -> Bool](./notify%28_,onchannel,isenabled%29.md)
  Enables or disables a profile and notifies all connected initiators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder/send(_:onchannel:profiledata:))*