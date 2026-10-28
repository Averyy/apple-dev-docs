# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer  
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

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Parameters

- `value`: A floating-point value to be converted.

## Default Implementations

### BinaryFloatingPoint Implementations
- [init<Source>(Source)](./init%28_%29-17tah.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init<Source>(Source)](./init%28_%29-5p0og.md)
  Creates a new value, rounded to the closest possible representation.

## See Also

### Converting Floating-Point Values
- [init(Float)](./init%28_%29-57jx7.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Double)](./init%28_%29-7ft14.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Float80)](./init%28_%29-1nijh.md)
  Creates a new instance from the given value, rounded to the closest possible representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(_:)-shau)*