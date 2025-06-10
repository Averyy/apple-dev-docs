# PhotogrammetrySession.Request.modelFile(url:detail:geometry:)

**Framework**: RealityKit  
**Kind**: case

An object-creation request saved to a USDZ file or a folder (for OBJ output).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case modelFile(url: URL, detail: PhotogrammetrySession.Request.Detail = .reduced, geometry: PhotogrammetrySession.Request.Geometry? = nil)
```

## Parameters

- `url`: The location URL in the file system where you want to save the model file.   The request saves a USDZ file if the   ends with  .   If   refers to a directory, the request saves an OBJ object and every texture map there.
- `detail`: The level of detail for the created model.
- `geometry`: The bounding box or transforms for the generated object.

## See Also

- [case modelEntity(detail: PhotogrammetrySession.Request.Detail, geometry: PhotogrammetrySession.Request.Geometry?)](photogrammetrysession/request/modelentity(detail:geometry:).md)
  An object-creation request stored in-memory for immediate display.
- [PhotogrammetrySession.Request.bounds](photogrammetrysession/request/bounds.md)
  An object-creation request that returns a box the same size as the created model.
- [PhotogrammetrySession.Request.Detail](photogrammetrysession/request/detail.md)
  Supported levels of detail for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/modelfile(url:detail:geometry:))*