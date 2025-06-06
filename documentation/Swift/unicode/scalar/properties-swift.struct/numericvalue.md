# numericValue

**Framework**: Swift  
**Kind**: property

The numeric value of the scalar.

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
var numericValue: Double? { get }
```

#### Discussion

For scalars that represent a numeric value, `numericValue` is the whole or fractional value. For all other scalars, this property is `nil`.

```swift
let scalars: [Unicode.Scalar] = ["4", "④", "⅕", "X"]
for scalar in scalars {
    print(scalar, "-->", scalar.properties.numericValue)
}
// 4 --> Optional(4.0)
// ④ --> Optional(4.0)
// ⅕ --> Optional(0.2)
// X --> nil
```

This property corresponds to the “Numeric_Value” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/numericvalue)*