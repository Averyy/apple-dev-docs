# Padding

**Framework**: MapKit JS  
**Kind**: class

The values that define content padding within the map view frame.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class Padding
```

#### Overview

Use padding to define edge insets on the map. MapKit JS then uses these insets when it positions items on the map, such as the map controls or annotations. For example, if you want to add your own control on top of the map and ensure that the map doesn’t position annotations underneath it, you can add padding to the map and then position your control within the padded area.

You can use a [`Padding`](padding.md) object when setting the map’s [`padding`](map/padding.md) property or as an option of [`showItems(items, options)`](map/showitems.md). Positive values add padding to the inside edges of the map. MapKit JS clips negative values to `0`.

## Topics

### Creating padding
- [new Padding()](padding/paddingconstructor.md)
  Creates a padding object with no inset margins.
- [new Padding(paddings)](padding/paddingconstructor1.md)
  Creates a padding object and initializes its values with the provided object literal.
- [new Padding(top)](padding/paddingconstructor2.md)
  Creates a padding object and initializes its top inset margin with the provided value.
- [new Padding(top, right)](padding/paddingconstructor3.md)
  Creates a padding object and initializes it with the provided top and right side values.
- [new Padding(top, right, bottom)](padding/paddingconstructor4.md)
  Creates a padding object and initializes it with the provided top, right, and bottom values.
- [new Padding(top, right, bottom, left)](padding/paddingconstructor5.md)
  Creates a padding object and initializes it with the provided values.
- [interface PaddingConstructorOptions](paddingconstructoroptions.md)
  Initial values of the edge insets for padding.
### Controlling the map’s padding
- [bottom](padding/bottom.md)
  The amount of padding, in CSS pixels, to inset the map from the bottom edge.
- [left](padding/left.md)
  The amount of padding, in CSS pixels, to inset the map from the left edge.
- [right](padding/right.md)
  The amount of padding, in CSS pixels, to inset the map from the right edge.
- [top](padding/top.md)
  The amount of padding, in CSS pixels, to inset the map from the top edge.
### Variables
- [Zero](padding/zero.md)
  An object that represents zero padding values.
### Instance Methods
- [copy()](padding/copy.md)
  Returns a copy of the padding object.
- [equals(anotherPadding)](padding/equals.md)
  Compares whether two padding values are equal.
- [toString()](padding/tostring.md)
  Returns a string representation of the padding object.

## See Also

- [const FeatureVisibility](featurevisibility.md)
  Constants indicating the visibility of different adaptive map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/padding)*