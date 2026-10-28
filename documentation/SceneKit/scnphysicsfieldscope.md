# SCNPhysicsFieldScope

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Options for defining the region of space affected by a physics field, used by the [`scope`](./scnphysicsfield/scope.md) property.

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
enum SCNPhysicsFieldScope
```

```c
enum SCNPhysicsFieldScope : NSInteger;
```

## Overview

You define a region of space for a field using the position of the node containing the field and the field’s [`halfExtent`](./scnphysicsfield/halfextent.md) and [`usesEllipsoidalExtent`](./scnphysicsfield/usesellipsoidalextent.md) properties. Then, you use the [`scope`](./scnphysicsfield/scope.md) property to choose whether the field’s area of effect is the interior of this region or whether it is the entirety of scene space excluding this region.

## Topics

### Constants
- [SCNPhysicsFieldScope.insideExtent](./scnphysicsfieldscope/insideextent.md)
  The field’s effect applies only to objects within the region of space defined by its position and extent.
- [SCNPhysicsFieldScope.outsideExtent](./scnphysicsfieldscope/outsideextent.md)
  The field’s effect applies only to objects outside the region of space defined by its position and extent.
### Initializers
- [init?(rawValue: Int)](./scnphysicsfieldscope/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [typealias SCNFieldForceEvaluator](./scnfieldforceevaluator.md)
  The signature for a block that SceneKit calls to determine the effect of a custom field on an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfieldscope)*