# map

**Framework**: MapKit JS  
**Kind**: property

Sets the annotation’s map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
map?: Map;
```

#### Discussion

The framework ignores the map option in the constructor. If present, the framework generates a warning.

To add or remove an annotation from a specific map, use `Map/addAnnotation` and `Map/removeAnnotation`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions/map)*