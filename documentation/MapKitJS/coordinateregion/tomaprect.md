# toMapRect()

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Returns the map rectangle that corresponds to the calling coordinate region.

**Availability**:
- MapKit JS 5.0+ - Deprecated in 6.0

> **Deprecated**: This conversion is mathematically imprecise. Use [`MapRect`](../maprect.md) directly to avoid inaccuracies.

## Declaration

```
toMapRect(): MapRect;
```

## Mentions

- [MapKit JS 6](../mapkit-js-6.md)
- [Migrating from Version 5 to Version 6](../migrating-from-version-5-to-version-6.md)

## Return Value

A [`MapRect`](../maprect.md) that corresponds to the calling [`CoordinateRegion`](../coordinateregion.md).

## See Also

### Comparing, copying, and converting regions
- [copy()](./copy.md)
  Returns a copy of the calling coordinate region.
- [equals(anotherRegion)](./equals.md)
  Returns a Boolean value indicating whether two regions are equal.
- [toBoundingRegion()](./toboundingregion.md)
  Returns the bounding region that corresponds to the specified coordinate region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/coordinateregion/tomaprect)*