# width(_:)

**Framework**: Swift  
**Kind**: method

Returns the number of code units required to encode the given Unicode scalar.

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
static func width(_ x: Unicode.Scalar) -> Int
```

#### Return Value

The width of `x` when encoded in UTF-8, from `1` to `4`.

#### Discussion

Because a Unicode scalar value can require up to 21 bits to store its value, some Unicode scalars are represented in UTF-8 by a sequence of up to 4 code units. The first code unit is designated a  byte and the rest are  bytes.

```swift
let anA: Unicode.Scalar = "A"
print(anA.value)
// Prints "65"
print(UTF8.width(anA))
// Prints "1"

let anApple: Unicode.Scalar = "🍎"
print(anApple.value)
// Prints "127822"
print(UTF8.width(anApple))
// Prints "4"
```

## Parameters

- `x`: A Unicode scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf8/width(_:))*