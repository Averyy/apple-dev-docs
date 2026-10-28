# init(enabledProfiles:disabledProfiles:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

Creates a new profile state object for the specified profiles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

> **Deprecated**: Use [`init(channel:enabledProfiles:disabledProfiles:)`](./init%28channel,enabledprofiles,disabledprofiles%29.md) instead.

## Declaration

```swift
init(enabledProfiles enabled: [MIDICIProfile], disabledProfiles disabled: [MIDICIProfile])
```

```objc
- (instancetype) initWithEnabledProfiles:(NSArray<MIDICIProfile *> *) enabled disabledProfiles:(NSArray<MIDICIProfile *> *) disabled;
```

## Return Value

A new profile state instance.

## Parameters

- `enabled`: The enabled MIDI-CI profiles.
- `disabled`: The disabled MIDI-CI profiles.

## See Also

### Creating a Profile State
- [init(channel: MIDIChannelNumber, enabledProfiles: [MIDICIProfile], disabledProfiles: [MIDICIProfile])](./init%28channel,enabledprofiles,disabledprofiles%29.md)
  Creates a new profile state object for the specified MIDI channel and profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofilestate/init(enabledprofiles:disabledprofiles:))*