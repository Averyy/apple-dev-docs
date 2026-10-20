# init(enabledProfiles:disabledProfiles:)

**Framework**: Core MIDI  
**Kind**: init

Creates a new profile state object for the specified profiles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(enabledProfiles enabled: [MIDICIProfile], disabledProfiles disabled: [MIDICIProfile])
```

#### Return Value

A new profile state instance.

## Parameters

- `enabled`: The enabled MIDI-CI profiles.
- `disabled`: The disabled MIDI-CI profiles.

## See Also

- [init(channel: MIDIChannelNumber, enabledProfiles: [MIDICIProfile], disabledProfiles: [MIDICIProfile])](midiciprofilestate/init(channel:enabledprofiles:disabledprofiles:).md)
  Creates a new profile state object for the specified MIDI channel and profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofilestate/init(enabledprofiles:disabledprofiles:))*