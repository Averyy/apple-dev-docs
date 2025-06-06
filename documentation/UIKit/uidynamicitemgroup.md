# UIDynamicItemGroup

**Framework**: UIKit  
**Kind**: class

A dynamic item that comprises multiple other dynamic items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDynamicItemGroup
```

#### Overview

Use groups to manipulate a group of dynamic items together and treat them as a single unit for the purpose of collisions. The group can contain dynamic items but cannot contain other [`UIDynamicItemGroup`](uidynamicitemgroup.md) objects. You can add a group to any [`UIDynamicBehavior`](uidynamicbehavior.md) object.

The attributes of the dynamic item group are derived from the items of the group itself. The group’s bounds rectangle is the rectangle that encloses all of the contained dynamic items, and the center point of the group is the center point of the bounds rectangle.

## Topics

### Initializing a group
- [init(items: [any UIDynamicItem])](uidynamicitemgroup/init(items:).md)
  Initializes and returns a group containing the specified items.
### Getting the dynamic items in a group
- [var items: [any UIDynamicItem]](uidynamicitemgroup/items.md)
  The dynamic items in the group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIDynamicItem](uidynamicitem.md)

## See Also

- [protocol UIDynamicItem](uidynamicitem.md)
  A set of methods that can make a custom object eligible to participate in UIKit Dynamics.
- [class UIDynamicItemBehavior](uidynamicitembehavior.md)
  A base dynamic animation configuration for one or more dynamic items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitemgroup)*