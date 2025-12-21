# convert(value:from:)

**Framework**: Spatial  
**Kind**: method

Converts a value from a source coordinate space to this one.

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
func convert<T>(value: T, from targetCoordinateSpace: Self) throws -> T where T : ProjectiveTransformable3D
```

#### Return Value

The value converted from the source space to this one.

## Parameters

- `value`: The value the function converts between spaces given in reference to   the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3d/convert(value:from:)-3zi9f)*