# ==(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether the two given values are equal.

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
static func == <Other>(lhs: Self, rhs: Other) -> Bool where Other : BinaryInteger
```

#### Discussion

You can check the equality of instances of any `BinaryInteger` types using the equal-to operator (`==`). For example, you can test whether the first `UInt8` value in a string’s UTF-8 encoding is equal to the first `UInt32` value in its Unicode scalar view:

```swift
let gameName = "Red Light, Green Light"
if let firstUTF8 = gameName.utf8.first,
    let firstScalar = gameName.unicodeScalars.first?.value {
    print("First code values are equal: \(firstUTF8 == firstScalar)")
}
// Prints "First code values are equal: true"
```

## Parameters

- `lhs`: An integer to compare.
- `rhs`: Another integer to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8/==(_:_:)-exky)*