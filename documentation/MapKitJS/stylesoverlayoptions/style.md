# style

**Framework**: MapKit JS  
**Kind**: property

An object literal of style properties.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Style style;
```

#### Discussion

The following table lists the available style properties:

|  |  |
| --- | --- |
| `strokeColor` | The stroke color of a line. This can be any valid CSS color value. The default value is `rgb(0, 122, 255)`. Set this to `null` to have no line stroke. |
| `strokeOpacity` | The opacity to apply to strokes as a number between `0` and `1`. The default value is `1`. |
| `lineWidth` | The line width of the stroke line for overlays, in CSS pixels. The default value is `1`. |
| `lineCap` | The shape of the ends of the line. The three options for line endings are `butt` (squared-off ends), `round` (rounded ends), or `square` (ends that have a half-square extension). The default value is `round`. |
| `lineJoin` | The style to use when drawing joins between line segments. The three options are `miter` (the join is a sharp corner), `round` (the join is a rounded corner), or `bevel` (the join is a beveled corner). The default value is `round`. |
| `lineDash` | An array to use as the line’s dash pattern where the numbers represent line and gap lengths in CSS pixels. For example, `[10, 5]` means draw for 10 pixels, leave a 5-pixel gap, and repeat. MapKit JS copies and duplicates the array if there are an odd number of elements in it. Set this to an empty array (`[]`) to draw solid lines. The default value is `[]`. |
| `lineDashOffset` | The number of CSS pixels to offset drawing of the dash pattern. This has no effect if you set the `lineDash` to draw solid lines. The default value is `0`. |
| `fillColor` | The color to use for filling shapes. This can be any valid CSS color value. The default fill color is `rgb(0, 122, 255)`. Set this to `null` to have no fill. |
| `fillOpacity` | The opacity to apply to fills as a number between `0` and `1`. The default opacity is `0.1`. |
| `fillRule` | The rule to use for determining whether a point is inside or outside a polygon. This can be either the nonzero winding rule (`nonzero`), the default, or the even-odd rule (`evenodd`). |

## Parameters

- `options`: An optional object literal of style properties (defined below).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/stylesoverlayoptions/style)*