# convert(value:to:)

**Framework**: Spatial  
**Kind**: method

Converts a value from this coordinate space to another.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func convert<T, Space>(value: T, to targetCoordinateSpace: Space) throws -> T where T : ProjectiveTransformable3DFloat, Space : CoordinateSpace3DFloat
```

#### Return Value

The value converted to the target coordinate space.

## Parameters

- `value`: The value to convert between spaces, given in reference to   this coordinate space.
- `targetCoordinateSpace`: The coordinate space the function transforms the value to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3dfloat/convert(value:to:))*