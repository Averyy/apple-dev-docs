# levelsOfDetail

**Framework**: SceneKit  
**Kind**: property

An array of [`SCNLevelOfDetail`](scnlevelofdetail.md) objects for managing the geometry’s appearance when viewed from far away.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var levelsOfDetail: [SCNLevelOfDetail]? { get set }
```

#### Discussion

Because rendering a complex geometry incurs a performance cost, you can use level-of-detail objects to substitute simpler geometries in its place as its distance from the point of view camera increases (or its apparent size decreases). For details, see [`SCNLevelOfDetail`](scnlevelofdetail.md).

## See Also

- [class SCNLevelOfDetail](scnlevelofdetail.md)
  An alternate resolution for a geometry that SceneKit automatically substitutes to improve rendering performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/levelsofdetail)*