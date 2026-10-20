# foregroundHeartRate

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A heart rate reading that a person takes while using an app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
static let foregroundHeartRate: SRPhotoplethysmogramSample.Usage
```

```c
extern SRPhotoplethysmogramSampleUsage const SRPhotoplethysmogramSampleUsageForegroundHeartRate;
```

#### Discussion

An example is a sample of a heart rate reading from a person using the Heart Rate or a workout app.

## See Also

### Getting the reading method
- [static let deepBreathing: SRPhotoplethysmogramSample.Usage](./deepbreathing.md)
  A deep breathing sensor reading that a person takes while using an app.
- [static let foregroundBloodOxygen: SRPhotoplethysmogramSample.Usage](./foregroundbloodoxygen.md)
  A blood oxygen reading that a person takes while using an app.
- [static let backgroundSystem: SRPhotoplethysmogramSample.Usage](./backgroundsystem.md)
  A reading taken by the system in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.struct/foregroundheartrate)*