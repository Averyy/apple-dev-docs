# startPoint

**Framework**: RealityKit  
**Kind**: property

The start point of the off-mesh connection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var startPoint: SIMD3<Float>
```

## See Also

- [var endPoint: SIMD3<Float>](navigationmeshresource/offmeshconnection/endpoint.md)
  The end point of the off-mesh connection.
- [var isBidirectional: Bool](navigationmeshresource/offmeshconnection/isbidirectional.md)
  Whether the connection is bidirectional. If false, pathfinds will only allow going from startPoint to endPoint. If true, pathfinds will allow going in both directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/offmeshconnection/startpoint)*