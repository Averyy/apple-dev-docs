# Annotations

**Framework**: MapKit JS

Create annotations to add indicators and additional details for specific locations on a map.

#### Overview

Annotations work differently in MapKit JS and native MapKit. In native MapKit, there are annotation objects and annotation views. You decide which annotation view to use for a particular annotation by implementing [`mapView(_:viewFor:)`](https://developer.apple.com/documentation/MapKit/MKMapViewDelegate/mapView(_:viewFor:)-8humz) in the map’s delegate. In MapKit JS, there’s only the annotation, which is both model and view. You can still customize the look of annotations, but MapKit JS requires that you create annotation views explicitly rather than through a delegate.

MapKit JS shows single-point annotations on a map. The framework accomplishes this by creating a [`Annotation`](annotation.md) object and adding it to a map. The framework provides three built-in objects for your convenience:

- [`Annotation`](annotation.md), which allows you to position a live DOM element on the map.
- [`ImageAnnotation`](imageannotation.md), which allows you to customize the annotation with your own imagery.
- [`MarkerAnnotation`](markerannotation.md), which places a defined  balloon marker on the map with a `title`, `subtitle`, and custom glyph text/image.
- [`PlaceAnnotation`](placeannotation.md), which places an annotation for a particular place on a map.
- [`MapFeatureAnnotation`](mapfeatureannotation.md), which places an image for a particular feature on a map.

A callout is a standard or custom element that can give more information about an annotation. A standard callout displays the annotation’s title and subtitle, if you provide them. A callout appears when the user selects an annotation interactively (by clicking or tapping), or programmatically when you set the annotation’s [`selected`](annotation/selected.md) property to `true`. A callout goes away when the user deselects an annotation interactively either by tapping or clicking the map or by selecting another item on the map, or when you deselect it programmatically.

| Event | Interface | Summary |
| --- | --- | --- |
| `select` | [`MapKitEvent`](mapkitevent.md) | MapKit JS sets the annotation’s selected property to `true`. |
| `deselect` | [`MapKitEvent`](mapkitevent.md) | MapKit JS sets the annotation’s selected property to `false`. |
| `drag-start` | [`MapKitEvent`](mapkitevent.md) | The user initiates a drag for an annotation. A long press or click without movement isn’t a drag. |
| `dragging` | [`AnnotationDragEvent`](annotationdragevent.md) | The user is dragging an annotation. This event has an extra coordinate property for the coordinate of the annotation at the time the event occurs. Note: This is different from the annotation’s own coordinate property because that property doesn’t update until the user drops the annotation. |
| `drag-end` | [`MapKitEvent`](mapkitevent.md) | The user ends a drag for an annotation. |

## Topics

### Annotations
- [Clustering annotations](clustering-annotations.md)
  Combine multiple annotations into a single clustered annotation.
- [class Annotation](annotation.md)
  The base annotation object for creating custom annotations.
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
### Customize annotations
- [interface AnnotationCalloutDelegate](annotationcalloutdelegate.md)
  Methods for customizing the behavior and appearance of an annotation callout.
- [const CollisionMode](collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
- [const DisplayPriority](displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [interface Size](size.md)
  A structure that represents a size.
### Events
- [class MapKitEvent](mapkitevent.md)
  A generic MapKit JS event object.
- [class AnnotationDragEvent](annotationdragevent.md)
  An event that occurs when someone drags an annotation.

## See Also

- [Overlays](overlays.md)
  Create overlays to highlight geographic regions or paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotations)*