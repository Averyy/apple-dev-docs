# init(channel:enabledProfiles:disabledProfiles:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

Creates a new profile state object for the specified MIDI channel and profiles.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
init(channel midiChannelNum: MIDIChannelNumber, enabledProfiles enabled: [MIDICIProfile], disabledProfiles disabled: [MIDICIProfile])
```

```objc
- (instancetype) initWithChannel:(MIDIChannelNumber) midiChannelNum enabledProfiles:(NSArray<MIDICIProfile *> *) enabled disabledProfiles:(NSArray<MIDICIProfile *> *) disabled;
```

## Parameters

- `midiChannelNum`: The MIDI channel.
- `enabled`: The enabled MIDI-CI profles.
- `disabled`: The disabled MIDI-CI profles.

## See Also

### Creating a Profile State
- [init(enabledProfiles: [MIDICIProfile], disabledProfiles: [MIDICIProfile])](./init%28enabledprofiles,disabledprofiles%29.md)
  Creates a new profile state object for the specified profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofilestate/init(channel:enabledprofiles:disabledprofiles:))*