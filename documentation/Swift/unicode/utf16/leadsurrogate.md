# leadSurrogate(_:)

**Framework**: Swift  
**Kind**: method

Returns the high-surrogate code unit of the surrogate pair representing the specified Unicode scalar.

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
static func leadSurrogate(_ x: Unicode.Scalar) -> UTF16.CodeUnit
```

#### Return Value

The leading surrogate code unit of `x` when encoded in UTF-16.

#### Discussion

Because a Unicode scalar value can require up to 21 bits to store its value, some Unicode scalars are represented in UTF-16 by a pair of 16-bit code units. The first and second code units of the pair, designated *leading* and *trailing* surrogates, make up a *surrogate pair*.

```swift
let apple: Unicode.Scalar = "🍎"
print(UTF16.leadSurrogate(apple))
// Prints "55356"
```

## Parameters

- `x`: A Unicode scalar value. `x` must be represented by a surrogate pair when encoded in UTF-16. To check whether `x` is represented by a surrogate pair, use `UTF16.width(x) == 2`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf16/leadsurrogate(_:))*