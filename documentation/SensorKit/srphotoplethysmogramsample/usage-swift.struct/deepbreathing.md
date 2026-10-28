# deepBreathing

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A deep breathing sensor reading that a person takes while using an app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
static let deepBreathing: SRPhotoplethysmogramSample.Usage
```

```c
extern SRPhotoplethysmogramSampleUsage const SRPhotoplethysmogramSampleUsageDeepBreathing;
```

## Discussion

An example is a sample of a reading from a person performing a reflect or breathe session in the Mindfulness app.

## See Also

### Getting the reading method
- [static let foregroundHeartRate: SRPhotoplethysmogramSample.Usage](./foregroundheartrate.md)
  A heart rate reading that a person takes while using an app.
- [static let foregroundBloodOxygen: SRPhotoplethysmogramSample.Usage](./foregroundbloodoxygen.md)
  A blood oxygen reading that a person takes while using an app.
- [static let backgroundSystem: SRPhotoplethysmogramSample.Usage](./backgroundsystem.md)
  A reading taken by the system in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.struct/deepbreathing)*