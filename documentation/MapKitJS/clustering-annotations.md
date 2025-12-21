# Clustering annotations

**Framework**: MapKit JS

Combine multiple annotations into a single clustered annotation.

#### Overview

Annotations display coordinate-specific data on a map, typically in the form of markers or images. To declutter annotation-heavy maps, MapKit JS supports . As the user zooms out on a map that contains annotations, MapKit JS groups individual annotations into a  if they collide and if they share the same [`clusteringIdentifier`](annotation/clusteringidentifier.md).

The cluster annotation’s [`memberAnnotations`](annotation/memberannotations.md) property lists the individual annotations within the cluster. By default, a cluster annotation’s marker displays its member count.

MapKit JS creates cluster annotations automatically. Although you can’t instantiate a cluster annotation, you can customize the look of cluster annotations by providing a delegate method, [`annotationForCluster`](map/annotationforcluster.md), to the map.

##### Understand the Annotations Arrays

Although visible on a map, cluster annotations aren’t members of the map’s [`annotations`](map/annotations.md) array. The annotations that make up the cluster do belong to the [`annotations`](map/annotations.md) array, however, even if they’re not individually visible on the map. For example, the following figure shows a map with annotations A, B, C, D, and E:

![A map showing annotations A, B, C, D, and E with markers.](https://docs-assets.developer.apple.com/published/9b726c928f429a9d0e686e2680c4a407/cluster-annotations-01%402x.png)

If the user zooms out so A, B, and C overlap on the map, the annotations combine to create cluster annotation Q, as in the following figure:

![A map showing cluster annotation Q, and annotations D and E. Annotations D and E have markers. Cluster annotation Q has the letters ABC in its marker.](https://docs-assets.developer.apple.com/published/fed1d7801c2f71b2277c4cac2681cf29/cluster-annotations-02%402x.png)

The map displays annotations Q, D, and E, and the resulting annotation arrays are:

- `Q.memberAnnotations = [A, B, C];`
- `map.annotations = [A, B, C, D, E];`

##### Set Cluster Annotation Properties

Cluster annotations have the same properties as other annotations, but you can’t set some values, including [`coordinate`](annotation/coordinate.md), [`clusteringIdentifier`](annotation/clusteringidentifier.md), and [`draggable`](annotation/draggable.md). Other values have specific defaults as the following table shows:

| Property | Default for clustering | Description |
| --- | --- | --- |
| [`title`](annotation/title.md) | The `title` of the member annotation with the highest priority. | The annotation title text. |
| [`subtitle`](annotation/subtitle.md) | “`+N` more”, where `N + 1` is the number of member annotations. | The annotation subtitle text. |
| [`coordinate`](annotation/coordinate.md) | The average of the member annotation coordinates. | The annotation’s coordinate. The system automatically sets the coordinate of a cluster annotation to the average of all of the contained member annotation coordinates. You can’t change this value; therefore, the user can’t ever drag a cluster annotation. |
| [`glyphText`](markerannotation/glyphtext.md) | `N + 1` (the number of member annotations). | The annotation glyph text. |
| [`draggable`](annotation/draggable.md) | `false` | Determines whether the user may drag the annotation. You can’t modify this property. |
| [`memberAnnotations`](annotation/memberannotations.md) | NA | A flat array containing all annotations within the cluster annotation. Only cluster annotations have a `memberAnnotations` property. You can’t modify this property. |
| [`clusteringIdentifier`](annotation/clusteringidentifier.md) | `null` | A shared identifier for all of the member annotations. An annotation needs a `clusteringIdentifier` to be part of an annotation cluster. |

## Topics

- [class ClusterAnnotation](clusterannotation.md)
  An annotation type that groups multiple annotations together.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/clustering-annotations)*