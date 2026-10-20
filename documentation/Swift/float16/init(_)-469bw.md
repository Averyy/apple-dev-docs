# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance that approximates the given value.

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
init(_ other: Float)
```

#### Discussion

The value of `other` is rounded to a representable value, if necessary. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Float = 21.25
let y = Float16(x)
// y == 21.25

let z = Float16(Float.nan)
// z.isNaN == true
```

## Parameters

- `other`: The value to use for the new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/init(_:)-469bw)*