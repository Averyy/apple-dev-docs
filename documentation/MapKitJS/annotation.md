# Annotation

**Framework**: MapKit JS  
**Kind**: class

The base annotation object for creating custom annotations.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class Annotation extends MapKitEventTarget
```

#### Overview

An annotation represents data that you want to display on the map’s surface. Associate each annotation with a [`coordinate`](annotation/coordinate.md) on the map. Use the extended objects [`MarkerAnnotation`](markerannotation.md) and [`ImageAnnotation`](imageannotation.md) to create annotations on the map, or `/Annotation` to customize a view beyond the presentation that [`ImageAnnotation`](imageannotation.md) or [`MarkerAnnotation`](markerannotation.md) provide.

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
const people = [
    { title: "Juan Chavez",
      coordinate: new mapkit.Coordinate(37.3349, -122.0090201),
      role: "developer",
      building: "HQ" },
    { title: "Anne Johnson",
      coordinate: new mapkit.Coordinate(37.722319, -122.434979),
      role: "manager",
      building: "HQ" }
];

const factory = function(coordinate, options) {
    const div = document.createElement("div"),
        name = options.title,           // "Juan Chavez"
        parts = name.split(' ');        // ["Chavez", "Juan"]
    div.textContent = parts[0].charAt(0) + parts[1].charAt(0);    // "JA"
    div.className = "circle-annotation";
    return div;
};

people.forEach(function(person) {
    const options = {
        title: person.title,
        data: { role: person.role, building: person.building }
    };
    const annotation = new mapkit.Annotation(person.coordinate, factory, options);
    map.addAnnotation(annotation);
});
```

## Topics

### Creating an annotation
- [new Annotation(location, factory, options)](annotation/annotationconstructor.md)
  Creates a new annotation given its location and initialization options.
- [interface AnnotationConstructorOptions](annotationconstructoroptions.md)
  An object that contains options for creating annotation features.
### Getting the map and element
- [map](annotation/map.md)
  The map that the framework adds the annotation to.
- [element](annotation/element.md)
  The annotation’s element in the DOM.
### Getting the Place ID
- [id](annotation/id.md)
  The place ID that references a place or a map feature.
### Getting and setting data, titles, and the accessibility label
- [data](annotation/data.md)
  Data that you define that’s specific to an annotation.
- [title](annotation/title.md)
  The text to display in the annotation’s callout.
- [subtitle](annotation/subtitle.md)
  The text to display as a subtitle on the second line of an annotation’s callout.
- [accessibilityLabel](annotation/accessibilitylabel.md)
  Accessibility text for the annotation.
### Getting and setting annotation appearance
- [coordinate](annotation/coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](annotation/anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](annotation/appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [displayPriority](annotation/displaypriority-data.property.md)
  A numeric hint that the map uses to prioritize how it displays annotations.
- [padding](annotation/padding.md)
  Spacing to add around the annotation when showing items.
- [size](annotation/size.md)
  The desired dimensions of the annotation, in CSS pixels.
- [visible](annotation/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.
### Getting and setting interaction behavior
- [animates](annotation/animates.md)
  A Boolean value that determines whether the framework animates the annotation.
- [draggable](annotation/draggable.md)
  A Boolean value that determines whether the user can drag the annotation.
- [selected](annotation/selected.md)
  A Boolean value that indicates whether the map shows the annotation in a selected state.
- [enabled](annotation/enabled.md)
  A Boolean value that determines whether the annotation responds to user interaction.
### Managing callouts
- [callout](annotation/callout.md)
  A delegate that enables you to customize the annotation’s callout.
- [calloutEnabled](annotation/calloutenabled.md)
  A Boolean value that determines whether the map shows an annotation’s callout.
- [calloutOffset](annotation/calloutoffset.md)
  An offset that changes the annotation callout’s default placement.
### Managing clustering
- [memberAnnotations](annotation/memberannotations.md)
  An array of annotations that the framework groups together in a cluster.
- [clusteringIdentifier](annotation/clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.
- [collisionMode](annotation/collisionmode-data.property.md)
  A mode that determines the shape of the collision frame.
### Managing selection accessories
- [selectionAccessory](annotation/selectionaccessory.md)
  An accessory that displays place information when a person selects a place.
- [selectionAccessoryOffset](annotation/selectionaccessoryoffset.md)
  An offset that changes the selection accessory’s default anchor point.
### Static properties
- [DisplayPriority](annotation/displaypriority-data.var.md)
  A static property that allows you to access the available display priority enumeration values.
- [CollisionMode](annotation/collisionmode-data.var.md)
  A static property that allows you to access the annotation’s collision mode enumeration values.

## Relationships

### Inherits From
- [MapKitEventTarget](mapkiteventtarget.md)
### Inherited By
- [ImageAnnotation](imageannotation.md)
- [MarkerAnnotation](markerannotation.md)
- [UserLocationAnnotation](userlocationannotation.md)

## See Also

- [Clustering annotations](clustering-annotations.md)
  Combine multiple annotations into a single clustered annotation.
- [class ImageAnnotation](imageannotation.md)
  A customized annotation with image resources that you provide.
- [class MarkerAnnotation](markerannotation.md)
  An annotation that displays a balloon-shaped marker at the designated location.
- [class PlaceAnnotation](placeannotation.md)
  An annotation for a place.
- [class MapFeatureAnnotation](mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [class UserLocationAnnotation](userlocationannotation.md)
  An annotation that represents someone’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation)*