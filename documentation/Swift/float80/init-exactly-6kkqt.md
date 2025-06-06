# init(exactly:)

**Framework**: Swift  
**Kind**: init

Creates a new instance initialized to the given value, if it can be represented without rounding.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init?(exactly other: Float)
```

#### Discussion

If `other` can’t be represented as an instance of `Float80` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float = 21.25
let y = Float80(exactly: x)
// y == Optional.some(21.25)

let z = Float80(exactly: Float.nan)
// z == nil
```

## Parameters

- `other`: The value to use for the new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(exactly:)-6kkqt)*