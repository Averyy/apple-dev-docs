# properties

**Framework**: Swift  
**Kind**: property

Properties of this scalar defined by the Unicode standard.

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
var properties: Unicode.Scalar.Properties { get }
```

#### Discussion

Use this property to access the Unicode properties of a Unicode scalar value. The following code tests whether a string contains any math symbols:

```swift
let question = "Which is larger, 3 * 3 * 3 or 10 + 10 + 10?"
let hasMathSymbols = question.unicodeScalars.contains(where: {
    $0.properties.isMath
})
// hasMathSymbols == true
```

## See Also

- [var value: UInt32](unicode/scalar/value.md)
  A numeric representation of the Unicode scalar.
- [Unicode.Scalar.Properties](unicode/scalar/properties-swift.struct.md)
  A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.
- [func hash(into: inout Hasher)](unicode/scalar/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var isASCII: Bool](unicode/scalar/isascii.md)
  A Boolean value indicating whether the Unicode scalar is an ASCII character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.property)*