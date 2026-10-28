# SNClassification

**Framework**: Sound Analysis  
**Kind**: class  
**Role**: Class

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

```objc
@interface SNClassification : NSObject
```

## Overview

An `SNClassification` represents a single sound classification prediction, and the sound classifier model’s confidence in that prediction.

## Topics

### Inspecting a Classification
- [var identifier: String](./snclassification/identifier.md)
  A prediction label that’s one of the classifications a sound classifier’s underlying model defines.
- [var confidence: Double](./snclassification/confidence.md)
  The confidence value the model has in its prediction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Inspecting the Result
- [var timeRange: CMTimeRange](./snclassificationresult/timerange.md)
  The time span that corresponds to the result’s classifications.
- [var classifications: [SNClassification]](./snclassificationresult/classifications.md)
  A sorted array of the request’s top classification candidates.
- [func classification(forIdentifier: String) -> SNClassification?](./snclassificationresult/classification%28foridentifier%29.md)
  Returns the classification for an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassification)*