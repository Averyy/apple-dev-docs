# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

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
init(_ value: Int)
```

#### Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Parameters

- `value`: The integer to convert to a floating-point value.

## Default Implementations

### BinaryFloatingPoint Implementations
- [init<Source>(Source)](../binaryfloatingpoint/init%28_%29-17tah.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init<Source>(Source)](../binaryfloatingpoint/init%28_%29-5p0og.md)
  Creates a new value, rounded to the closest possible representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/init(_:)-2xwlo)*