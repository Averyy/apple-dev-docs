# DirectionsConstructorOptions

**Framework**: MapKit JS  
**Kind**: struct

Options that you may provide when creating a directions object.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary DirectionsConstructorOptions {
	string language;
};
```

#### Overview

Use [`DirectionsConstructorOptions`](directionsconstructoroptions.md) to set options when creating a [`mapkit.Directions`](mapkit.directions/mapkit.directions.md) object.

If you set `language` to a language ID, such as `fr-CA` or `en-GB`, MapKit JS returns step-by-step directions in the specified language, if available. If you don’t set `language` when initializing a [`mapkit.Directions`](mapkit.directions.md) object, the directions default to the language ID you provide when initializing the map with [`init`](mapkit/init.md). If the map doesn’t have a specified language upon initialization, MapKit JS returns directions in the browser’s language setting.

Set the `language` option when creating a [`mapkit.Directions`](mapkit.directions/mapkit.directions.md) object as in the code below:

```javascript
var directions = new mapkit.Directions({
    language: "en-GB"
});
```

## Topics

### Initializing language
- [language](directionsconstructoroptions/language.md)
  A language ID that determines the language for route information.

## See Also

- [mapkit.Directions](mapkit.directions/mapkit.directions.md)
  Creates a directions object with options you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsconstructoroptions)*