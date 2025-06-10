# cumulativeForegroundTime

**Framework**: MetricKit  
**Kind**: property

The total time the app is in the foreground.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var cumulativeForegroundTime: Measurement<UnitDuration> { get }
```

## See Also

- [var cumulativeBackgroundTime: Measurement<UnitDuration>](mxappruntimemetric/cumulativebackgroundtime.md)
  The total time the app is active in the background.
- [var cumulativeBackgroundAudioTime: Measurement<UnitDuration>](mxappruntimemetric/cumulativebackgroundaudiotime.md)
  The total time the app is in the background and playing audio.
- [var cumulativeBackgroundLocationTime: Measurement<UnitDuration>](mxappruntimemetric/cumulativebackgroundlocationtime.md)
  The total time the app is in the background and using location services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappruntimemetric/cumulativeforegroundtime)*