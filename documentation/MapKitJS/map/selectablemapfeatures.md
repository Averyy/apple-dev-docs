# selectableMapFeatures

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

An array of map features that users can select from the map.

**Availability**:
- MapKit JS 5.74.1+

## Declaration

```
get selectableMapFeatures(): MapFeatureType[];
set selectableMapFeatures(value: MapFeatureType[]);
```

## Discussion

This is an array of the selectable map features the map displays from the types available in [`MapFeatureType`](../mapfeaturetype.md).

## See Also

### Selecting map features
- [selectableMapFeatureSelectionAccessory](./selectablemapfeatureselectionaccessory.md)
  An accessory for displaying place information when a person selects a map feature.
- [annotationForMapFeature](./annotationformapfeature.md)
  The method MapKit JS calls when the framework creates a map feature annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/selectablemapfeatures)*