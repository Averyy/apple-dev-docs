# string(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates and returns a localized string representation of the provided measurement.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func string(from measurement: Measurement<Unit>) -> String
```

```objc
- (NSString *) stringFromMeasurement:(NSMeasurement *) measurement;
```

#### Return Value

A user-readable string that represents the measurement.

## Parameters

- `measurement`: The measurement to be represented.

## See Also

### Converting Measurements
- [func string<UnitType>(from: Measurement<UnitType>) -> String](./string%28from%29-6rcb1.md)
  Creates and returns a localized string representation of the provided measurement.
- [func string(from: Unit) -> String](./string%28from%29-4hwjz.md)
  Creates and returns a localized string representation of the provided unit of measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter/string(from:)-wt9y)*