# mapkit.BoundingRegion

**Framework**: MapKit JS  
**Kind**: init

Creates a rectangular bounding region, which the latitude and longitude coordinates of the rectangle’s northeast and southwest corners define.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.BoundingRegion(
	number northLatitude,
	number eastLongitude,
	number southLatitude,
	number westLongitude
);
```

#### Discussion

The example below creates a new bounding region by passing the required longitude and latitude coordinates to the constructor:

```javascript
const region = new mapkit.BoundingRegion(northLatitude, eastLongitude, southLatitude, westLongitude);
```

## Parameters

- `northLatitude`: The north latitude of the bounding region.
- `eastLongitude`: The east longitude of the bounding region.
- `southLatitude`: The south latitude of the bounding region.
- `westLongitude`: The west longitude of the bounding region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.boundingregion/mapkit.boundingregion)*