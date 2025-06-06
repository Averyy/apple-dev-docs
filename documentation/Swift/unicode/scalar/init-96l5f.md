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
init?(_ v: Int)
```

#### Discussion

For example, the following code sample creates a `Unicode.Scalar` instance with a value of an emoji character:

```swift
let codepoint = 127881
let emoji = Unicode.Scalar(codepoint)!
print(emoji)
// Prints "🎉"
```

In case of an invalid input value, nil is returned.

```swift
let codepoint: UInt32 = extValue // This might be an invalid value.
if let emoji = Unicode.Scalar(codepoint) {
  print(emoji)
} else {
  // Do something else
}
```

## Parameters

- `v`: The Unicode code point to use for the scalar.   must be   a valid Unicode scalar value, in the ranges   or   . In case of an invalid unicode scalar value, nil is   returned.

## See Also

- [init(UInt8)](unicode/scalar/init(_:)-2oo2e.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(Unicode.Scalar)](unicode/scalar/init(_:)-5d6us.md)
  Creates a duplicate of the given Unicode scalar.
- [init?(UInt32)](unicode/scalar/init(_:)-9eo1y.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(UInt16)](unicode/scalar/init(_:)-18u1m.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral: Unicode.Scalar)](unicode/scalar/init(unicodescalarliteral:).md)
  Creates a Unicode scalar with the specified value.
- [init?(String)](unicode/scalar/init(_:)-4p868.md)
  Instantiates an instance of the conforming type from a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/init(_:)-96l5f)*