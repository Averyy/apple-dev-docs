# timeRange

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The time range in the audio stream that the level applies to.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

```objc
@property (nonatomic, assign, readonly) CMTimeRange timeRange;
```

## See Also

### Getting metrics
- [var loudness: Double](./loudness.md)
  The measure of the audio level in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/sraudiolevel/timerange)*