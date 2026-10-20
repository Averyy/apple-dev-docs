# new Directions(options)

**Framework**: MapKit JS  
**Kind**: init  
**Role**: Constructor

Creates a directions object with options you provide.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
constructor(options?: DirectionsConstructorOptions);
```

#### Discussion

To request directions, create an instance of the [`Directions`](../directions.md) object, then call the [`route()`](./route.md) function with a [`DirectionsRequest`](../directionsrequest.md) object as the first parameter. The second parameter for [`route()`](./route.md) is a callback function, through which MapKit JS returns the directions response asynchronously.

To return directions in a specific language, set [`language`](../directionsconstructoroptions/language.md) in [`DirectionsConstructorOptions`](../directionsconstructoroptions.md) when you create an instance of the [`Directions`](../directions.md) object.

## Parameters

- `options`: An object containing the options for creating a directions object. This parameter is optional.

## See Also

### Creating a directions object
- [interface DirectionsConstructorOptions](../directionsconstructoroptions.md)
  Options that you may provide when creating a directions object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directions/directionsconstructor)*