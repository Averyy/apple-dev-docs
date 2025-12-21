# ClusterAnnotation

**Framework**: MapKit JS  
**Kind**: class

An annotation type that groups multiple annotations together.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class ClusterAnnotation extends MarkerAnnotation
```

#### Discussion

The framework creates a [`ClusterAnnotation`](clusterannotation.md) when it groups annotations in a cluster. You can replace the annotation or update its properties using the [`annotationForCluster`](map/annotationforcluster.md) delegate method.

## Topics

### Instance Properties
- [memberAnnotations](clusterannotation/memberannotations.md)
  An array of annotations that the framework grouped together in a cluster.

## Relationships

### Inherits From
- [MarkerAnnotation](markerannotation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/clusterannotation)*