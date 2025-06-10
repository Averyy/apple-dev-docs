# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new value, rounded to the closest possible representation.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(_ v: Int)
```

#### Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(_:)-42n91)*