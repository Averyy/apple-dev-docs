# NSDecimalCopy(_:_:)

**Framework**: Foundation  
**Kind**: func

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

#### Discussion

Copies the value in `source` to `destination`.

For more information, see [`Number and Value Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## Parameters

- `destination`: A   reference that receives the copied value.
- `source`: A source   to copy.

## See Also

- [init(signOf: Decimal, magnitudeOf: Decimal)](decimal/init(signof:magnitudeof:).md)
  Creates and initializes a decimal with the sign and magnitude of the given decimals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalcopy(_:_:))*