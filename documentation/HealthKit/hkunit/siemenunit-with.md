# siemenUnit(with:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring electrical conductance, using siemen units with the provided prefix.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func siemenUnit(with prefix: HKMetricPrefix) -> Self
```

#### Return Value

A HealthKit unit for measuring electrical conductance based on siemens and the provided prefix.

#### Discussion

This method is used to create prefixed versions of siemens. HealthKit often records electrodermal activity in microsiemens, as shown below.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func siemen() -> Self](hkunit/siemen.md)
  Returns a HealthKit unit for measuring electrical conductance in siemens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/siemenunit(with:))*