# numericType

**Framework**: Swift  
**Kind**: property

The numeric type of the scalar.

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
var numericType: Unicode.NumericType? { get }
```

#### Discussion

For scalars that represent a number, `numericType` is the numeric type of the scalar. For all other scalars, this property is `nil`.

```swift
let scalars: [Unicode.Scalar] = ["4", "④", "⅕", "X"]
for scalar in scalars {
    print(scalar, "-->", scalar.properties.numericType)
}
// 4 --> Optional(Swift.Unicode.NumericType.decimal)
// ④ --> Optional(Swift.Unicode.NumericType.digit)
// ⅕ --> Optional(Swift.Unicode.NumericType.numeric)
// X --> nil
```

This property corresponds to the “Numeric_Type” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/numerictype)*