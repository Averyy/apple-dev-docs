# MusicUnderstandingSession.TimedValue

**Framework**: Music Understanding  
**Kind**: struct

A structure that pairs a value with a time.

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
struct TimedValue<Value> where Value : Decodable, Value : Encodable, Value : Equatable, Value : Sendable
```

#### Overview

The `TimedValue` pairs a value with a `CMTime` point — a measurement at a specific instant, as opposed to a span. Contrast: properties that hold constant over a span (key, pace) use RangedValue with a `CMTimeRange`; instantaneous measurements use `TimedValue` with a `CMTime`.

## Topics

### Getting the time
- [let time: CMTime](musicunderstandingsession/timedvalue/time.md)
  The time at which the value applies.
### Getting the value
- [let value: Value](musicunderstandingsession/timedvalue/value.md)
  The value associated with the time.
### Initializers
- [init(from: any Decoder) throws](musicunderstandingsession/timedvalue/init(from:).md)
  Creates a timed value by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](musicunderstandingsession/timedvalue/encode(to:).md)
  Encodes the timed value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MusicUnderstandingSession.RangedValue](musicunderstandingsession/rangedvalue.md)
  A structure that pairs a value over a time range.
- [struct AnalysisType](analysistype.md)
  The analysis type for each session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/timedvalue)*