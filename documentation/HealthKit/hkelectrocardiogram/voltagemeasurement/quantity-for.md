# quantity(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the voltage for the specified lead.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func quantity(for lead: HKElectrocardiogram.Lead) -> HKQuantity?
```

#### Return Value

A quantity object containing a value in volt units. These values are compatible with any units created using [`voltUnit(with:)`](hkunit/voltunit(with:).md).

## Parameters

- `lead`: The lead whose voltage you want to read.

## See Also

- [var timeSinceSampleStart: TimeInterval](hkelectrocardiogram/voltagemeasurement/timesincesamplestart.md)
  The time of the measurement relative to the sample’s start time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/voltagemeasurement/quantity(for:))*