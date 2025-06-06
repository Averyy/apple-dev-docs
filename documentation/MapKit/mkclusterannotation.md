# MKClusterAnnotation

**Framework**: MapKit  
**Kind**: class

An annotation that groups two or more distinct annotations into a single entity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MKClusterAnnotation
```

#### Overview

A cluster annotation object stands in for the group of annotations. Cluster views promote legibility of the underlying annotations by displaying a single annotation that takes it’s title from one annotation and includes a subtitle that indicates how many additional annotations belong to the group.

MapKit automatically creates cluster annotations when two or more annotation views group too closely together on the map surface. To customize the cluster annotations that display on your map, implement the [`mapView(_:clusterAnnotationForMemberAnnotations:)`](mkmapviewdelegate/mapview(_:clusterannotationformemberannotations:).md) method in your map’s delegate.

## Topics

### Creating a cluster annotation
- [init(memberAnnotations: [any MKAnnotation])](mkclusterannotation/init(memberannotations:).md)
  Creates a cluster annotation with the specified individual annotations.
### Getting the cluster attributes
- [var title: String?](mkclusterannotation/title.md)
  The title string to display for the group of annotations.
- [var subtitle: String?](mkclusterannotation/subtitle.md)
  The subtitle string to display for the group of annotations.
### Getting the annotations
- [var memberAnnotations: [any MKAnnotation]](mkclusterannotation/memberannotations.md)
  The annotations that the cluster contains.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Decluttering a Map with MapKit Annotation Clustering](decluttering-a-map-with-mapkit-annotation-clustering.md)
  Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkclusterannotation)*