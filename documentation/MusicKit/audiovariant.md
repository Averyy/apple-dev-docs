# AudioVariant

**Framework**: MusicKit  
**Kind**: enum

Variants that indicate the quality of audio available for an item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum AudioVariant
```

## Topics

### Operators
- [static func == (AudioVariant, AudioVariant) -> Bool](audiovariant/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [AudioVariant.dolbyAtmos](audiovariant/dolbyatmos.md)
  Dolby Atmos is an immersive audio experience that surrounds you with sound from all sides, including above.
- [AudioVariant.dolbyAudio](audiovariant/dolbyaudio.md)
  Dolby Audio is a surround sound format that includes Dolby 5.1 and 7.1.
- [AudioVariant.highResolutionLossless](audiovariant/highresolutionlossless.md)
  Hi-Res Lossless uses Apple Lossless Audio Codec (ALAC) for bit-for-bit accuracy up to 24-bit/192 kHz.
- [AudioVariant.lossless](audiovariant/lossless.md)
  Lossless uses Apple Lossless Audio Codec (ALAC) for bit-for-bit accuracy up to 24-bit/48 kHz.
- [AudioVariant.lossyStereo](audiovariant/lossystereo.md)
  Lossy stereo uses compression used to store sound data.
- [AudioVariant.spatialAudio](audiovariant/spatialaudio.md)
  Spatial audio is a fallback mode if the content is Dolby Atmos or Dolby Audio, but hardware capabilities don’t support them.
### Instance Properties
- [var hashValue: Int](audiovariant/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](audiovariant/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [AudioVariant.AllCases](audiovariant/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [AudioVariant]](audiovariant/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [CustomStringConvertible Implementations](audiovariant/customstringconvertible-implementations.md)
- [Decodable Implementations](audiovariant/decodable-implementations.md)
- [Encodable Implementations](audiovariant/encodable-implementations.md)
- [Equatable Implementations](audiovariant/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/audiovariant)*