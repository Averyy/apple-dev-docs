# foregroundExitData

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The metrics for the foreground app exits.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`ForegroundTerminationMetric`](../foregroundterminationmetric.md) instead.

## Declaration

```swift
var foregroundExitData: MXForegroundExitData { get }
```

```objc
@property (strong, readonly, nonnull) MXForegroundExitData * foregroundExitData;
```

## See Also

### Reading the foreground exit data
- [class MXForegroundExitData](../mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappexitmetric/foregroundexitdata)*