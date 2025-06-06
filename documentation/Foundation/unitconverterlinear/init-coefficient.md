# init(coefficient:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

A unit converter initialized with the specified coefficient.

#### Discussion

Calling this initializer is equivalent to calling [`init(coefficient:constant:)`](unitconverterlinear/init(coefficient:constant:).md), passing `0` for the `constant` parameter.

## Parameters

- `coefficient`: The coefficient used in the linear unit conversion calculation.

## See Also

- [init(coefficient: Double, constant: Double)](unitconverterlinear/init(coefficient:constant:).md)
  Creates a unit converter with the coefficient and constant you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitconverterlinear/init(coefficient:))*