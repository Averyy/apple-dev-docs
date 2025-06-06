# init(_:radix:uppercase:)

**Framework**: Swift  
**Kind**: init

Creates a string representing the given value in base 10, or some other specified base.

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
init<T>(_ value: T, radix: Int = 10, uppercase: Bool = false) where T : BinaryInteger
```

#### Discussion

The following example converts the maximal `Int` value to a string and prints its length:

```swift
let max = String(Int.max)
print("\(max) has \(max.count) digits.")
// Prints "9223372036854775807 has 19 digits."
```

Numerals greater than 9 are represented as Roman letters. These letters start with `"A"` if `uppercase` is `true`; otherwise, with `"a"`.

```swift
let v = 999_999
print(String(v, radix: 2))
// Prints "11110100001000111111"

print(String(v, radix: 16))
// Prints "f423f"
print(String(v, radix: 16, uppercase: true))
// Prints "F423F"
```

## Parameters

- `value`: The value to convert to a string.
- `radix`: The base to use for the string representation.   must be   at least 2 and at most 36. The default is 10.
- `uppercase`: Pass   to use uppercase letters to represent numerals   greater than 9, or   to use lowercase letters. The default is   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(_:radix:uppercase:))*