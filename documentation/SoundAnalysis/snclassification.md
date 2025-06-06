# SNClassification

**Framework**: Sound Analysis  
**Kind**: class

A type that pairs a sound classifier’s prediction with its confidence in that prediction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class SNClassification
```

#### Overview

An `SNClassification` represents a single sound classification prediction, and the sound classifier model’s confidence in that prediction.

## Topics

### Inspecting a Classification
- [var identifier: String](snclassification/identifier.md)
  A prediction label that’s one of the classifications a sound classifier’s underlying model defines.
- [var confidence: Double](snclassification/confidence.md)
  The confidence value the model has in its prediction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var timeRange: CMTimeRange](snclassificationresult/timerange.md)
  The time span that corresponds to the result’s classifications.
- [var classifications: [SNClassification]](snclassificationresult/classifications.md)
  A sorted array of the request’s top classification candidates.
- [func classification(forIdentifier: String) -> SNClassification?](snclassificationresult/classification(foridentifier:).md)
  Returns the classification for an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassification)*