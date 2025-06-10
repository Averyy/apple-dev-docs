# convert(value:from:)

**Framework**: Spatial  
**Kind**: method

Converts a value from a source coordinate space to this one.

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
func convert<T, Space>(value: T, from sourceCoordinateSpace: Space) throws -> T where T : ProjectiveTransformable3DFloat, Space : CoordinateSpace3DFloat
```

#### Return Value

The value converted from the source space to this one.

## Parameters

- `value`: The value the function converts between spaces given in reference to   the  .
- `sourceCoordinateSpace`: The coordinate space the value is provided   in reference to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3dfloat/convert(value:from:))*