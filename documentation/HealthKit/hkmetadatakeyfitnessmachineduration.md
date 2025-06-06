# HKMetadataKeyFitnessMachineDuration

**Framework**: HealthKit  
**Kind**: var

The workout duration displayed by a connected GymKit fitness machine.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let HKMetadataKeyFitnessMachineDuration: String
```

#### Discussion

Set this key on a workout sample representing exercise on a GymKit fitness machine. Set its value to an [`HKQuantity`](hkquantity.md) object with a time unit.

## See Also

- [let HKMetadataKeyCrossTrainerDistance: String](hkmetadatakeycrosstrainerdistance.md)
  The workout distance displayed by a connected GymKit cross-trainer machine.
- [let HKMetadataKeyIndoorBikeDistance: String](hkmetadatakeyindoorbikedistance.md)
  The workout distance displayed by a connected GymKit exercise bike.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyfitnessmachineduration)*