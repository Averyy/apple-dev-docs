# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

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
init?(_ v: UInt32)
```

## Discussion

For example, the following code sample creates a `Unicode.Scalar` instance with a value of an emoji character:

```swift
let codepoint: UInt32 = 127881
let emoji = Unicode.Scalar(codepoint)
print(emoji!)
// Prints "🎉"
```

In case of an invalid input value, nil is returned.

```swift
let codepoint: UInt32 = extValue   // This might be an invalid value
if let emoji = Unicode.Scalar(codepoint) {
  print(emoji)
} else {
  // Do something else
}
```

## Parameters

- `v`: The Unicode code point to use for the scalar. The initializer succeeds if `v` is a valid Unicode scalar value—that is, if `v` is in the range `0...0xD7FF` or `0xE000...0x10FFFF`. If `v` is an invalid Unicode scalar value, the result is `nil`.

## See Also

### Creating a Scalar
- [init(UInt8)](./init%28_%29-2oo2e.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(Unicode.Scalar)](./init%28_%29-5d6us.md)
  Creates a duplicate of the given Unicode scalar.
- [init?(UInt16)](./init%28_%29-18u1m.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(Int)](./init%28_%29-96l5f.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral: Unicode.Scalar)](./init%28unicodescalarliteral%29.md)
  Creates a Unicode scalar with the specified value.
- [init?(String)](./init%28_%29-4p868.md)
  Instantiates an instance of the conforming type from a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/init(_:)-9eo1y)*