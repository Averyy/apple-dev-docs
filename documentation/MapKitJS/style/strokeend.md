# strokeEnd

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The unit distance along the line where a stroke ends.

**Availability**:
- MapKit JS 5.45+

## Declaration

```
get strokeEnd(): number;
set strokeEnd(strokeEnd: number);
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

## Discussion

The value of this property must be a number between `0` and `1`. A value of `0` represents the beginning of the polyline, and a value of `1`, the default, represents the end. MapKit JS interprets values between `0` and `1` linearly along the length of the polyline.

The stroke is only visible for the overlay when [`strokeStart`](../styleconstructoroptions/strokestart.md) is less than [`strokeEnd`](../styleconstructoroptions/strokeend.md).

## See Also

### Styling strokes
- [strokeColor](./strokecolor.md)
  The stroke color of a line.
- [strokeOpacity](./strokeopacity.md)
  The opacity of the stroke color.
- [strokeStart](./strokestart.md)
  The unit distance along the line where a stroke begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/style/strokeend)*