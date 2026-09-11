# AnalysisType

**Framework**: Music Understanding  
**Kind**: struct

The analysis type for each session.

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
struct AnalysisType
```

#### Overview

This serves as the primarily type used by the [`MusicUnderstandingSession`](musicunderstandingsession.md).

## Topics

### Types of analysis
- [static let key: AnalysisType](analysistype/key.md)
  A value that identifies the key music analysis type.
- [static let instrumentActivity: AnalysisType](analysistype/instrumentactivity.md)
  A value that identifies the instrument activity music analysis type.
- [static let loudness: AnalysisType](analysistype/loudness.md)
  A value that identifies the loudness music analysis type.
- [static let pace: AnalysisType](analysistype/pace.md)
  A value that identifies the pace music analysis type.
- [let rawValue: String](analysistype/rawvalue.md)
  A value that identifies the type of music analysis to perform.
- [static let rhythm: AnalysisType](analysistype/rhythm.md)
  A value that identifies the rhythm music analysis type.
- [static let structure: AnalysisType](analysistype/structure.md)
  A value that identifies the structure music analysis type.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [MusicUnderstandingSession.TimedValue](musicunderstandingsession/timedvalue.md)
  A structure that pairs a value with a time.
- [MusicUnderstandingSession.RangedValue](musicunderstandingsession/rangedvalue.md)
  A structure that pairs a value over a time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/analysistype)*