# NSDecimalNumberHandler

**Framework**: Foundation  
**Kind**: class

A class that adopts the decimal number behaviors protocol.

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
class NSDecimalNumberHandler
```

#### Overview

This class allows you to set the way an [`NSDecimalNumber`](nsdecimalnumber.md) object rounds off and handles errors, without having to create a custom class.

You can use an instance of this class as an argument to any of the [`NSDecimalNumber`](nsdecimalnumber.md) methods that end with `...Behavior:`. If you don’t think you need special behavior, you probably don’t need this class—it is likely that [`NSDecimalNumber`](nsdecimalnumber.md)’s default behavior will suit your needs.

For more information, see the [`NSDecimalNumberBehaviors`](nsdecimalnumberbehaviors.md) protocol specification.

## Topics

### Creating a Decimal Number Handler
- [class var `default`: NSDecimalNumberHandler](nsdecimalnumberhandler/default.md)
  Returns the default instance of `NSDecimalNumberHandler`.
### Initializing a decimal number handler
- [init(roundingMode: NSDecimalNumber.RoundingMode, scale: Int16, raiseOnExactness: Bool, raiseOnOverflow: Bool, raiseOnUnderflow: Bool, raiseOnDivideByZero: Bool)](nsdecimalnumberhandler/init(roundingmode:scale:raiseonexactness:raiseonoverflow:raiseonunderflow:raiseondividebyzero:).md)
  Returns an `NSDecimalNumberHandler` object initialized so it behaves as specified by the method’s arguments.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSDecimalNumberBehaviors](nsdecimalnumberbehaviors.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var roundingBehavior: NSDecimalNumberHandler](numberformatter/roundingbehavior.md)
  The rounding behavior used by the receiver.
- [var roundingIncrement: NSNumber!](numberformatter/roundingincrement.md)
  The rounding increment used by the receiver.
- [var roundingMode: NumberFormatter.RoundingMode](numberformatter/roundingmode-swift.property.md)
  The rounding mode used by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumberhandler)*