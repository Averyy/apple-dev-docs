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

The width of `x` when encoded in UTF-16, either `1` or `2`.

#### Discussion

Because a Unicode scalar value can require up to 21 bits to store its value, some Unicode scalars are represented in UTF-16 by a pair of 16-bit code units. The first and second code units of the pair, designated  and  surrogates, make up a .

```swift
let anA: Unicode.Scalar = "A"
print(anA.value)
// Prints "65"
print(UTF16.width(anA))
// Prints "1"

let anApple: Unicode.Scalar = "🍎"
print(anApple.value)
// Prints "127822"
print(UTF16.width(anApple))
// Prints "2"
```

## Parameters

- `x`: A Unicode scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf16/width(_:))*