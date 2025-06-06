# init(unicodeScalarLiteral:)

**Framework**: Swift  
**Kind**: init

Creates a Unicode scalar with the specified value.

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
init(unicodeScalarLiteral value: Unicode.Scalar)
```

#### Discussion

Do not call this initializer directly. It may be used by the compiler when you use a string literal to initialize a `Unicode.Scalar` instance.

```swift
let letterK: Unicode.Scalar = "K"
print(letterK)
// Prints "K"
```

In this example, the assignment to the `letterK` constant is handled by this initializer behind the scenes.

## See Also

- [init(UInt8)](unicode/scalar/init(_:)-2oo2e.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(Unicode.Scalar)](unicode/scalar/init(_:)-5d6us.md)
  Creates a duplicate of the given Unicode scalar.
- [init?(UInt32)](unicode/scalar/init(_:)-9eo1y.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(UInt16)](unicode/scalar/init(_:)-18u1m.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(Int)](unicode/scalar/init(_:)-96l5f.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(String)](unicode/scalar/init(_:)-4p868.md)
  Instantiates an instance of the conforming type from a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/init(unicodescalarliteral:))*