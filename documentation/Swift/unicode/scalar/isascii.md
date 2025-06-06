# isASCII

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the Unicode scalar is an ASCII character.

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
var isASCII: Bool { get }
```

#### Discussion

ASCII characters have a scalar value between 0 and 127, inclusive. For example:

```swift
let canyon = "Cañón"
for scalar in canyon.unicodeScalars {
    print(scalar, scalar.isASCII, scalar.value)
}
// Prints "C true 67"
// Prints "a true 97"
// Prints "ñ false 241"
// Prints "ó false 243"
// Prints "n true 110"
```

## See Also

- [var value: UInt32](unicode/scalar/value.md)
  A numeric representation of the Unicode scalar.
- [var properties: Unicode.Scalar.Properties](unicode/scalar/properties-swift.property.md)
  Properties of this scalar defined by the Unicode standard.
- [Unicode.Scalar.Properties](unicode/scalar/properties-swift.struct.md)
  A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.
- [func hash(into: inout Hasher)](unicode/scalar/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/isascii)*