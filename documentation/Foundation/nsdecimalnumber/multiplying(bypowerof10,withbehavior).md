# multiplying(byPowerOf10:withBehavior:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Multiplies the number by 10 raised to the given power using the specified behavior.

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
func multiplying(byPowerOf10 power: Int16, withBehavior behavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber
```

```objc
- (NSDecimalNumber *) decimalNumberByMultiplyingByPowerOf10:(short) power withBehavior:(id<NSDecimalNumberBehaviors>) behavior;
```

#### Discussion

`behavior` specifies the handling of calculation errors and rounding.

## See Also

### Performing Arithmetic
- [func adding(NSDecimalNumber) -> NSDecimalNumber](./adding%28_%29.md)
  Adds this number to another given number.
- [func subtracting(NSDecimalNumber) -> NSDecimalNumber](./subtracting%28_%29.md)
  Subtracts another given number from this one.
- [func multiplying(by: NSDecimalNumber) -> NSDecimalNumber](./multiplying%28by%29.md)
  Multiplies the number by another given number.
- [func dividing(by: NSDecimalNumber) -> NSDecimalNumber](./dividing%28by%29.md)
  Divides the number by another given number.
- [func raising(toPower: Int) -> NSDecimalNumber](./raising%28topower%29.md)
  Raises the number to a given power.
- [func multiplying(byPowerOf10: Int16) -> NSDecimalNumber](./multiplying%28bypowerof10%29.md)
  Multiplies the number by 10 raised to the given power.
- [func adding(NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](./adding%28_,withbehavior%29.md)
  Adds this number to another given number using the specified behavior.
- [func subtracting(NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](./subtracting%28_,withbehavior%29.md)
  Subtracts this a given number from this one using the specified behavior.
- [func multiplying(by: NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](./multiplying%28by,withbehavior%29.md)
  Multiplies this number by another given number using the specified behavior.
- [func dividing(by: NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](./dividing%28by,withbehavior%29.md)
  Divides this number by another given number using the specified behavior.
- [func raising(toPower: Int, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](./raising%28topower,withbehavior%29.md)
  Raises the number to a given power using the specified behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/multiplying(bypowerof10:withbehavior:))*