# strokeEnd

**Framework**: MapKit JS  
**Kind**: property

The unit distance along the line where a stroke ends.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
attribute number strokeEnd;
```

#### Discussion

The value of this property must be a number between `0` and `1`. A value of `0` represents the beginning of the polyline, and a value of `1,` the default, represents the end. MapKit JS interprets values between `0` and `1` linearly along the length of the polyline.

The stroke is only visible for the overlay when [`strokeStart`](styleconstructoroptions/strokestart.md) is less than [`strokeEnd`](styleconstructoroptions/strokeend.md).

## See Also

- [strokeColor](styleconstructoroptions/strokecolor.md)
  The stroke color of a line.
- [strokeOpacity](styleconstructoroptions/strokeopacity.md)
  The opacity of the stroke color.
- [strokeStart](styleconstructoroptions/strokestart.md)
  The unit distance along the line where a stroke begins.
- [lineGradient](styleconstructoroptions/linegradient.md)
  The gradient to apply along the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/styleconstructoroptions/strokeend)*