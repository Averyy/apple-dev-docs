# KeyResult.KeySignature

**Framework**: Music Understanding  
**Kind**: struct

The set of sharp and flat symbols for the notes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct KeySignature
```

#### Overview

A key signature pairs a root note, [`tonic`](keyresult/keysignature/tonic.md) with a [`mode`](keyresult/keysignature/mode.md), major or minor, to describe the harmonic center of a section of audio.

## Topics

### Tonic and mode
- [let tonic: KeyResult.Tonic](keyresult/keysignature/tonic.md)
  The root note of the musical key.
- [let mode: KeyResult.Mode](keyresult/keysignature/mode.md)
  The mode of the musical key.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let tonic: KeyResult.Tonic](keyresult/keysignature/tonic.md)
  The root note of the musical key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/keyresult/keysignature)*