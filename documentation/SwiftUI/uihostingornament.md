# UIHostingOrnament

**Framework**: SwiftUI  
**Kind**: class

A model that represents an ornament suitable for being hosted in UIKit.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
class UIHostingOrnament<Content> where Content : View
```

#### Overview

Use a `UIHostingOrnament` when you want to add ornaments to a UIKit view controller. For example, the following adds a single bottom ornament to the current view controller:

```swift
self.ornaments = [
    UIHostingOrnament(sceneAnchor: .bottom) {
        OrnamentContent()
    }
]
```

## Topics

### Creating a hosting ornament
- [init(sceneAnchor:contentAlignment:content:)](uihostingornament/init(sceneanchor:contentalignment:content:).md)
  Creates an ornament with the specified alignment and content.
- [var rootView: Content](uihostingornament/rootview.md)
  The root view of the SwiftUI view hierarchy managed by this ornament.
### Setting the alignment
- [var contentAlignment: Alignment](uihostingornament/contentalignment.md)
  The alignment in the ornament used to position it.
- [var sceneAnchor: UnitPoint](uihostingornament/sceneanchor.md)
  The anchor point for aligning the ornament’s content (based on the `contentAlignment`) with the scene.
### Instance Properties
- [var contentAlignment3D: Alignment3D](uihostingornament/contentalignment3d.md)

## Relationships

### Inherits From
- [UIOrnament](uiornament.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIOrnament](uiornament.md)
  The abstract base class that represents an ornament.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingornament)*