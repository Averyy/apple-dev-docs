# PresentationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that presents a SwiftUI modal presentation from a RealityKit entity.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct PresentationComponent
```

#### Overview

Popovers that this component presents initially rotate themselves to face the active camera and appear with a breakthrough effect by default. To change the breakthrough effect on the presented view, use the `presentationBreakthroughEffect` modifier, like in the following example:

```None
var presentationComponent = PresentationComponent(
    configuration: .popover(arrowEdge: .bottom),
    content: PresentedView()
        .glassBackgroundEffect()
        .presentationBreakthroughEffect(.prominent)
)
```

For presentations that opt out of breakthrough effects, consider applying breakthrough effects to the main elements of the view, to ensure that the occluding content doesn’t clip the content within the presentation:

```None
HStack {
    Text(title)
        .breakthroughEffect(.subtle)

    Button(action: action, label: label)
        .breakthroughEffect(.subtle)
}
.glassBackgroundEffect()
.presentationBreakthroughEffect(.none)
```

To make the presentation continuously face the active camera, add a [`BillboardComponent`](billboardcomponent.md) to the same entity that contains the `PresentationComponent`:

```None
entity.add(presentationComponent)
entity.add(BillboardComponent())
```

> **Note**: For an example of breakthrough effects on presentations, see [`Canyon Crosser: Building a volumetric hike-planning app`](https://developer.apple.com/documentation/visionos/canyon-crosser-building-a-volumetric-hike-planning-app).

## Topics

### Structures
- [PresentationComponent.Configuration](presentationcomponent/configuration.md)
  A configuration that specifies the modality, appearance, and behavior of the presentation.
### Initializers
- [init<Content>(configuration: PresentationComponent.Configuration, content: Content)](presentationcomponent/init(configuration:content:).md)
  Present `content` using modality and options specified by `configuration`. A component created using this method will have its `isPresented` property default to `true`, which means it will present as soon as an entity with the component is added to the hierarchy.
- [init<Content>(isPresented: Binding<Bool>, configuration: PresentationComponent.Configuration, content: Content)](presentationcomponent/init(ispresented:configuration:content:).md)
  Present `content` when a binding that you provide is `true`, using modality and options specified by `configuration`.
### Instance Properties
- [var isPresented: Bool](presentationcomponent/ispresented.md)
  A boolean value that indicates whether the content is presented.

## Relationships

### Conforms To
- [Component](component.md)
- [TransientComponent](transientcomponent.md)

## See Also

- [struct RealityViewAttachmentBuilderContent](realityviewattachmentbuildercontent.md)
  A view that gathers the attachment content for your current reality view.
- [struct Attachment](attachment.md)
  An attachment content you can use to gather an identifier and view.
- [struct RealityViewAttachments](realityviewattachments.md)
  The attachments that belong to a RealityView.
- [class ViewAttachmentEntity](viewattachmententity.md)
  An entity that has a view attachment.
- [struct ViewAttachmentComponent](viewattachmentcomponent.md)
  A component containing additional information about a view attachment entity provided  via the [`entity(for:)`](realityviewattachments/entity(for:).md) function.
- [struct TextComponent](textcomponent.md)
  A component that draws 2D text at an entity’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/presentationcomponent)*