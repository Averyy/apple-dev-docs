# init(nan:signaling:)

**Framework**: Swift  
**Kind**: init

Creates a NaN (“not a number”) value with the specified payload.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(nan payload: Float16.RawSignificand, signaling: Bool)
```

#### Discussion

NaN values compare not equal to every value, including themselves. Most operations with a NaN operand produce a NaN result. Don’t use the equal-to operator (`==`) to test whether a value is NaN. Instead, use the value’s `isNaN` property.

```swift
let x = Float16(nan: 0, signaling: false)
print(x == .nan)
// Prints "false"
print(x.isNaN)
// Prints "true"
```

## Parameters

- `payload`: The payload to use for the new NaN value.
- `signaling`: Pass   to create a signaling NaN or   to create   a quiet NaN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/init(nan:signaling:))*