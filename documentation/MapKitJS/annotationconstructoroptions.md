# AnnotationConstructorOptions

**Framework**: MapKit JS  
**Kind**: struct

An object that contains options for creating annotation features.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface AnnotationConstructorOptions
```

#### Overview

Use [`AnnotationConstructorOptions`](annotationconstructoroptions.md) when you need to create a custom view to provide features beyond those that the [`ImageAnnotation`](imageannotation.md) object provides.

## Topics

### Creating data and titles
- [data](annotationconstructoroptions/data.md)
  Data that you define and assign to the annotation.
- [title](annotationconstructoroptions/title.md)
  The text to display in the annotation’s callout.
- [subtitle](annotationconstructoroptions/subtitle.md)
  The text to display as a subtitle on the second line of an annotation’s callout.
- [accessibilityLabel](annotationconstructoroptions/accessibilitylabel.md)
  Accessibility text for the annotation.
### Setting position and appearances
- [anchorOffset](annotationconstructoroptions/anchoroffset.md)
  The offset, in CSS pixels, of the element from the bottom center.
- [appearanceAnimation](annotationconstructoroptions/appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [displayPriority](annotationconstructoroptions/displaypriority.md)
  A hint the map uses to prioritize displaying the annotation.
- [padding](annotationconstructoroptions/padding.md)
  Spacing to add around the annotation when showing items.
- [size](annotationconstructoroptions/size.md)
  The desired dimensions of the annotation, in CSS pixels.
- [visible](annotationconstructoroptions/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.
### Creating interaction behavior
- [animates](annotationconstructoroptions/animates.md)
  A Boolean value that determines whether the map animates the annotation.
- [draggable](annotationconstructoroptions/draggable.md)
  A Boolean value that determines whether the user can drag the annotation.
- [enabled](annotationconstructoroptions/enabled.md)
  A Boolean value that determines whether the annotation responds to user interaction.
- [selected](annotationconstructoroptions/selected.md)
  A Boolean value that determines whether the map displays the annotation in a selected state.
- [place](annotationconstructoroptions/place.md)
  An object that allows a custom annotation to potentially supersede a point of interest at the same map coordinates.
### Creating callouts
- [callout](annotationconstructoroptions/callout.md)
  A delegate that enables you to customize the annotation’s callout.
- [calloutEnabled](annotationconstructoroptions/calloutenabled.md)
  A Boolean value that determines whether the map shows a callout.
- [calloutOffset](annotationconstructoroptions/calloutoffset.md)
  The offset, in CSS pixels, of a callout from the top center of the element.
### Grouping annotations
- [clusteringIdentifier](annotationconstructoroptions/clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.
- [collisionMode](annotationconstructoroptions/collisionmode.md)
  A mode that determines the shape of the collision frame.
- [id](annotationconstructoroptions/id.md)
  A Place ID that uniquely identifies a feature.
### Instance Properties
- [coordinate](annotationconstructoroptions/coordinate.md)
  Sets the coordinate of the annotation.
- [element](annotationconstructoroptions/element.md)
  Sets the element of the annotation.
- [map](annotationconstructoroptions/map.md)
  Sets the annotation’s map.
- [selectionAccessory](annotationconstructoroptions/selectionaccessory.md)
  The accessory that displays place information when a person selects a place.
- [selectionAccessoryOffset](annotationconstructoroptions/selectionaccessoryoffset.md)
  The offset that changes the selection accessory’s default anchor point.

## Relationships

### Inherited By
- [ImageAnnotationConstructorOptions](imageannotationconstructoroptions.md)
- [MarkerAnnotationConstructorOptions](markerannotationconstructoroptions.md)

## See Also

- [new Annotation(location, factory, options)](annotation/annotationconstructor.md)
  Creates a new annotation given its location and initialization options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions)*