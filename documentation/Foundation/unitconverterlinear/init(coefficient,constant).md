# init(coefficient:constant:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a unit converter with the coefficient and constant you specify.

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
init(coefficient: Double, constant: Double)
```

```objc
- (instancetype) initWithCoefficient:(double) coefficient constant:(double) constant;
```

## Parameters

- `coefficient`: The coefficient used in the linear unit conversion calculation.
- `constant`: The constant used in the linear unit conversion calculation.

## See Also

### Creating Unit Converters
- [convenience init(coefficient: Double)](./init%28coefficient%29.md)
  Initializes the unit converter with the coefficient you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitconverterlinear/init(coefficient:constant:))*