# SCNScene.Attribute

**Framework**: SceneKit  
**Kind**: struct

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
struct Attribute
```

## Topics

### Type Properties
- [static let endTime: SCNScene.Attribute](scnscene/attribute/endtime.md)
- [static let frameRate: SCNScene.Attribute](scnscene/attribute/framerate.md)
  A floating-point value for the frame rate of the scene.
- [static let startTime: SCNScene.Attribute](scnscene/attribute/starttime.md)
- [static let upAxis: SCNScene.Attribute](scnscene/attribute/upaxis.md)
  An `SCNVector3` structure specifying the orientation of the scene.
### Initializers
- [init(rawValue: String)](scnscene/attribute/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func attribute(forKey: String) -> Any?](scnscene/attribute(forkey:).md)
  Returns the scene attribute for the specified key.
- [func setAttribute(Any?, forKey: String)](scnscene/setattribute(_:forkey:).md)
  Sets a scene attribute for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/attribute)*