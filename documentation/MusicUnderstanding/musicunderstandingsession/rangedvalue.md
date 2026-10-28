# MusicUnderstandingSession.RangedValue

**Framework**: Music Understanding  
**Kind**: struct  
**Role**: Structure

A structure that pairs a value over a time range.

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
struct RangedValue<Value> where Value : Decodable, Value : Encodable, Value : Equatable, Value : Sendable
```

## Overview

The `RangedValue` is a container pairing an analysis value with a CMTimeRange segment of media time. Music properties like key and pace change over a track. The results are expressed as a sequence of contiguous segments covering the full timeline.

## Topics

### Getting the time range
- [let range: CMTimeRange](./rangedvalue/range.md)
  The time range over which the value applies.
### Getting the value
- [let value: Value](./rangedvalue/value.md)
  The value associated with the time range.
### Initializers
- [init(from: any Decoder) throws](./rangedvalue/init%28from%29.md)
  Creates a ranged value by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](./rangedvalue/encode%28to%29.md)
  Encodes the ranged value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Support types
- [MusicUnderstandingSession.TimedValue](./timedvalue.md)
  A structure that pairs a value with a time.
- [struct AnalysisType](../analysistype.md)
  The analysis type for each session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/rangedvalue)*