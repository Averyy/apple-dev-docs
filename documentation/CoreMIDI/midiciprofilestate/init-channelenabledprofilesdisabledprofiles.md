# init(channel:enabledProfiles:disabledProfiles:)

**Framework**: Core MIDI  
**Kind**: init

Creates a new profile state object for the specified MIDI channel and profiles.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(channel midiChannelNum: MIDIChannelNumber, enabledProfiles enabled: [MIDICIProfile], disabledProfiles disabled: [MIDICIProfile])
```

## Parameters

- `midiChannelNum`: The MIDI channel.
- `enabled`: The enabled MIDI-CI profles.
- `disabled`: The disabled MIDI-CI profles.

## See Also

- [init(enabledProfiles: [MIDICIProfile], disabledProfiles: [MIDICIProfile])](midiciprofilestate/init(enabledprofiles:disabledprofiles:).md)
  Creates a new profile state object for the specified profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofilestate/init(channel:enabledprofiles:disabledprofiles:))*