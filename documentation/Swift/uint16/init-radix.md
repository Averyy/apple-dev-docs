# init(_:radix:)

**Framework**: Swift  
**Kind**: init

Creates a new integer value from the given string and radix.

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
init?<S>(_ text: S, radix: Int = 10) where S : StringProtocol
```

#### Discussion

The string passed as `text` may begin with a plus or minus sign character (`+` or `-`), followed by one or more numeric digits (`0-9`) or letters (`a-z` or `A-Z`). Parsing of the string is case insensitive.

```swift
let x = Int("123")
// x == 123

let y = Int("-123", radix: 8)
// y == -83
let y = Int("+123", radix: 8)
// y == +83

let z = Int("07b", radix: 16)
// z == 123
```

If `text` is in an invalid format or contains characters that are out of bounds for the given `radix`, or if the value it denotes in the given `radix` is not representable, the result is `nil`. For example, the following conversions result in `nil`:

```swift
Int(" 100")                       // Includes whitespace
Int("21-50")                      // Invalid format
Int("ff6600")                     // Characters out of bounds
Int("zzzzzzzzzzzzz", radix: 36)   // Out of range
```

## Parameters

- `text`: The ASCII representation of a number in the radix passed as   .
- `radix`: The radix, or base, to use for converting   to an integer   value.   must be in the range  . The default is 10.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint16/init(_:radix:))*