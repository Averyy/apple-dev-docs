# KeyResult.KeySignature

**Framework**: Music Understanding  
**Kind**: struct

The set of sharp and flat symbols for the notes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let tonic: KeyResult.Tonic](keyresult/keysignature/tonic.md)
  The root note of the musical key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/keyresult/keysignature)*