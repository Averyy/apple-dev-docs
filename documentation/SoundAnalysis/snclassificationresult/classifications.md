# classifications

**Framework**: Sound Analysis  
**Kind**: property

A sorted array of the request’s top classification candidates.

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
var classifications: [SNClassification] { get }
```

#### Discussion

`SNClassificationResult` sorts its classifications in descending confidence score order.

## See Also

- [var timeRange: CMTimeRange](snclassificationresult/timerange.md)
  The time span that corresponds to the result’s classifications.
- [class SNClassification](snclassification.md)
  A type that pairs a sound classifier’s prediction with its confidence in that prediction.
- [func classification(forIdentifier: String) -> SNClassification?](snclassificationresult/classification(foridentifier:).md)
  Returns the classification for an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassificationresult/classifications)*