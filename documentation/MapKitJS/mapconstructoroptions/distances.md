# distances

**Framework**: MapKit JS  
**Kind**: property

The system of measurement that displays on the map.

**Availability**:
- MapKit JS 5.13+

## Declaration

```swift
distances?: Distance;
```

#### Discussion

Sets the system of measurement for displaying map distances. See [`Distance`](distance.md) for accepted values.

This property applies to the scale, if it displays. The default value is [`Adaptive`](distance/adaptive.md), which means that the measurement system depends on the map’s set [`language`](mapkitinitializationoptions/language.md). This property affects displayed distances only; it doesn’t affect data that returns from a service, such as [`Directions`](directions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapconstructoroptions/distances)*