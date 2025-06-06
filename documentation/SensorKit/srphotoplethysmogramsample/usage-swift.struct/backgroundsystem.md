# backgroundSystem

**Framework**: SensorKit  
**Kind**: property

A reading taken by the system in the background.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
static let backgroundSystem: SRPhotoplethysmogramSample.Usage
```

#### Discussion

The system takes this reading while performing various heart features on watchOS — such as background blood oxygen, atrial fibrillation (AFib), and low-cardio notifications.

## See Also

- [static let foregroundHeartRate: SRPhotoplethysmogramSample.Usage](srphotoplethysmogramsample/usage-swift.struct/foregroundheartrate.md)
  A heart rate reading that a person takes while using an app.
- [static let deepBreathing: SRPhotoplethysmogramSample.Usage](srphotoplethysmogramsample/usage-swift.struct/deepbreathing.md)
  A deep breathing sensor reading that a person takes while using an app.
- [static let foregroundBloodOxygen: SRPhotoplethysmogramSample.Usage](srphotoplethysmogramsample/usage-swift.struct/foregroundbloodoxygen.md)
  A blood oxygen reading that a person takes while using an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.struct/backgroundsystem)*