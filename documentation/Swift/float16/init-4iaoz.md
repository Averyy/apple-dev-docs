# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new value, rounded to the closest possible representation.

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
init(_ v: Int)
```

#### Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/init(_:)-4iaoz)*