# NSDecimalCopy(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Copies the value of a decimal number.

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
func NSDecimalCopy(_ destination: UnsafeMutablePointer<Decimal>, _ source: UnsafePointer<Decimal>)
```

```c
extern void NSDecimalCopy(NSDecimal *destination, const NSDecimal *source);
```

#### Discussion

Copies the value in `source` to `destination`.

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## Parameters

- `destination`: A [`Decimal`](./decimal.md) reference that receives the copied value.
- `source`: A source [`Decimal`](./decimal.md) to copy.

## See Also

### Creating a decimal from another decimal
- [init(signOf: Decimal, magnitudeOf: Decimal)](./decimal/init%28signof,magnitudeof%29.md)
  Creates and initializes a decimal with the sign and magnitude of the given decimals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalcopy(_:_:))*