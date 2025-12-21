# BindPath.Part.scene(_:)

**Framework**: RealityKit  
**Kind**: case

A path component for a nested scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
case scene(String)
```

#### Discussion

This path component indicates that another component follows, and at the same time specifies the entity, scene, or property that animates.

Because no path contains nested scenes, this component exists only as the first element of a multicomponent path.

## See Also

- [BindPath.Part.anchorEntity(_:)](bindpath/part/anchorentity(_:).md)
  A path component for the scene’s anchor entity.
- [BindPath.Part.entity(_:)](bindpath/part/entity(_:).md)
  A path component for a nested entity.
- [BindPath.Part.jointTransforms](bindpath/part/jointtransforms.md)
  A path component to animate joint transforms.
- [BindPath.Part.parameter(_:)](bindpath/part/parameter(_:).md)
  A path component to animate a named parameter.
- [BindPath.Part.transform](bindpath/part/transform.md)
  A path component to animate a transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindpath/part/scene(_:))*