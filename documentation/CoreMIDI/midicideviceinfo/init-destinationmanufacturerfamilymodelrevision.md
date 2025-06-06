# init(destination:manufacturer:family:model:revision:)

**Framework**: Core MIDI  
**Kind**: init

Creates a new device information instance.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(destination midiDestination: MIDIEntityRef, manufacturer: Data, family: Data, model modelNumber: Data, revision revisionLevel: Data)
```

## Parameters

- `midiDestination`: The MIDI destination to use for capability inquiry.
- `manufacturer`: The device manufacturer.
- `family`: The family to which this device belongs.
- `modelNumber`: The device’s model number.
- `revisionLevel`: The version of the device’s model number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceinfo/init(destination:manufacturer:family:model:revision:))*