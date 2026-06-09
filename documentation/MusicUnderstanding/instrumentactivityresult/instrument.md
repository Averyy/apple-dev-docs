# InstrumentActivityResult.Instrument

**Framework**: MusicUnderstanding  
**Kind**: struct

A type that identifies a specific instrument category.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Instrument
```

#### Overview

The framework defines four built-in categories: [`vocal`](instrumentactivityresult/instrument/vocal.md), [`drum`](instrumentactivityresult/instrument/drum.md), [`bass`](instrumentactivityresult/instrument/bass.md), and [`other`](instrumentactivityresult/instrument/other.md). The [`other`](instrumentactivityresult/instrument/other.md) category groups any instruments that don’t fall into the other three categories.

## Topics

### Instance Properties
- [let rawValue: String](instrumentactivityresult/instrument/rawvalue.md)
  The raw value string.
### Type Properties
- [static let bass: InstrumentActivityResult.Instrument](instrumentactivityresult/instrument/bass.md)
  The key to use to obtain bass activity from an instrument activity result.
- [static let drum: InstrumentActivityResult.Instrument](instrumentactivityresult/instrument/drum.md)
  The key to use to obtain drum activity from an instrument activity result.
- [static let other: InstrumentActivityResult.Instrument](instrumentactivityresult/instrument/other.md)
  The key to use to obtain other instrument activity from an instrument activity result.
- [static let vocal: InstrumentActivityResult.Instrument](instrumentactivityresult/instrument/vocal.md)
  The key to use to obtain vocal activity from an instrument activity result.

## Relationships

### Conforms To
- [CodingKeyRepresentable](../Swift/CodingKeyRepresentable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/instrumentactivityresult/instrument)*