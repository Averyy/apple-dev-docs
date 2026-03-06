# Overlay

**Framework**: Maps Web Snapshots  
**Kind**: dictionary

A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.

**Availability**:
- Maps Web Snapshots 1.0+

## Declaration

```swift
object Overlay
```

## Topics

### Objects
- [object Overlay.LineGradient](overlay/linegradient-data.dictionary.md)
  A property that sets the color stops for the gradient, positioned by offsets between 0 and 1.
- [object Overlay.LineGradientIndexes](overlay/linegradientindexes-data.dictionary.md)
  A property that sets the color stops for the gradient, positioned by indexes of points on the polyline.

## Properties

- `type` (string): An optional property that specifies the type of overlay shape to render. Default: `”polygon”` Options: `“circle”, ”polygon”, or “polyline”`
- `points` (([string] | string)): An array of coordinates, specified as latitude and longitude coordinate pairs, or as a string encoded with the Encoded Polyline Algorithm Format. The array format specifies points for a polyline overlay. The following example specifies two points for a polyline overlay as an array of latitude and longitude coordinate pairs: ```javascript
"points": ["37.779996,-122.51158","37.78040,-122.51348"]

``` You can provide those same parameters in encoded polyline algorithm format: ```javascript
"points": "w{qeFj`wjVwAzJ"
```
- `center` (string): The coordinate of the circle’s center.
- `radius` (number): The circle’s radius in meters.
- `strokeColor` (string): The color of the line between each coordinate point. Supported values are HTML color names or hexadecimal color codes.
- `lineWidth` (integer): The width of the line, in CSS pixels.
- `lineDash` ([integer]): An array that defines a line’s dash pattern, where numbers represent line and gap lengths in CSS pixels. For example, `[10,5]` means draw a line for 10 pixels, leave a 5-pixel gap, and repeat. An empty array draws a solid line, which is the default.
- `fillColor` (string): The object’s fill color.
- `fillOpacity` (number): The opacity value used for filling the object.
- `fillRule` (string): The rule used to determine the inside of the polygon.
- `lineCap` (string): The style used for line end points. Default: `”round”` Options: `”butt”, “round”, or “square”`
- `lineDashOffset` (integer): The line dash offset.
- `lineGradient` (Overlay.LineGradient): An object that determines color stops for the gradient, positioned by offsets between 0 and 1. ```javascript
"lineGradient": {"0": "green", "1": "blue"}
```
- `lineGradientIndexes` (Overlay.LineGradientIndexes): An object that determines where the color stops for the gradient. This property uses indexes of points on the polyline. ```javascript
"lineGradientIndexes": {"1": "blue"}
```
- `lineJoin` (string): The style used for joins between line segments. Default: `“round”` Options: `“bevel”, “miter”, or “round”`
- `strokeOpacity` (number): The opacity value for stroking.
- `styleIdx` (integer): The index number used to reference an `OverlayStyle` object.

## See Also

- [Generating a URL and Signature to Create a Maps Web Snapshot](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md)
  Create a Snapshot URL and generate a signature to validate the request.
- [object Annotation](annotation.md)
  An object for a Snapshot URL that describes annotation characteristics.
- [object OverlayStyle](overlaystyle.md)
  A  JSON object that describes reusable styles for an overlay.
- [object Image](image.md)
  A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/snapshots/overlay)*