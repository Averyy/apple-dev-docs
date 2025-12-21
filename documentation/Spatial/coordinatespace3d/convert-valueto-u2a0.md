# convert(value:to:)

**Framework**: Spatial  
**Kind**: method

Converts a value from this coordinate space to another.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func convert<T>(value: T, to targetCoordinateSpace: Self) throws -> T where T : ProjectiveTransformable3D
```

#### Return Value

The value converted to the target coordinate space.

## Parameters

- `value`: The value the function converts between spaces, given in reference to   this coordinate space.
- `targetCoordinateSpace`: The coordinate space that the function transforms the value to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3d/convert(value:to:)-u2a0)*