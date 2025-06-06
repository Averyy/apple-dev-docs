# RealityViewCameraContent.Body

**Framework**: RealityKit  
**Kind**: struct

The default view contents of a [`RealityView`](realityview.md) using [`RealityViewCameraContent`](realityviewcameracontent.md).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Body<Placeholder> where Placeholder : View
```

#### Overview

You don’t directly create instances of this type because [`RealityView`](realityview.md) creates them for you.

## Topics

### Instance Properties
- [var body: some View](realityviewcameracontent/body/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [RealityViewCameraContent.Body.Body](realityviewcameracontent/body/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](realityviewcameracontent/body/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent/body)*