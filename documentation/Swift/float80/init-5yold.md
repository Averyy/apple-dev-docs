# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance from the given value, rounded to the closest possible representation.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init<Source>(_ value: Source) where Source : BinaryFloatingPoint
```

#### Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Parameters

- `value`: A floating-point value to be converted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(_:)-5yold)*