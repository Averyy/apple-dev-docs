# MusicUnderstandingSession.RangedValue

**Framework**: Music Understanding  
**Kind**: struct

A structure that pairs a value over a time range.

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
struct RangedValue<Value> where Value : Decodable, Value : Encodable, Value : Equatable, Value : Sendable
```

#### Overview

The `RangedValue` is a container pairing an analysis value with a CMTimeRange segment of media time. Music properties like key and pace change over a track. The results are expressed as a sequence of contiguous segments covering the full timeline.

## Topics

### Getting the time range
- [let range: CMTimeRange](musicunderstandingsession/rangedvalue/range.md)
  The time range over which the value applies.
### Getting the value
- [let value: Value](musicunderstandingsession/rangedvalue/value.md)
  The value associated with the time range.
### Initializers
- [init(from: any Decoder) throws](musicunderstandingsession/rangedvalue/init(from:).md)
  Creates a ranged value by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](musicunderstandingsession/rangedvalue/encode(to:).md)
  Encodes the ranged value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MusicUnderstandingSession.TimedValue](musicunderstandingsession/timedvalue.md)
  A structure that pairs a value with a time.
- [struct AnalysisType](analysistype.md)
  The analysis type for each session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/rangedvalue)*