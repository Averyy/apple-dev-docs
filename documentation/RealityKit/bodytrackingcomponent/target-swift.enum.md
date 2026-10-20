# BodyTrackingComponent.Target

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Body-tracking settings for selecting a person to track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Target
```

## Topics

### Body tracking target types
- [BodyTrackingComponent.Target.any](./target-swift.enum/any.md)
  Any person that is detected in front of the camera.
- [BodyTrackingComponent.Target.body(identifier:)](./target-swift.enum/body%28identifier%29.md)
  A person detected by ARKit.
### Operators
- [static func == (BodyTrackingComponent.Target, BodyTrackingComponent.Target) -> Bool](./target-swift.enum/eqeq%28_,_%29.md)
  Indicates whether two targets are equal.
### Instance Methods
- [func hash(into: inout Hasher)](./target-swift.enum/hash%28into%29.md)
  Hashes the essential components of the target by feeding them into the given hash function.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Selecting a body to track
- [var target: BodyTrackingComponent.Target](./target-swift.property.md)
  The body-tracking setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bodytrackingcomponent/target-swift.enum)*