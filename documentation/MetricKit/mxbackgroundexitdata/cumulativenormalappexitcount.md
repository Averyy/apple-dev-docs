# cumulativeNormalAppExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the app exited normally from the background.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`normalTerminationCount`](../backgroundterminationmetric/normalterminationcount.md) instead.

## Declaration

```swift
var cumulativeNormalAppExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeNormalAppExitCount;
```

## Discussion

Normal exits include terminations by the app switcher when the user swipes up to exit the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativenormalappexitcount)*