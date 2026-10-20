# SCNScene.Attribute

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

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
struct Attribute
```

```c
typedef NSString * SCNSceneAttribute;
```

## Topics

### Type Properties
- [static let endTime: SCNScene.Attribute](./attribute/endtime.md)
- [static let frameRate: SCNScene.Attribute](./attribute/framerate.md)
  A floating-point value for the frame rate of the scene.
- [static let startTime: SCNScene.Attribute](./attribute/starttime.md)
- [static let upAxis: SCNScene.Attribute](./attribute/upaxis.md)
  An `SCNVector3` structure specifying the orientation of the scene.
### Initializers
- [init(rawValue: String)](./attribute/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Scene Attributes
- [func attribute(forKey: String) -> Any?](./attribute%28forkey%29.md)
  Returns the scene attribute for the specified key.
- [func setAttribute(Any?, forKey: String)](./setattribute%28_,forkey%29.md)
  Sets a scene attribute for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/attribute)*