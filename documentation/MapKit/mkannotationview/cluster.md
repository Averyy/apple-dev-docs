# cluster

**Framework**: MapKit  
**Kind**: property

The clustering annotation view that replaces the annotation view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var cluster: MKAnnotationView? { get }
```

#### Discussion

When the map is displaying this annotation view, the value of this property is `nil`.

## See Also

- [Decluttering a Map with MapKit Annotation Clustering](decluttering-a-map-with-mapkit-annotation-clustering.md)
  Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.
- [var clusteringIdentifier: String?](mkannotationview/clusteringidentifier.md)
  An identifier that determines whether the annotation view participates in clustering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/cluster)*