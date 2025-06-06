# mapkit.Annotation

**Framework**: MapKit JS  
**Kind**: class

The base annotation object for creating custom annotations.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Annotation
```

## Mentions

- [Handling map events](handling-map-events.md)

#### Overview

An annotation represents data that you want to display on the map’s surface. Associate each annotation with a [`coordinate`](mapkit.annotation/coordinate.md) on the map. It’s rare that you need to create a [`mapkit.Annotation`](mapkit.annotation/mapkit.annotation.md) object. Use the more common extended objects, [`mapkit.MarkerAnnotation`](mapkit.markerannotation.md) and [`mapkit.ImageAnnotation`](mapkit.imageannotation.md) instead.

Use [`mapkit.Annotation`](mapkit.annotation/mapkit.annotation.md) when you need to customize a view in a way that you can’t accomplish with [`mapkit.ImageAnnotation`](mapkit.imageannotation.md).

The examples below create a custom annotation using a person’s initials to show them on the map. The following CSS style encloses the initials in a gray circle:

```javascript
.circle-annotation {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    color: #FFF;
    background-color: #CCC;
    text-align: center;
    line-height: 32px;
}
```

The following code creates the annotation:

```javascript
var people = [
    { title: "Juan Chavez",
      coordinate: new mapkit.Coordinate(37.3349, -122.0090201),
      role: "developer",
      building: "HQ" },
    { title: "Anne Johnson",
      coordinate: new mapkit.Coordinate(37.722319, -122.434979),
      role: "manager",
      building: "HQ" }
];

var factory = function(coordinate, options) {
    var div = document.createElement("div"),
        name = options.title,           // "Juan Chavez"
        parts = name.split(' ');        // ["Chavez", "Juan"]
    div.textContent = parts[0].charAt(0) + parts[1].charAt(0);    // "JA"
    div.className = "circle-annotation";
    return div;
};

people.forEach(function(person) {
    var options = {
        title: person.title,
        data: { role: person.role, building: person.building }
    };
    var annotation = new mapkit.Annotation(person.coordinate, factory, options);
    map.addAnnotation(annotation);
});
```

## Topics

### Creating an annotation
- [mapkit.Annotation](mapkit.annotation/mapkit.annotation.md)
  Creates a new annotation given its location and initialization options.
- [AnnotationConstructorOptions](annotationconstructoroptions.md)
  An object that contains options for creating annotation features.
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [addEventListener](mapkit.annotation/addeventlistener.md)
  Adds an event listener to handle events that user interactions with annotations trigger.
- [removeEventListener](mapkit.annotation/removeeventlistener.md)
  Removes an event listener.
### Getting the map and element
- [map](mapkit.annotation/map.md)
  The map that the framework adds the annotation to.
- [element](mapkit.annotation/element.md)
  The annotation’s element in the DOM.
### Getting and setting data, titles, and the accessibility label
- [data](mapkit.annotation/data.md)
  Data that you define that’s specific to an annotation.
- [title](mapkit.annotation/title.md)
  The text to display in the annotation’s callout.
- [subtitle](mapkit.annotation/subtitle.md)
  The text to display as a subtitle on the second line of an annotation’s callout.
- [accessibilityLabel](mapkit.annotation/accessibilitylabel.md)
  Accessibility text for the annotation.
### Getting and setting annotation appearance
- [coordinate](mapkit.annotation/coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](mapkit.annotation/anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](mapkit.annotation/appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [displayPriority](mapkit.annotation/displaypriority.md)
  A numeric hint that the map uses to prioritize how it displays annotations.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [padding](mapkit.annotation/padding.md)
  Spacing to add around the annotation when showing items.
- [size](mapkit.annotation/size.md)
  The desired dimensions of the annotation, in CSS pixels.
- [visible](mapkit.annotation/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.
### Getting and setting interaction behavior
- [animates](mapkit.annotation/animates.md)
  A Boolean value that determines whether the framework animates the annotation.
- [draggable](mapkit.annotation/draggable.md)
  A Boolean value that determines whether the user can drag the annotation.
- [selected](mapkit.annotation/selected.md)
  A Boolean value that indicates whether the map shows the annotation in a selected state.
- [enabled](mapkit.annotation/enabled.md)
  A Boolean value that determines whether the annotation responds to user interaction.
### Managing callouts
- [callout](mapkit.annotation/callout.md)
  A delegate that enables you to customize the annotation’s callout.
- [calloutEnabled](mapkit.annotation/calloutenabled.md)
  A Boolean value that determines whether the map shows an annotation’s callout.
- [calloutOffset](mapkit.annotation/calloutoffset.md)
  An offset that changes the annotation callout’s default placement.
### Managing clustering
- [memberAnnotations](mapkit.annotation/memberannotations.md)
  An array of annotations that the framework groups together in a cluster.
- [clusteringIdentifier](mapkit.annotation/clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.
- [collisionMode](mapkit.annotation/collisionmode.md)
  A mode that determines the shape of the collision frame.
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
### Managing selection accessories
- [selectionAccessory](mapkit.annotation/selectionaccessory.md)
  An accessory that displays place information when a person selects a place.
- [selectionAccessoryOffset](mapkit.annotation/selectionaccessoryoffset.md)
  An offset that changes the selection accessory’s default anchor point.

## See Also

- [Clustering annotations](clustering-annotations.md)
  Combine multiple annotations into a single clustered annotation.
- [AnnotationCalloutDelegate](annotationcalloutdelegate.md)
  Methods for customizing the behavior and appearance of an annotation callout.
- [mapkit.PlaceAnnotation](mapkit.placeannotation.md)
  An annotation for a place.
- [mapkit.MapFeatureAnnotation](mapkit.mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation)*