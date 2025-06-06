# BodyTrackingComponent.Target

**Framework**: RealityKit  
**Kind**: enum

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
- [BodyTrackingComponent.Target.any](bodytrackingcomponent/target-swift.enum/any.md)
  Any person that is detected in front of the camera.
- [BodyTrackingComponent.Target.body(identifier:)](bodytrackingcomponent/target-swift.enum/body(identifier:).md)
  A person detected by ARKit.
### Comparing targets
- [static func == (BodyTrackingComponent.Target, BodyTrackingComponent.Target) -> Bool](bodytrackingcomponent/target-swift.enum/==(_:_:).md)
  Indicates whether two targets are equal.
- [static func != (Self, Self) -> Bool](bodytrackingcomponent/target-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](bodytrackingcomponent/target-swift.enum/hash(into:).md)
  Hashes the essential components of the target by feeding them into the given hash function.
- [var hashValue: Int](bodytrackingcomponent/target-swift.enum/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](bodytrackingcomponent/target-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var target: BodyTrackingComponent.Target](bodytrackingcomponent/target-swift.property.md)
  The body-tracking setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bodytrackingcomponent/target-swift.enum)*