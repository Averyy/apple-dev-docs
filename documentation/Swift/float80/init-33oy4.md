# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new value, rounded to the closest possible representation.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init<Source>(_ value: Source) where Source : BinaryInteger
```

#### Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Parameters

- `value`: The integer to convert to a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(_:)-33oy4)*