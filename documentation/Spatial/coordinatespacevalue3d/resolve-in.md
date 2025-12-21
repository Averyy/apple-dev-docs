# resolve(in:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

Resolves the associated value in the given coordinate space.

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
func resolve<Space>(in otherSpace: Space) throws -> Self.Value where Space : CoordinateSpace3D
```

#### Return Value

A concrete value converted to the provided space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespacevalue3d/resolve(in:))*