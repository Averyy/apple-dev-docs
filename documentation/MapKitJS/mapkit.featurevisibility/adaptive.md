# Adaptive

**Framework**: MapKit JS  
**Kind**: case

A constant indicating that feature visibility adapts to the current map state.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const string Adaptive;
```

#### Discussion

Use `mapkit.FeatureVisibility.Adaptive` to show adaptive controls only when the map is in a given state. You can show or hide controls that aren’t adaptive by setting map properties to `true` or `false`, respectively.

The following example sets the adaptive visibility for the compass and scale, and hides the map type and zoom controls:

```javascript
// Create a map.
var map = new mapkit.Map("my-map-element-id");

// Show the compass only when the rotation is actively changing.
map.showsCompass = mapkit.FeatureVisibility.Adaptive;

// Show the scale only when the zoom level is actively changing.
map.showsScale = mapkit.FeatureVisibility.Adaptive;

// Hide the map type and zoom controls.
map.showsMapTypeControl = false;
map.showsZoomControl = false;
```

## See Also

- [Hidden](mapkit.featurevisibility/hidden.md)
  A constant indicating that the feature is always hidden.
- [Visible](mapkit.featurevisibility/visible.md)
  A constant indicating that the feature is always visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.featurevisibility/adaptive)*