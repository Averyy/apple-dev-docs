# Preliminary_ReferenceImage

**Framework**: RealityKit

A schema that defines the properties of an image in the physical environment.

#### Overview

This schema defines the criteria that the runtime uses to recognize an image in the physical environment, including pixel data and width.

When RealityKit opens a USDZ file that defines a reference image, it instantiates an [`AnchorEntity`](AnchorEntity.md) with a component type  [`AnchoringComponent.Target.image(group:name:)`](AnchoringComponent/Target-swift.enum/image(group:name:).md).

##### Declaration

```other
class Preliminary_ReferenceImage "Preliminary_ReferenceImage" (
    inherits = </Typed>
)
```

##### Define a Reference Image

The following example defines a prim named `ImageReference` that instructs the runtime to scan for an image described by `image.png`.

```other
def Preliminary_ReferenceImage "ImageReference"
{
    uniform asset image = @image.png@
    uniform double physicalWidth = 12
}
```

## Topics

### Properties
- [image](image.md)
  An image file for which the runtime should search.
- [physicalWidth](physicalwidth.md)
  An image’s width in centimeters.

## See Also

- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Preliminary_AnchoringAPI](preliminary-anchoringapi.md)
  A schema that defines the placement of a prim and its children at a real-world location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/preliminary-referenceimage)*