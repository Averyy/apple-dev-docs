# MapSpan

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

An object used in a map or place component for defining the visible area of the map.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object MapSpan
```

## Discussion

Use the `MapSpan` object to define the visible bounds of a map using deltas from a defined center coordinate.

This object can be used in [`Map`](./map.md) and [`Place`](./place.md).

### Example

```json
{
  "components": [
    {
      "role": "map",
      "caption": "Apple Headquarters",
      "latitude": 37.3315294,
      "longitude": -122.0183063,
      "mapSpan": {
        "latitudeDelta": 0.1,
        "longitudeDelta": 0.1
      }
    }
  ]
}
```

## Properties

- `latitudeDelta` (number) *(required)*: A float value between 0.0 and 90.0.

  **Minimum**: `0`; **Maximum**: `90`
- `longitudeDelta` (number) *(required)*: A float value between 0.0 and 180.0.

  **Minimum**: `0`; **Maximum**: `180`

## See Also

### Location
- [object Map](./map.md)
  The component for adding a map.
- [object MapItem](./mapitem.md)
  An object used in a map component for specifying the location of a map pin.
- [object Place](./place.md)
  The component for adding a map with a specific point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/mapspan)*