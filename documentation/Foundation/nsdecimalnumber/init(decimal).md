# init(decimal:)

**Framework**: Foundation  
**Kind**: init

Initializes a decimal number to represent a given decimal.

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
init(decimal dcm: Decimal)
```

#### Return Value

An `NSDecimalNumber` object initialized to represent `dcm`.

#### Discussion

This method is the designated initializer for `NSDecimalNumber`.

## Parameters

- `dcm`: The value of the new object.

## See Also

- [convenience init(mantissa: UInt64, exponent: Int16, isNegative: Bool)](nsdecimalnumber/init(mantissa:exponent:isnegative:).md)
  Initializes a decimal number using the given mantissa, exponent, and sign.
- [convenience init(string: String?)](nsdecimalnumber/init(string:).md)
  Initializes a decimal number so that its value is equivalent to that in a given numeric string.
- [convenience init(string: String?, locale: Any?)](nsdecimalnumber/init(string:locale:).md)
  Initializes a decimal number so that its value is equivalent to that in a given numeric string, interpreted using a given locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/init(decimal:))*