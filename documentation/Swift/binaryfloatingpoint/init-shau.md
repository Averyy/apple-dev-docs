# init(_:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates a new instance from the given value, rounded to the closest possible representation.

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
init<Source>(_ value: Source) where Source : BinaryFloatingPoint
```

#### Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Parameters

- `value`: A floating-point value to be converted.

## See Also

- [init(Float)](binaryfloatingpoint/init(_:)-57jx7.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Double)](binaryfloatingpoint/init(_:)-7ft14.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Float80)](binaryfloatingpoint/init(_:)-1nijh.md)
  Creates a new instance from the given value, rounded to the closest possible representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(_:)-shau)*