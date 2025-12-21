# coordinate

**Framework**: MapKit JS  
**Kind**: property

A map coordinate that provides a hint for the geographic area to search.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get coordinate(): Coordinate | null;
set coordinate(value: Coordinate | null);
```

#### Discussion

This property supplies coordinates as a reference for a search, for example the coordinates of San Francisco City Hall in San Francisco, CA.

```javascript
{ coordinate: new mapkit.Coordinate(37.779268, -122.419248) }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/coordinate)*