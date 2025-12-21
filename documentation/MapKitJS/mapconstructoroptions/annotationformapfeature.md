# annotationForMapFeature

**Framework**: MapKit JS  
**Kind**: property

The method MapKit JS calls when the framework creates a map feature annotation.

**Availability**:
- MapKit JS 5.74.1+

## Declaration

```swift
annotationForMapFeature?: (
        mapFeatureAnnotation: MapFeatureAnnotation,
    ) => Annotation | undefined;
```

#### Discussion

You can choose to return the annotation the method provides with modified properties, or provide a new annotation to represent the map feature. If an annotation doesn’t return, MapKit JS uses the default annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapconstructoroptions/annotationformapfeature)*