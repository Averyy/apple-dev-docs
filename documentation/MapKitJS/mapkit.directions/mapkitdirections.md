# mapkit.Directions

**Framework**: MapKit JS  
**Kind**: init

Creates a directions object with options you provide.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.Directions(
	optional DirectionsConstructorOptions options
);
```

#### Discussion

To request directions, create an instance of the [`mapkit.Directions`](mapkit.directions/mapkit.directions.md) object, then call the [`route`](mapkit.directions/route.md) function with a [`DirectionsRequest`](directionsrequest.md) object as the first parameter. The second parameter for [`route`](mapkit.directions/route.md) is a callback function, through which MapKit JS returns the directions response asynchronously.

To return directions in a specific language, set [`language`](directionsconstructoroptions/language.md) in [`DirectionsConstructorOptions`](directionsconstructoroptions.md) when you create an instance of the [`mapkit.Directions`](mapkit.directions/mapkit.directions.md) object.

## Parameters

- `options`: An object containing the options for creating a directions object. This parameter is optional.

## See Also

- [DirectionsConstructorOptions](directionsconstructoroptions.md)
  Options that you may provide when creating a directions object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.directions/mapkit.directions)*