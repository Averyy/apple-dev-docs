# RealityViewDefaultPlaceholder

**Framework**: RealityKit  
**Kind**: struct

A view that represents the default placeholder for a RealityView.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct RealityViewDefaultPlaceholder
```

#### Overview

You don’t directly create instances of this type because [`RealityView`](realityview.md) creates them for you.

## Topics

### Instance Properties
- [var body: some View](realityviewdefaultplaceholder/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [RealityViewDefaultPlaceholder.Body](realityviewdefaultplaceholder/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](realityviewdefaultplaceholder/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct RealityView](realityview.md)
  A view that contains RealityKit content.
- [struct RealityViewContent](realityviewcontent.md)
  The content of a visionOS reality view.
- [struct RealityViewCameraContent](realityviewcameracontent.md)
  The content of a reality view that is displayed through a camera.
- [protocol RealityViewContentProtocol](realityviewcontentprotocol.md)
  A protocol representing the content of a reality view.
- [struct RealityViewEntityCollection](realityviewentitycollection.md)
  A collection of entities in a RealityView.
- [protocol EntityCollection](entitycollection.md)
  An ordered, mutable collection of entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder)*