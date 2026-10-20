# maximumScore

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The highest score of all exposures for this item.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var maximumScore: Double { get }
```

```objc
@property (nonatomic, assign, readonly) double maximumScore;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## See Also

### Getting Summary Properties
- [var scoreSum: Double](./scoresum.md)
  The sum of scores for all exposure for this item.
- [var weightedDurationSum: TimeInterval](./weighteddurationsum.md)
  The sum of exposure durations weighted by their attenuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuresummaryitem/maximumscore)*