# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance initialized to the given value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(_ other: Float80)
```

#### Discussion

The value of `other` is represented exactly by the new instance. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Float80 = 21.25
let y = Float80(x)
// y == 21.25

let z = Float80(Float80.nan)
// z.isNaN == true
```

## Parameters

- `other`: The value to use for the new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(_:)-6dyii)*