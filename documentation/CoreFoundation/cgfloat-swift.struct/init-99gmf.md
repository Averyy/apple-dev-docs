# init(_:)

**Framework**: Core Foundation  
**Kind**: init

Creates a new value, rounded to the closest possible representation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 2.0+
- Swift ?+

## Declaration

```swift
init(_ number: NSNumber)
```

#### Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Parameters

- `number`: The number to convert to a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgfloat-swift.struct/init(_:)-99gmf)*