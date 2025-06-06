# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a Unicode scalar with the specified numeric value.

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
init(_ v: UInt8)
```

#### Discussion

For example, the following code sample creates a `Unicode.Scalar` instance with a value of `"7"`:

```swift
let codepoint: UInt8 = 55
let seven = Unicode.Scalar(codepoint)
print(seven)
// Prints "7"
```

## Parameters

- `v`: The code point to use for the scalar.

## See Also

- [init(Unicode.Scalar)](unicode/scalar/init(_:)-5d6us.md)
  Creates a duplicate of the given Unicode scalar.
- [init?(UInt32)](unicode/scalar/init(_:)-9eo1y.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(UInt16)](unicode/scalar/init(_:)-18u1m.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(Int)](unicode/scalar/init(_:)-96l5f.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral: Unicode.Scalar)](unicode/scalar/init(unicodescalarliteral:).md)
  Creates a Unicode scalar with the specified value.
- [init?(String)](unicode/scalar/init(_:)-4p868.md)
  Instantiates an instance of the conforming type from a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/init(_:)-2oo2e)*