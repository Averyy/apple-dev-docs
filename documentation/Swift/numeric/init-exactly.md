# init(exactly:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates a new instance from the given integer, if it can be represented exactly.

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
init?<T>(exactly source: T) where T : BinaryInteger
```

#### Discussion

If the value passed as `source` is not representable exactly, the result is `nil`. In the following example, the constant `x` is successfully created from a value of `100`, while the attempt to initialize the constant `y` from `1_000` fails because the `Int8` type can represent `127` at maximum:

```swift
let x = Int8(exactly: 100)
// x == Optional(100)
let y = Int8(exactly: 1_000)
// y == nil
```

## Parameters

- `source`: A value to convert to this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/numeric/init(exactly:))*