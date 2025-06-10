# ENVariantOfConcernType

**Framework**: Exposure Notification  
**Kind**: enum

A set of user-definable types that indicate variants of concern.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+

## Declaration

```swift
enum ENVariantOfConcernType
```

#### Overview

A Public Health Authority (PHA) defines the meaning of the types that indicate variants of concern. For example, a PHA could define the meaning of [`ENVariantOfConcernType.type1`](envariantofconcerntype/type1.md) as “Vaccine is effective”, and [`ENVariantOfConcernType.type2`](envariantofconcerntype/type2.md) as “Highly transmissive.” The PHA could assign the definition of “High severity” to [`ENVariantOfConcernType.type3`](envariantofconcerntype/type3.md), and “Vaccine breakthrough” to [`ENVariantOfConcernType.type4`](envariantofconcerntype/type4.md).

## Topics

### User-Defined Types
- [ENVariantOfConcernType.type1](envariantofconcerntype/type1.md)
  The first user-definable type for a variant of concern.
- [ENVariantOfConcernType.type2](envariantofconcerntype/type2.md)
  The second user-definable type for a variant of concern.
- [ENVariantOfConcernType.type3](envariantofconcerntype/type3.md)
  The third user-definable type for a variant of concern.
- [ENVariantOfConcernType.type4](envariantofconcerntype/type4.md)
  The fourth user-definable type for a variant of concern.
- [ENVariantOfConcernType.typeUnknown](envariantofconcerntype/typeunknown.md)
  The unknown type for a variant of concern.
### Initializers
- [init?(rawValue: UInt32)](envariantofconcerntype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var calibrationConfidence: ENCalibrationConfidence](enexposurewindow/calibrationconfidence.md)
  The transmitting device’s calibration confidence.
- [var date: Date](enexposurewindow/date.md)
  The date that the exposure occurred.
- [var diagnosisReportType: ENDiagnosisReportType](enexposurewindow/diagnosisreporttype.md)
  The report type of the observed diagnosis.
- [var infectiousness: ENInfectiousness](enexposurewindow/infectiousness.md)
  How infectious the user is, based on the number of days since the onset of symptoms.
- [var scanInstances: [ENScanInstance]](enexposurewindow/scaninstances.md)
  An array of scans corresponding to a beacon associated with an exposure.
- [var variantOfConcernType: ENVariantOfConcernType](enexposurewindow/variantofconcerntype.md)
  The variant of concern associated with this user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/envariantofconcerntype)*