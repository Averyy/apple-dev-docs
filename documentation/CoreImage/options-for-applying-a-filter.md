# Options for Applying a Filter

**Framework**: Core Image

Options that control the application of a custom Core Image filter.

#### Overview

Use these constants only when creating a custom filter for which you are writing the kernel. For more information, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185). The example on creating a custom filter shows how to use these options.

## Topics

### Constants
- [let kCIApplyOptionExtent: String](kciapplyoptionextent.md)
  The extent of the image.
- [let kCIApplyOptionDefinition: String](kciapplyoptiondefinition.md)
  The domain of definition (DOD) of the produced image.
- [let kCIApplyOptionUserInfo: String](kciapplyoptionuserinfo.md)
  Information needed by a callback. The associated value is an object that Core Image will pass to any callbacks invoked for that filter.
- [let kCIApplyOptionColorSpace: String](kciapplyoptioncolorspace.md)
  The color space of the produced image.

## See Also

- [Filter Attribute Keys](filter-attribute-keys.md)
  Attributes for a filter and its parameters.
- [Data Type Attributes](data-type-attributes.md)
  Numeric data types.
- [Vector Quantity Attributes](vector-quantity-attributes.md)
  Vector data types.
- [Color Attribute Keys](color-attribute-keys.md)
  Color types.
- [Image Attribute Keys](image-attribute-keys.md)
  Image Types
- [Filter Category Keys](filter-category-keys.md)
  Categories of filters.
- [User Interface Control Options](user-interface-control-options.md)
  Sets of controls for various user scenarios.
- [User Interface Options](user-interface-options.md)
  Keys or values for the size of the input parameter controls for a filter view.
- [Filter Parameter Keys](filter-parameter-keys.md)
  Keys for input parameters to filters.
- [RAW Image Options](raw-image-options.md)
  Options for creating a [`CIFilter`](cifilter-swift.class.md) object from RAW image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/options-for-applying-a-filter)*