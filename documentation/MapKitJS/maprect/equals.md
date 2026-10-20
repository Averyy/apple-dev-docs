# equals(anotherRect)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Compares whether two map rectangles are equal.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
equals(anotherRect: MapRect): boolean;
```

#### Return Value

Returns `true` if a rectangle exactly matches `anotherRect`. Returns `false` if the origin point or size values are different.

## Parameters

- `anotherRect`: The map rectangle to use for comparison.

## See Also

### Working with map rectangles
- [copy()](./copy.md)
  Returns a copy of a map rectangle.
- [scale(scaleFactor, scaleCenter)](./scale.md)
  Returns a scaled map rectangle for a map location.
- [toCoordinateRegion()](./tocoordinateregion.md)
  Returns the region that corresponds to a map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/maprect/equals)*