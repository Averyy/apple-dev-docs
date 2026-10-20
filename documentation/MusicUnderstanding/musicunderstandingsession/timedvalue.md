# MusicUnderstandingSession.TimedValue

**Framework**: Music Understanding  
**Kind**: struct  
**Role**: Structure

A structure that pairs a value with a time.

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
struct TimedValue<Value> where Value : Decodable, Value : Encodable, Value : Equatable, Value : Sendable
```

#### Overview

The `TimedValue` pairs a value with a `CMTime` point — a measurement at a specific instant, as opposed to a span. Contrast: properties that hold constant over a span (key, pace) use RangedValue with a `CMTimeRange`; instantaneous measurements use `TimedValue` with a `CMTime`.

## Topics

### Getting the time
- [let time: CMTime](./timedvalue/time.md)
  The time at which the value applies.
### Getting the value
- [let value: Value](./timedvalue/value.md)
  The value associated with the time.
### Initializers
- [init(from: any Decoder) throws](./timedvalue/init%28from%29.md)
  Creates a timed value by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](./timedvalue/encode%28to%29.md)
  Encodes the timed value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Support types
- [MusicUnderstandingSession.RangedValue](./rangedvalue.md)
  A structure that pairs a value over a time range.
- [struct AnalysisType](../analysistype.md)
  The analysis type for each session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/timedvalue)*