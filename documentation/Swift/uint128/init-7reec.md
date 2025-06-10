# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new integer value from the given string.

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
init?(_ description: String)
```

#### Discussion

The string passed as `description` may begin with a plus or minus sign character (`+` or `-`), followed by one or more numeric digits (`0-9`).

```swift
let x = Int("123")
// x == 123
```

If `description` is in an invalid format, or if the value it denotes in base 10 is not representable, the result is `nil`. For example, the following conversions result in `nil`:

```swift
Int(" 100")                       // Includes whitespace
Int("21-50")                      // Invalid format
Int("ff6600")                     // Characters out of bounds
Int("10000000000000000000000000") // Out of range
```

## Parameters

- `description`: The ASCII representation of a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/init(_:)-7reec)*