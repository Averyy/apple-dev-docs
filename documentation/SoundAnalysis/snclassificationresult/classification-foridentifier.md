# classification(forIdentifier:)

**Framework**: Sound Analysis  
**Kind**: method

Returns the classification for an identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func classification(forIdentifier identifier: String) -> SNClassification?
```

#### Return Value

A sound classification with a corresponding identifier if it exists in the result; otherwise, `nil`.

#### Discussion

The `identifier` parameter corresponds to the [`identifier`](snclassification/identifier.md) property in an [`SNClassification`](snclassification.md).

## Parameters

- `identifier`: A sound classification label.

## See Also

- [var timeRange: CMTimeRange](snclassificationresult/timerange.md)
  The time span that corresponds to the result’s classifications.
- [var classifications: [SNClassification]](snclassificationresult/classifications.md)
  A sorted array of the request’s top classification candidates.
- [class SNClassification](snclassification.md)
  A type that pairs a sound classifier’s prediction with its confidence in that prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassificationresult/classification(foridentifier:))*