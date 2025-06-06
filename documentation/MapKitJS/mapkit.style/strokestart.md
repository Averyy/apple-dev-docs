# strokeStart

**Framework**: MapKit JS  
**Kind**: property

The unit distance along the line where a stroke begins.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
attribute number strokeStart;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

The value of this property must be a number between `0` and `1`. A value of `0`, the default, represents the beginning of the polyline, and a value of `1` represents the end. MapKit JS interprets values between `0` and `1` linearly along the length of the polyline.

The stroke is only visible for the overlay when [`strokeStart`](styleconstructoroptions/strokestart.md) is less than [`strokeEnd`](styleconstructoroptions/strokeend.md).

## See Also

- [strokeColor](mapkit.style/strokecolor.md)
  The stroke color of a line.
- [strokeOpacity](mapkit.style/strokeopacity.md)
  The opacity of the stroke color.
- [strokeEnd](mapkit.style/strokeend.md)
  The unit distance along the line where a stroke ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.style/strokestart)*