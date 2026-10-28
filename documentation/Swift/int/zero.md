# zero

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

The zero value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var zero: Self { get }
```

Available when `Self` conforms to `ExpressibleByIntegerLiteral`.

## Discussion

Zero is the identity element for addition. For any value, `x + .zero == x` and `.zero + x == x`.

## See Also

### Accessing Numeric Constants
- [static var min: Self](./min.md)
  The minimum representable integer in this type.
- [static var max: Self](./max.md)
  The maximum representable integer in this type.
- [static var isSigned: Bool](./issigned.md)
  A Boolean value indicating whether this type is a signed integer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/zero)*