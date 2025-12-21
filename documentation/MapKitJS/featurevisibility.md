# FeatureVisibility

**Framework**: MapKit JS  
**Kind**: enum

Constants indicating the visibility of different adaptive map features.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const FeatureVisibility: Readonly<{
    readonly Adaptive: "adaptive";
    readonly Hidden: "hidden";
    readonly Visible: "visible";
}>
```

#### Overview

Indicates whether the map shows adaptive features like the scale, compass, and annotation title and subtitle text. The display of an adaptive feature depends on the current map state. You can show or hide controls that aren’t adaptive, such as the map type control or zoom controls, by setting map properties to `true` or `false`, respectively.

The following example shows the compass only when the map rotation is changing, and hides the zoom controls:

```javascript
// Create a map.
const map = new mapkit.Map("my-map-element-id");

// Show the compass only when the rotation is actively changing.
map.showsCompass = mapkit.FeatureVisibility.Adaptive;

// Hide the zoom controls.
map.showsZoomControl = false;
```

## Topics

### Feature visibility values
- [Adaptive](featurevisibility/adaptive.md)
  A constant indicating that feature visibility adapts to the current map state.
- [Hidden](featurevisibility/hidden.md)
  A constant indicating that the feature is always hidden.
- [Visible](featurevisibility/visible.md)
  A constant indicating that the feature is always visible.
### Type Aliases
- [type FeatureVisibility](featurevisibility/featurevisibility.md)
  A type alias that represents the values of the feature visibility enumeration.

## See Also

- [class Padding](padding.md)
  The values that define content padding within the map view frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/featurevisibility)*