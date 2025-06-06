# RealityViewContent.Body

**Framework**: RealityKit  
**Kind**: struct

The default view contents of a reality view, using reality view content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Body<Placeholder> where Placeholder : View
```

#### Overview

You don’t create this type directly. [`RealityView`](realityview.md) creates values for you.

## Topics

### Instance Properties
- [var body: some View](realityviewcontent/body/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [RealityViewContent.Body.Body](realityviewcontent/body/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](realityviewcontent/body/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontent/body)*