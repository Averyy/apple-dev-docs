# Annotation

**Framework**: Maps Web Snapshots  
**Kind**: dictionary

An object for a Snapshot URL that describes annotation characteristics.

**Availability**:
- Maps Web Snapshots 1.0+

## Declaration

```swift
object Annotation
```

## Properties

- `markerStyle` (string): The style of the annotation. Supported styles include `do`t, `balloon`, `large`, and `img`. If you use `img`, you must also specify `imgIdx`, and may specify `offset`.
- `point` (string): A single point that defines the location at which to place an annotation. Supported values include latitude and longitude coordinates, addresses, or the keyword `center`, which places an annotation on the map’s center point.
- `color` (string): The color of the annotation. Supported values are HTML color names or hexadecimal color codes. For example: ```javascript
annotations=[{"point":"37.78,-122.42", "color":"449944"}]
``` If the annotation has an “`img`” `markerStyle`, the Maps Web Snapshots API ignores this parameter.
- `glyphColor` (string): The tint color of the glyph. This property accepts a color name or a hexadecimal color value.
- `glyphImgIdx` (integer): The zero-based index of the glyph image referenced in the array of images used for a specific annotation. Don’t set the `glyphText` property when using this property. If the annotation has a `“dot”` or `“img”` `markerStyle`, the Maps Web Snapshots API ignores this parameter.
- `glyphText` (string): A single alphanumeric character from the set {`a`-`z`, `A`-`Z`, `0`-`9`}, displayed inside the annotation. If the annotation has a “`dot`” or “`img`” `markerStyle`, the Maps Web Snapshots API ignores this parameter.
- `imgIdx` (integer): The zero-based index of the image referenced in the array of images to use for this annotation. The Maps Web Snapshots API requires this property if `markerStyle` is `img`.
- `offset` (string): An optional offset in scale independent pixels of the image from the bottom center. Specify the offset as a comma-separated string with x and y values. X values move the element to the left or right with positive and negative values, respectively. Y values move the element up or down with positive and negative values, respectively. For example, the following value moves the element down 5 scale-independent pixels: ```javascript
"offset": "0,-5"
``` The Maps Web Snapshots API ignores the offset property if `markerStyle` is `dot`, `balloon`, or `large`.

## See Also

- [Generating a URL and Signature to Create a Maps Web Snapshot](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md)
  Create a Snapshot URL and generate a signature to validate the request.
- [object Overlay](overlay.md)
  A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.
- [object OverlayStyle](overlaystyle.md)
  A  JSON object that describes reusable styles for an overlay.
- [object Image](image.md)
  A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/snapshots/annotation)*