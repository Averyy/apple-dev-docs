# multiplying(by:withBehavior:)

**Framework**: Foundation  
**Kind**: method

Multiplies this number by another given number using the specified behavior.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func multiplying(by decimalNumber: NSDecimalNumber, withBehavior behavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber
```

#### Discussion

`behavior` specifies the handling of calculation errors and rounding.

## See Also

- [func adding(NSDecimalNumber) -> NSDecimalNumber](nsdecimalnumber/adding(_:).md)
  Adds this number to another given number.
- [func subtracting(NSDecimalNumber) -> NSDecimalNumber](nsdecimalnumber/subtracting(_:).md)
  Subtracts another given number from this one.
- [func multiplying(by: NSDecimalNumber) -> NSDecimalNumber](nsdecimalnumber/multiplying(by:).md)
  Multiplies the number by another given number.
- [func dividing(by: NSDecimalNumber) -> NSDecimalNumber](nsdecimalnumber/dividing(by:).md)
  Divides the number by another given number.
- [func raising(toPower: Int) -> NSDecimalNumber](nsdecimalnumber/raising(topower:).md)
  Raises the number to a given power.
- [func multiplying(byPowerOf10: Int16) -> NSDecimalNumber](nsdecimalnumber/multiplying(bypowerof10:).md)
  Multiplies the number by 10 raised to the given power.
- [func adding(NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/adding(_:withbehavior:).md)
  Adds this number to another given number using the specified behavior.
- [func subtracting(NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/subtracting(_:withbehavior:).md)
  Subtracts this a given number from this one using the specified behavior.
- [func dividing(by: NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/dividing(by:withbehavior:).md)
  Divides this number by another given number using the specified behavior.
- [func raising(toPower: Int, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/raising(topower:withbehavior:).md)
  Raises the number to a given power using the specified behavior.
- [func multiplying(byPowerOf10: Int16, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/multiplying(bypowerof10:withbehavior:).md)
  Multiplies the number by 10 raised to the given power using the specified behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/multiplying(by:withbehavior:))*