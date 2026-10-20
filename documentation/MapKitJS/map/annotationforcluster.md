# annotationForCluster

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get annotationForCluster():
    | ((clusterAnnotation: ClusterAnnotation) => Annotation | undefined)
    | null;
set annotationForCluster(
    value:
        | ((clusterAnnotation: ClusterAnnotation) => Annotation | undefined)
        | null,
);
```

#### Discussion

MapKit JS invokes this delegate method when it creates a cluster annotation, or when a member annotation within the cluster changes.

You can return any of the following:

- The same cluster annotation with its properties, such as title or subtitle, modified.
- A new annotation, such as an image annotation, to represent the cluster.
- No return value. If you don’t return an annotation, MapKit JS uses the default annotation. You don’t need to return a default annotation even if you modify it (as the following code example shows for the cities cluster); the map displays the modifications.

The following example creates annotation clusters for cities and parks:

```javascript
map.addAnnotations(cities.map(city =>
    new mapkit.MarkerAnnotation(city.coordinate, {
        title: city.name,
        subtitle: city.population,
        glyphImage: city.landmarkImage,
        displayPriority: Math.max(city.population / 10000, 1000),
        clusteringIdentifier: "city"
    })
));

map.addAnnotations(parks.map(park =>
    new mapkit.ImageAnnotation(park.coordinate, {
        title: park.name,
        url: { 1: park.image },
        displayPriority: 250,
        clusteringIdentifier: "park"
    })
));

map.annotationForCluster = function(clusterAnnotation) {
    if (clusterAnnotation.clusteringIdentifier === "city") {
        clusterAnnotation.title = "Cities";
        clusterAnnotation.subtitle = clusterAnnotation.memberAnnotations
            .reduce((total, clusterAnnotation) => total + clusterAnnotation.population, 0);
    } else if (clusterAnnotation.clusteringIdentifier === "park") {
        return new mapkit.ImageAnnotation(clusterAnnotation.coordinate, {
            title: "Parks",
            url: { 1: "tree.png" }
        });
    }
};
```

For more information, see [Clustering annotations](../clustering-annotations.md).

## Parameters

- `clusterAnnotation`: An annotation that represents a group of annotations that MapKit JS combines into a cluster.

## See Also

### Annotating the map
- [annotations](./annotations.md)
  An array of all the annotations on the map.
- [selectedAnnotation](./selectedannotation.md)
  The selected annotation.
- [annotationsInMapRect(mapRect)](./annotationsinmaprect.md)
  Returns the list of annotation objects within the specified map rectangle.
- [addAnnotation(annotation)](./addannotation.md)
  Adds an annotation to the map.
- [addAnnotations(annotations)](./addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation(annotation)](./removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations(annotations)](./removeannotations.md)
  Removes multiple annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/annotationforcluster)*