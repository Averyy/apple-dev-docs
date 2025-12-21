# SCNSceneSourceStatus.validating

**Framework**: SceneKit  
**Kind**: case

SceneKit has begun validating the scene file’s format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case validating
```

#### Discussion

If you specify [`true`](https://developer.apple.com/documentation/Swift/true) for the [`checkConsistency`](scnscenesource/loadingoption/checkconsistency.md) when creating or loading from a scene source, SceneKit verifies the scene file against the specification for its file format and reports any format consistency errors.

## See Also

- [SCNSceneSourceStatus.error](scnscenesourcestatus/error.md)
  An error occurred when SceneKit attempted to load the scene.
- [SCNSceneSourceStatus.parsing](scnscenesourcestatus/parsing.md)
  SceneKit has begun deserializing the source file.
- [SCNSceneSourceStatus.processing](scnscenesourcestatus/processing.md)
  SceneKit has begun generating scene graph objects from the scene file’s contents.
- [SCNSceneSourceStatus.complete](scnscenesourcestatus/complete.md)
  SceneKit has successfully finished loading the scene file’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesourcestatus/validating)*