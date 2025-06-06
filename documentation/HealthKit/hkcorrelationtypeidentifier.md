# HKCorrelationTypeIdentifier

**Framework**: HealthKit  
**Kind**: struct

The identifiers that create correlation type objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct HKCorrelationTypeIdentifier
```

#### Overview

To create an [`HKCorrelationType`](hkcorrelationtype.md) instance, pass an [`HKCorrelationTypeIdentifier`](hkcorrelationtypeidentifier.md) value to the [`correlationType(forIdentifier:)`](hkobjecttype/correlationtype(foridentifier:).md) method.

## Topics

### Correlation Types
- [static let bloodPressure: HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier/bloodpressure.md)
  A correlation sample that combines a systolic sample and a diastolic sample into a single blood pressure reading.
- [static let food: HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier/food.md)
  Food correlation types combine any number of nutritional samples into a single food object.
### Initializers
- [init(rawValue: String)](hkcorrelationtypeidentifier/init(rawvalue:).md)
  Returns a newly initialized correlation type identifier using the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func correlationType(forIdentifier: HKCorrelationTypeIdentifier) -> HKCorrelationType?](hkobjecttype/correlationtype(foridentifier:).md)
  Returns the shared correlation type for the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelationtypeidentifier)*