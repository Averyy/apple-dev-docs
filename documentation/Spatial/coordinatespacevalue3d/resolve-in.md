# resolve(in:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

Resolves the associated value in the given coordinate space.

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
func resolve<Space>(in otherSpace: Space) throws -> Self.Value where Space : CoordinateSpace3D
```

#### Return Value

A concrete value converted to the provided space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespacevalue3d/resolve(in:))*