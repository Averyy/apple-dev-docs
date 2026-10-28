# HKCorrelationTypeIdentifier

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

The identifiers that create correlation type objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
struct HKCorrelationTypeIdentifier
```

```c
typedef NSString * HKCorrelationTypeIdentifier;
```

## Overview

To create an [`HKCorrelationType`](./hkcorrelationtype.md) instance, pass an [`HKCorrelationTypeIdentifier`](./hkcorrelationtypeidentifier.md) value to the [`correlationType(forIdentifier:)`](./hkobjecttype/correlationtype%28foridentifier%29.md) method.

## Topics

### Correlation Types
- [static let bloodPressure: HKCorrelationTypeIdentifier](./hkcorrelationtypeidentifier/bloodpressure.md)
  A correlation sample that combines a systolic sample and a diastolic sample into a single blood pressure reading.
- [static let food: HKCorrelationTypeIdentifier](./hkcorrelationtypeidentifier/food.md)
  Food correlation types combine any number of nutritional samples into a single food object.
### Initializers
- [init(rawValue: String)](./hkcorrelationtypeidentifier/init%28rawvalue%29.md)
  Returns a newly initialized correlation type identifier using the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating correlation types
- [class func correlationType(forIdentifier: HKCorrelationTypeIdentifier) -> HKCorrelationType?](./hkobjecttype/correlationtype%28foridentifier%29.md)
  Returns the shared correlation type for the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelationtypeidentifier)*