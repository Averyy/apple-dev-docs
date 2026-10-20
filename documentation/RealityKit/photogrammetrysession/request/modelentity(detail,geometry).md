# PhotogrammetrySession.Request.modelEntity(detail:geometry:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

An object-creation request stored in-memory for immediate display.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case modelEntity(detail: PhotogrammetrySession.Request.Detail = .reduced, geometry: PhotogrammetrySession.Request.Geometry? = nil)
```

## Parameters

- `detail`: The level of detail for the created model.
- `geometry`: The bounding box and transforms for the entity the request generates.

## See Also

### Specifying the output
- [case modelFile(url: URL, detail: PhotogrammetrySession.Request.Detail, geometry: PhotogrammetrySession.Request.Geometry?)](./modelfile%28url,detail,geometry%29.md)
  An object-creation request saved to a USDZ file or a folder (for OBJ output).
- [PhotogrammetrySession.Request.bounds](./bounds.md)
  An object-creation request that returns a box the same size as the created model.
- [PhotogrammetrySession.Request.Detail](./detail.md)
  Supported levels of detail for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/modelentity(detail:geometry:))*