# NSDecimalNumber

**Framework**: Foundation  
**Kind**: class

An object for representing and performing arithmetic on base-10 numbers.

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
class NSDecimalNumber
```

#### Overview

In Swift, this object bridges to [`Decimal`](decimal.md); use [`NSDecimalNumber`](nsdecimalnumber.md) when you need reference semantics or other Foundation-specific behavior.

`NSDecimalNumber`, an immutable subclass of `NSNumber`, provides an object-oriented wrapper for doing base-10 arithmetic. An instance can represent any number that can be expressed as `mantissa x 10^exponent` where mantissa is a decimal integer up to 38 digits long, and exponent is an integer from –128 through 127.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Decimal`](decimal.md) structure, which bridges to the [`NSDecimalNumber`](nsdecimalnumber.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating a Decimal Number
- [class var one: NSDecimalNumber](nsdecimalnumber/one.md)
  A decimal number equivalent to the number 1.0.
- [class var zero: NSDecimalNumber](nsdecimalnumber/zero.md)
  A decimal number equivalent to the number 0.0.
- [class var notANumber: NSDecimalNumber](nsdecimalnumber/notanumber.md)
  A decimal number that specifies no number.
### Initializing a Decimal Number
- [init(decimal: Decimal)](nsdecimalnumber/init(decimal:).md)
  Initializes a decimal number to represent a given decimal.
- [convenience init(mantissa: UInt64, exponent: Int16, isNegative: Bool)](nsdecimalnumber/init(mantissa:exponent:isnegative:).md)
  Initializes a decimal number using the given mantissa, exponent, and sign.
- [convenience init(string: String?)](nsdecimalnumber/init(string:).md)
  Initializes a decimal number so that its value is equivalent to that in a given numeric string.
- [convenience init(string: String?, locale: Any?)](nsdecimalnumber/init(string:locale:).md)
  Initializes a decimal number so that its value is equivalent to that in a given numeric string, interpreted using a given locale.
### Performing Arithmetic
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
- [func multiplying(by: NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/multiplying(by:withbehavior:).md)
  Multiplies this number by another given number using the specified behavior.
- [func dividing(by: NSDecimalNumber, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/dividing(by:withbehavior:).md)
  Divides this number by another given number using the specified behavior.
- [func raising(toPower: Int, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/raising(topower:withbehavior:).md)
  Raises the number to a given power using the specified behavior.
- [func multiplying(byPowerOf10: Int16, withBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/multiplying(bypowerof10:withbehavior:).md)
  Multiplies the number by 10 raised to the given power using the specified behavior.
### Rounding Off
- [func rounding(accordingToBehavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber](nsdecimalnumber/rounding(accordingtobehavior:).md)
  Returns a rounded version of the decimal number using the specified rounding behavior.
### Managing Behavior
- [class var defaultBehavior: any NSDecimalNumberBehaviors](nsdecimalnumber/defaultbehavior.md)
  The way arithmetic methods round off and handle error conditions.
- [protocol NSDecimalNumberBehaviors](nsdecimalnumberbehaviors.md)
  A protocol that declares three methods that control the discretionary aspects of working with decimal numbers.
- [class NSDecimalNumberHandler](nsdecimalnumberhandler.md)
  A class that adopts the decimal number behaviors protocol.
### Accessing the Value
- [var decimalValue: Decimal](nsdecimalnumber/decimalvalue.md)
  The decimal number’s value, expressed as an [`Decimal`](decimal.md) structure.
- [var doubleValue: Double](nsdecimalnumber/doublevalue.md)
  The decimal number’s closest approximate `double` value.
- [func description(withLocale: Any?) -> String](nsdecimalnumber/description(withlocale:).md)
  Returns a string representation of the decimal number appropriate for the specified locale.
- [var objCType: UnsafePointer<CChar>](nsdecimalnumber/objctype.md)
  A C string containing the Objective-C type for the data contained in the decimal number object.
### Comparing Decimal Numbers
- [func compare(NSNumber) -> ComparisonResult](nsdecimalnumber/compare(_:).md)
  Compares this decimal number and another.
### Getting Maximum and Minimum Possible Values
- [class var maximum: NSDecimalNumber](nsdecimalnumber/maximum.md)
  Returns the largest possible value of a decimal number.
- [class var minimum: NSDecimalNumber](nsdecimalnumber/minimum.md)
  Returns the smallest possible value of a decimal number.
### Recognizing Exceptions
- [static let decimalNumberExactnessException: NSExceptionName](nsexceptionname/decimalnumberexactnessexception.md)
  The exception raised if there is an exactness error.
- [static let decimalNumberOverflowException: NSExceptionName](nsexceptionname/decimalnumberoverflowexception.md)
  The exception raised on overflow.
- [static let decimalNumberUnderflowException: NSExceptionName](nsexceptionname/decimalnumberunderflowexception.md)
  The exception raised on underflow.
- [static let decimalNumberDivideByZeroException: NSExceptionName](nsexceptionname/decimalnumberdividebyzeroexception.md)
  The exception raised on divide by zero.

## Relationships

### Inherits From
- [NSNumber](nsnumber.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByBooleanLiteral](../Swift/ExpressibleByBooleanLiteral.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber)*