# max

**Framework**: Swift  
**Kind**: property

The maximum representable integer in this type.

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
static var max: Self { get }
```

#### Discussion

For signed integer types, this value is `(2 ** (bitWidth - 1)) - 1`, where `**` is exponentiation.

## See Also

- [static var zero: Self](int/zero.md)
  The zero value.
- [static var min: Self](int/min.md)
  The minimum representable integer in this type.
- [static var isSigned: Bool](int/issigned.md)
  A Boolean value indicating whether this type is a signed integer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/max)*