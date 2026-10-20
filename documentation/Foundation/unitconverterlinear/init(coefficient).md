# init(coefficient:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the unit converter with the coefficient you specify.

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
convenience init(coefficient: Double)
```

```objc
- (instancetype) initWithCoefficient:(double) coefficient;
```

#### Return Value

A unit converter initialized with the specified coefficient.

#### Discussion

Calling this initializer is equivalent to calling [`init(coefficient:constant:)`](./init%28coefficient,constant%29.md), passing `0` for the `constant` parameter.

## Parameters

- `coefficient`: The coefficient used in the linear unit conversion calculation.

## See Also

### Creating Unit Converters
- [init(coefficient: Double, constant: Double)](./init%28coefficient,constant%29.md)
  Creates a unit converter with the coefficient and constant you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitconverterlinear/init(coefficient:))*