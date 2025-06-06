# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance from the given string.

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
init?<S>(_ text: S) where S : StringProtocol
```

#### Discussion

The string passed as `text` can represent a real number in decimal or hexadecimal format or can be in a special format representing infinity or NaN (“not a number”). If `text` is not in a recognized format, the optional initializer will fail and return `nil`.

The `text` string consists of an optional plus or minus sign character (`+` or `-`) followed by one of the following:

- A  contains a significand consisting of one or more decimal digits that may include a decimal point: ```swift
let c = Double("-1.0")
// c == -1.0

let d = Double("28.375")
// d == 28.375
``` A decimal string may also include an exponent following the significand, indicating the power of 10 by which the significand should be multiplied. If included, the exponent is separated by a single character, `e` or `E`, and consists of an optional plus or minus sign character and a sequence of decimal digits. ```swift
let e = Double("2837.5e-2")
// e == 28.375
```
- A  contains a significand consisting of `0X` or `0x` followed by one or more hexadecimal digits that may include a decimal point. ```swift
let f = Double("0x1c.6")
// f == 28.375
``` A hexadecimal string may also include an exponent indicating the power of 2 by which the significand should be multiplied. If included, the exponent is separated by a single character, `p` or `P`, and consists of an optional plus or minus sign character and a sequence of decimal digits. ```swift
let g = Double("0x1.c6p4")
// g == 28.375
```
- The input strings `"inf"` or `"infinity"` (case insensitive) are converted to an infinite result: ```swift
let i = Double("inf")
// i == Double.infinity

let j = Double("-Infinity")
// j == -Double.infinity
```
- An input string of `"nan"` (case insensitive) is converted into a  value: ```swift
let n = Double("-nan")
// n?.isNaN == true
// n?.sign == .minus
``` A NaN string may also include a payload in parentheses following the `"nan"` keyword. The payload consists of a sequence of decimal digits, or the characters `0X` or `0x` followed by a sequence of hexadecimal digits. If the payload contains any other characters, it is ignored. If the value of the payload is larger than can be stored as the payload of a `Double.nan`, the least significant bits are used. ```swift
let p = Double("nan(0x10)")
// p?.isNaN == true
// String(p!) == "nan(0x10)"
```

A string in any other format than those described above or containing additional characters results in a `nil` value. For example, the following conversions result in `nil`:

```swift
  Double(" 5.0")      // Includes whitespace
  Double("±2.0")      // Invalid character
  Double("0x1.25e4")  // Incorrect exponent format
```

A decimal or hexadecimal string is converted to a `Double` instance using the IEEE 754 roundTiesToEven (default) rounding attribute. Values with absolute value smaller than `Double.leastNonzeroMagnitude` are rounded to plus or minus zero. Values with absolute value larger than `Double.greatestFiniteMagnitude` are rounded to plus or minus infinity.

```swift
  let y = Double("1.23e-9999")
  // y == 0.0
  // y?.sign == .plus

  let z = Double("-7.89e-7206")
  // z == -0.0
  // z?.sign == .minus

  let r = Double("1.23e17802")
  // r == Double.infinity

  let s = Double("-7.89e7206")
  // s == Double.-infinity
```

> **Note**: Prior to Swift 5.4, a decimal or hexadecimal input string whose value was too large to represent as a finite `Double` instance returned `nil` instead of `Double.infinity`.

## Parameters

- `text`: An input string to convert to a   instance.

## See Also

- [init?(Substring)](double/init(_:)-15kej.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(_:)-5wmm8)*