# memberAnnotations

**Framework**: MapKit JS  
**Kind**: property

An array of annotations that the framework grouped together in a cluster.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get memberAnnotations(): Annotation[];
```

#### Discussion

This is a flat array that contains all of the annotations that MapKit JS groups together in a cluster. If there are multiple clusters of annotations, this array contains all of the individual annotations within those clusters; it doesn’t contain any cluster annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/clusterannotation/memberannotations)*