# AnnotationConstructorOptions

**Framework**: MapKit JS  
**Kind**: struct

An object that contains options for creating annotation features.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary AnnotationConstructorOptions {
	string title;
	string subtitle;
	string accessibilityLabel;
	Object data;
	boolean draggable;
	boolean visible;
	boolean enabled;
	boolean selected;
	boolean calloutEnabled;
	boolean animates;
	string appearanceAnimation;
	DOMPoint anchorOffset;
	DOMPoint calloutOffset;
	AnnotationCalloutDelegate callout;
	Object size;
	number displayPriority;
	string collisionMode;
	mapkit.Padding padding;
	string clusteringIdentifier;
	Place place;
	string id;
};
```

#### Overview

Use [`AnnotationConstructorOptions`](annotationconstructoroptions.md) when you need to create a custom view to provide features beyond those that the [`mapkit.ImageAnnotation`](mapkit.imageannotation.md) object provides.

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
### Setting position and appearance attributes
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
  An object that allows a custom annotation to potentially supecede a point of interest at the same map coordinates.
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

## See Also

- [mapkit.Annotation](mapkit.annotation/mapkit.annotation.md)
  Creates a new annotation given its location and initialization options.
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [addEventListener](mapkit.annotation/addeventlistener.md)
  Adds an event listener to handle events that user interactions with annotations trigger.
- [removeEventListener](mapkit.annotation/removeeventlistener.md)
  Removes an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions)*