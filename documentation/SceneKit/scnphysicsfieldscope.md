# SCNPhysicsFieldScope

**Framework**: SceneKit  
**Kind**: enum

Options for defining the region of space affected by a physics field, used by the [`scope`](scnphysicsfield/scope.md) property.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum SCNPhysicsFieldScope
```

#### Overview

You define a region of space for a field using the position of the node containing the field and the field’s [`halfExtent`](scnphysicsfield/halfextent.md) and [`usesEllipsoidalExtent`](scnphysicsfield/usesellipsoidalextent.md) properties. Then, you use the [`scope`](scnphysicsfield/scope.md) property to choose whether the field’s area of effect is the interior of this region or whether it is the entirety of scene space excluding this region.

## Topics

### Constants
- [SCNPhysicsFieldScope.insideExtent](scnphysicsfieldscope/insideextent.md)
  The field’s effect applies only to objects within the region of space defined by its position and extent.
- [SCNPhysicsFieldScope.outsideExtent](scnphysicsfieldscope/outsideextent.md)
  The field’s effect applies only to objects outside the region of space defined by its position and extent.
### Initializers
- [init?(rawValue: Int)](scnphysicsfieldscope/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias SCNFieldForceEvaluator](scnfieldforceevaluator.md)
  The signature for a block that SceneKit calls to determine the effect of a custom field on an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfieldscope)*