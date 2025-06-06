# mapkit.FeatureVisibility

**Framework**: MapKit JS  
**Kind**: enum

Constants indicating the visibility of different adaptive map features.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.FeatureVisibility {
	const string Adaptive;
	const string Hidden;
	const string Visible;
};
```

#### Overview

Indicates whether the map shows adaptive features like the scale, compass, and annotation title and subtitle text. The display of an adaptive feature depends on the current map state. You can show or hide controls that aren’t adaptive, such as the map type control or zoom controls, by setting map properties to `true` or `false`, respectively.

The following example shows the compass only when the map rotation is changing, and hides the zoom controls:

```javascript
// Create a map.
var map = new mapkit.Map("my-map-element-id");

// Show the compass only when the rotation is actively changing.
map.showsCompass = mapkit.FeatureVisibility.Adaptive;

// Hide the zoom controls.
map.showsZoomControl = false;
```

## Topics

### Feature visibility values
- [Adaptive](mapkit.featurevisibility/adaptive.md)
  A constant indicating that feature visibility adapts to the current map state.
- [Hidden](mapkit.featurevisibility/hidden.md)
  A constant indicating that the feature is always hidden.
- [Visible](mapkit.featurevisibility/visible.md)
  A constant indicating that the feature is always visible.

## See Also

- [mapkit.Padding](mapkit.padding.md)
  The values that define content padding within the map view frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.featurevisibility)*