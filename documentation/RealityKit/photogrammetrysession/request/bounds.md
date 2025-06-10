# PhotogrammetrySession.Request.bounds

**Framework**: RealityKit  
**Kind**: case

An object-creation request that returns a box the same size as the created model.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case bounds
```

#### Discussion

Use a `bounds` request to quickly retrieve a box the same size as the final created object.

## See Also

- [case modelFile(url: URL, detail: PhotogrammetrySession.Request.Detail, geometry: PhotogrammetrySession.Request.Geometry?)](photogrammetrysession/request/modelfile(url:detail:geometry:).md)
  An object-creation request saved to a USDZ file or a folder (for OBJ output).
- [case modelEntity(detail: PhotogrammetrySession.Request.Detail, geometry: PhotogrammetrySession.Request.Geometry?)](photogrammetrysession/request/modelentity(detail:geometry:).md)
  An object-creation request stored in-memory for immediate display.
- [PhotogrammetrySession.Request.Detail](photogrammetrysession/request/detail.md)
  Supported levels of detail for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/bounds)*