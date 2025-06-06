# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new value, rounded to the closest possible representation.

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
init<Source>(_ value: Source) where Source : BinaryInteger
```

#### Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Parameters

- `value`: The integer to convert to a floating-point value.

## See Also

- [init(Int)](float/init(_:)-6cvkq.md)
  Creates a new value, rounded to the closest possible representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(_:)-7e965)*