# levelsOfDetail

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An array of [`SCNLevelOfDetail`](../scnlevelofdetail.md) objects for managing the geometry’s appearance when viewed from far away.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var levelsOfDetail: [SCNLevelOfDetail]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<SCNLevelOfDetail *> * levelsOfDetail;
```

#### Discussion

Because rendering a complex geometry incurs a performance cost, you can use level-of-detail objects to substitute simpler geometries in its place as its distance from the point of view camera increases (or its apparent size decreases). For details, see [`SCNLevelOfDetail`](../scnlevelofdetail.md).

## See Also

### Optimizing Level of Detail
- [class SCNLevelOfDetail](../scnlevelofdetail.md)
  An alternate resolution for a geometry that SceneKit automatically substitutes to improve rendering performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/levelsofdetail)*