# classifications

**Framework**: Sound Analysis  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSArray<SNClassification *> * classifications;
```

## Discussion

`SNClassificationResult` sorts its classifications in descending confidence score order.

## See Also

### Inspecting the Result
- [var timeRange: CMTimeRange](./timerange.md)
  The time span that corresponds to the result’s classifications.
- [class SNClassification](../snclassification.md)
  A type that pairs a sound classifier’s prediction with its confidence in that prediction.
- [func classification(forIdentifier: String) -> SNClassification?](./classification%28foridentifier%29.md)
  Returns the classification for an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassificationresult/classifications)*