# InstrumentActivityResult.Instrument

**Framework**: Music Understanding  
**Kind**: struct  
**Role**: Structure

A type that identifies a specific instrument category.

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
struct Instrument
```

#### Overview

The framework defines four built-in categories: [`vocal`](./instrument/vocal.md), [`drum`](./instrument/drum.md), [`bass`](./instrument/bass.md), and [`other`](./instrument/other.md). The [`other`](./instrument/other.md) category groups any instruments that don’t fall into the other three categories.

## Topics

### Instance Properties
- [let rawValue: String](./instrument/rawvalue.md)
  The raw value string.
### Type Properties
- [static let bass: InstrumentActivityResult.Instrument](./instrument/bass.md)
  The key to use to obtain bass activity from an instrument activity result.
- [static let drum: InstrumentActivityResult.Instrument](./instrument/drum.md)
  The key to use to obtain drum activity from an instrument activity result.
- [static let other: InstrumentActivityResult.Instrument](./instrument/other.md)
  The key to use to obtain other instrument activity from an instrument activity result.
- [static let vocal: InstrumentActivityResult.Instrument](./instrument/vocal.md)
  The key to use to obtain vocal activity from an instrument activity result.

## Relationships

### Conforms To
- [CodingKeyRepresentable](../../Swift/codingkeyrepresentable.md)
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/instrumentactivityresult/instrument)*