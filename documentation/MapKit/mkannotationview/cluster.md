# cluster

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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
weak var cluster: MKAnnotationView? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) MKAnnotationView * clusterAnnotationView;
```

#### Discussion

When the map is displaying this annotation view, the value of this property is `nil`.

## See Also

### Clustering annotation views
- [Decluttering a Map with MapKit Annotation Clustering](../decluttering-a-map-with-mapkit-annotation-clustering.md)
  Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.
- [var clusteringIdentifier: String?](./clusteringidentifier.md)
  An identifier that determines whether the annotation view participates in clustering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/cluster)*