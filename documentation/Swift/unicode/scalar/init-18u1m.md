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
init?(_ v: UInt16)
```

#### Discussion

For example, the following code sample creates a `Unicode.Scalar` instance with a value of `"밥"`, the Korean word for rice:

```swift
let codepoint: UInt16 = 48165
let bap = Unicode.Scalar(codepoint)
print(bap!)
// Prints "밥"
```

In case of an invalid input value, the result is `nil`.

```swift
let codepoint: UInt16 = extValue   // This might be an invalid value
if let bap = Unicode.Scalar(codepoint) {
    print(bap)
} else {
    // Do something else
}
```

## Parameters

- `v`: The Unicode code point to use for the scalar. The   initializer succeeds if   is a valid Unicode scalar value, in the   range   or  . If   is an invalid   unicode scalar value, the result is  .

## See Also

- [init(UInt8)](unicode/scalar/init(_:)-2oo2e.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(Unicode.Scalar)](unicode/scalar/init(_:)-5d6us.md)
  Creates a duplicate of the given Unicode scalar.
- [init?(UInt32)](unicode/scalar/init(_:)-9eo1y.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(Int)](unicode/scalar/init(_:)-96l5f.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral: Unicode.Scalar)](unicode/scalar/init(unicodescalarliteral:).md)
  Creates a Unicode scalar with the specified value.
- [init?(String)](unicode/scalar/init(_:)-4p868.md)
  Instantiates an instance of the conforming type from a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/init(_:)-18u1m)*