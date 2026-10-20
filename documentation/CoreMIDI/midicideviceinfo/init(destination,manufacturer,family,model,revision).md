# init(destination:manufacturer:family:model:revision:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

Creates a new device information instance.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
init(destination midiDestination: MIDIEntityRef, manufacturer: Data, family: Data, model modelNumber: Data, revision revisionLevel: Data)
```

```objc
- (instancetype) initWithDestination:(MIDIEntityRef) midiDestination manufacturer:(NSData *) manufacturer family:(NSData *) family model:(NSData *) modelNumber revision:(NSData *) revisionLevel;
```

## Parameters

- `midiDestination`: The MIDI destination to use for capability inquiry.
- `manufacturer`: The device manufacturer.
- `family`: The family to which this device belongs.
- `modelNumber`: The device’s model number.
- `revisionLevel`: The version of the device’s model number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceinfo/init(destination:manufacturer:family:model:revision:))*