# Hidden

**Framework**: MapKit JS  
**Kind**: case

A constant indicating that the feature is always hidden.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const string Hidden;
```

#### Discussion

Use `mapkit.FeatureVisibility.Hidden` to hide adaptive map controls, such as the compass and scale. You can show or hide controls that aren’t adaptive by setting map properties to `true` or `false`, respectively.

The following example shows how to always hide the compass, the map type, and the zoom controls:

```javascript
// Create a map.
const map = new mapkit.Map("my-map-element-id");

// Always hide the compass. 
map.showsCompass = mapkit.FeatureVisibility.Hidden;

// Hide the map type and the zoom controls.
map.showsMapTypeControl = false;
map.showsZoomControl = false;

```

## See Also

- [Adaptive](mapkit.featurevisibility/adaptive.md)
  A constant indicating that feature visibility adapts to the current map state.
- [Visible](mapkit.featurevisibility/visible.md)
  A constant indicating that the feature is always visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.featurevisibility/hidden)*