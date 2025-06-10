# customDetailSpecification

**Framework**: RealityKit  
**Kind**: property

Defines custom detail level specifications for a photogrammetry session with custom detail level.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var customDetailSpecification: PhotogrammetrySession.Configuration.CustomDetailSpecification
```

#### Discussion

This property configures the characteristics of the model’s precision and characteristics, such as texture size and the types of texture maps.

> ❗ **Important**: The system checks this property only when processing a request with the [`PhotogrammetrySession.Request.Detail.custom`](photogrammetrysession/request/detail/custom.md) detail set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.property)*