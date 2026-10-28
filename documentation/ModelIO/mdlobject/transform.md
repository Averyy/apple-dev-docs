# transform

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

A component that manages this object’s spatial transform and its changes over time.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var transform: (any MDLTransformComponent)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MDLTransformComponent> transform;
```

## Discussion

A transform defines the local coordinate space for an object’s content—that is, its position, orientation, shear, and scale—relative to the coordinate space of the object’s parent. The [`MDLTransformComponent`](../mdltransformcomponent.md) protocol defines a general interface for objects that manage transforms, including time-based transform information for assets that include animation data. By default, Model I/O uses the [`MDLTransform`](../mdltransform.md) object for this property; however, you can also use a custom class that adopts the [`MDLTransformComponent`](../mdltransformcomponent.md) protocol to support alternative ways of calculating or storing transform data.

> **Note**:  Reading or writing this property is equivalent to calling the [`componentConforming(to:)`](./componentconforming%28to%29.md) or [`setComponent(_:for:)`](./setcomponent%28_,for%29.md) method with the [`MDLTransformComponent`](../mdltransformcomponent.md) protocol.

## See Also

### Working with Objects in Space
- [func boundingBox(atTime: TimeInterval) -> MDLAxisAlignedBoundingBox](./boundingbox%28attime%29.md)
  Returns the minimum region entirely enclosing the object’s contents at the specified time sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/transform)*