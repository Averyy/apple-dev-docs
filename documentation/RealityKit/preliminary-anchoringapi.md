# Preliminary_AnchoringAPI

**Framework**: RealityKit

A schema that defines the placement of a prim and its children at a real-world location.

#### Overview

Use this schema to attach prims to real-world areas in an AR experience, such as surfaces, images, or faces. In non-AR viewers like studio mode in AR Quick Look, the runtime displays a prim by applying its  –– that is, its position, rotation, and scale –– relative to the center of the view.

> **Note**:  Although ARKit features the ability to recognize predefined real-world objects (see [`ARReferenceObject`](https://developer.apple.com/documentation/ARKit/ARReferenceObject)), and location anchors (see [`ARGeoAnchor`](https://developer.apple.com/documentation/ARKit/ARGeoAnchor)), the [`Preliminary_AnchoringAPI`](preliminary-anchoringapi.md) schema doesn’t support object or location anchors.

 Although ARKit features the ability to recognize predefined real-world objects (see [`ARReferenceObject`](https://developer.apple.com/documentation/ARKit/ARReferenceObject)), and location anchors (see [`ARGeoAnchor`](https://developer.apple.com/documentation/ARKit/ARGeoAnchor)), the [`Preliminary_AnchoringAPI`](preliminary-anchoringapi.md) schema doesn’t support object or location anchors.

##### Declaration

```other
class "Preliminary_AnchoringAPI"
(
    inherits = </APISchemaBase>
)
```

##### Nest and Layer Anchorable Prims

When you assign this schema to a nested prim, the runtime positions the nested prim independently by not basing the child’s transform relative to its parent. As a result, the anchorable child is effectively out of the parent’s hierarchy. Similarly, if an asset defines one or more anchorable prims layered beneath another anchorable prim, the runtime positions each prim independently. However, any unanchorable children of an anchorable prim remain positioned relative to their parent.

Since the runtime doesn’t observe anchorable prim hierarchies, you need to define all anchorable prims at the root of the document, thus, without a parent.

## Topics

### Properties
- [preliminary:anchoring:type](preliminary-anchoring-type.md)
  A option that specifies the type of anchor.
- [preliminary:planeAnchoring:alignment](preliminary-planeanchoring-alignment.md)
  An option that specifies the orientation of a plane.
- [preliminary:imageAnchoring:referenceImage](preliminary-imageanchoring-referenceimage.md)
  The characteristics of an image the runtime should scan for in order to attach a prim.

## See Also

- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Preliminary_ReferenceImage](preliminary-referenceimage.md)
  A schema that defines the properties of an image in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/preliminary-anchoringapi)*