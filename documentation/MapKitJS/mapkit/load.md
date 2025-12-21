# load(libraryNames)

**Framework**: MapKit JS  
**Kind**: method

Tells MapKit JS which libraries to load.

**Availability**:
- MapKit JS 5.75+

## Declaration

```swift
load?(libraryNames: string[]): void;
```

#### Discussion

> **Note**:  The full bundle of MapKit JS doesn’t implement this method.

When this method is called, MapKit JS dispatches either a `load` event or an `load-error` event when the libraries are loaded. The event ([`MapKitLibraryLoadEvent`](mapkitlibraryloadevent.md)) contains the array of library names specified in this method.

## See Also

- [Handling initialization events](handling-initialization-events.md)
  Respond to events that trigger when MapKit JS initializes.
- [init(options)](mapkit/init.md)
  Initializes MapKit JS by providing an authorization callback function and optional language.
- [interface MapKitInitializationOptions](mapkitinitializationoptions.md)
  Initialization options for MapKit JS.
- [Libraries](mapkit/libraries.md)
  The list of available libraries.
- [loadedLibraries](mapkit/loadedlibraries.md)
  A string that describes the list of loaded libraries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit/load)*