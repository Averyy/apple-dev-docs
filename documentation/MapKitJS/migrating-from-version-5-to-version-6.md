# Migrating from Version 5 to Version 6

**Framework**: MapKit JS

Adopt modern web platform conventions introduced in MapKit JS version 6.

#### Breaking Changes

##### Native Eventtarget Replaces Mapkiteventtarget

MapKit JS version 6 removes the custom event system in favor of standard DOM APIs. All MapKit JS classes that previously extended [`MapKitEventTarget`](mapkiteventtarget.md) (such as [`Map`](map.md), [`Annotation`](annotation.md), [`TileOverlay`](tileoverlay.md), and the [`mapkit`](mapkit.md) namespace object) now extend `EventTarget`.

**The third argument to `addEventListener` has changed.** In version 5, the third argument was a `thisObject` — an object to use as `this` when calling the listener. In version 6, it’s the standard `EventListenerOptions` object, which supports `once`, `signal`, and other standard features.

```javascript
// Version 5: thisObject as third argument.
map.addEventListener("region-change-end", this.handleRegionChange, this);

// Version 6: use arrow functions for context binding.
map.addEventListener("region-change-end", (event) => this.handleRegionChange(event));

// Version 6: use standard EventListenerOptions.
map.addEventListener("region-change-end", handleRegionChange, { once: true });
```

##### Null Replaces Undefined for Absent Values

MapKit JS version 6 returns `null` instead of `undefined` for optional properties and return values. This affects getters, method return values, callback parameters, event properties, and data class properties such as [`Place`](place.md).

```javascript
// Version 5
if (annotation.id !== undefined) { /* ... */ }

// Version 6 — check for null.
if (annotation.id !== null) { /* ... */ }

// Version 6 — nullish check (works for both null and undefined).
if (annotation.id != null) { /* ... */ }
```

JavaScript code using truthy/falsy checks or nullish coalescing (`??`) isn’t affected.

**TypeScript:** Getter return types change from `T | undefined` to `T | null`. Code using strict equality checks against `undefined` produces type errors.

##### Cors Required for Images

MapKit JS version 6 requires CORS for all images, including tile images and annotation images. When you use [`ImageSource`](imagesource.md) objects such as `HTMLCanvasElement` or `HTMLImageElement`, make sure they contain only CORS-clean pixel data.

##### Tileoverlay Behavioral Changes

In version 6, MapKit JS no longer turns off map rotation when tile overlays are present, and zoom no longer snaps to integer levels. Tile images also require CORS, as described in [`CORS Required for Images`](migrating-from-version-5-to-version-6#CORS-Required-for-Images.md).

#### Deprecations

##### Callback Parameters and Cancellation in Async Service Apis

All asynchronous service methods now return `Promise` instead of `number` (request ID). You can use async/await syntax. Callbacks still work at runtime but the framework considers them deprecated. The framework also deprecates [`cancel()`](service/cancel.md) method accepting a numeric request ID — use `AbortController`/`AbortSignal` instead.

```javascript
// Version 5
search.search("coffee", (error, result) => {
    if (error) { console.error(error); return; }
    console.log(result.places);
});

// Version 6
try {
    const result = await search.search("coffee");
    console.log(result.places);
} catch (error) {
    console.error(error);
}
```

```javascript
// Version 5
const id = search.search("query", callback);
search.cancel(id);

// Version 6
const controller = new AbortController();
const promise = search.search("query", { signal: controller.signal });
controller.abort();
```

When you abort a request, the Promise rejects with a `DOMException` where `name === "AbortError"`, matching the `fetch()` API behavior. A new [`RequestError`](requesterror.md) type represents network and HTTP errors.

**TypeScript:** The return type changes from `number` to `Promise<T>`, and `cancel()` now accepts `Promise<unknown>` instead of `number`.

##### Mapfeatureannotationfetchplace

Use [`getPlace()`](placelookup/getplace.md) instead. It returns a Promise and supports AbortSignal cancellation.

##### Imagedelegategetimageurl

Use [`getImage()`](imagedelegate/getimage.md) instead. It returns a Promise that resolves to an [`ImageSource`](imagesource.md) or URL string.

##### Coordinateregiontomaprect

[`toMapRect()`](coordinateregion/tomaprect.md) is mathematically imprecise and MapKit JS deprecates it in this release. Use [`MapRect`](maprect.md) directly when precision matters, particularly at low zoom levels.

- Prefer [`visibleMapRect`](map/visiblemaprect.md) over [`region`](map/region.md) for setting the map’s visible area.
- Pass [`MapRect`](maprect.md) to [`cameraBoundary`](map/cameraboundary.md) instead of [`CoordinateRegion`](coordinateregion.md).

##### Tileoverlayurltemplate Renamed to Imagefortile

This release renames the `urlTemplate` property to [`imageForTile`](tileoverlay/imagefortile.md). The old name continues to work as a deprecated alias.

##### Enumeration Accessors Moved to Top Level

Enumeration accessors previously nested on class objects are now available directly on the [`mapkit`](mapkit.md) namespace with singular naming. The old accessors still work but log a deprecation warning.

| Deprecated | Replacement |
| --- | --- |
| `mapkit.Map.`​[`MapTypes`](map/maptypes.md) | `mapkit.`​[`MapType`](mapkit/maptype.md) |
| `mapkit.Map.`​[`ColorSchemes`](map/colorschemes.md) | `mapkit.`​[`ColorScheme`](mapkit/colorscheme.md) |
| `mapkit.Map.`​[`Distances`](map/distances-data.var.md) | `mapkit.`​[`DistanceUnitSystem`](mapkit/distanceunitsystem.md) |
| `mapkit.Map.`​[`LoadPriorities`](map/loadpriorities.md) | `mapkit.`​[`MapLoadPriority`](mapkit/maploadpriority.md) |
| `mapkit.Annotation.`​[`CollisionMode`](annotation/collisionmode-data.var.md) | `mapkit.`​[`AnnotationCollisionMode`](mapkit/annotationcollisionmode.md) |
| `mapkit.Annotation.`​[`DisplayPriority`](annotation/displaypriority-data.var.md) | `mapkit.`​[`AnnotationDisplayPriority`](mapkit/annotationdisplaypriority.md) |
| `mapkit.Directions.`​[`Transport`](directions/transport.md) | `mapkit.`​[`TransportType`](mapkit/transporttype.md) |
| `mapkit.Search.`​[`RegionPriority`](search/regionpriority-data.var.md) | `mapkit.`​[`RegionPriority`](mapkit/regionpriority.md) |

#### New Features

##### Wheel Events Zoom and Pan Without Holding Shift

The map now zooms and pans with wheel events without requiring you to hold the Shift key.

##### Mapkitload Returns Promise

[`load()`](mapkit/load.md) now returns `Promise<MapKit>`:

```javascript
// Version 5
mapkit.load(["map"]);
await new Promise((resolve) => {
    mapkit.addEventListener("load", resolve);
});

// Version 6
const { Map } = await mapkit.load(["map"]);
```

The `data-callback` function now also fires when libraries fail to load, so your application can handle errors instead of waiting indefinitely.

##### Object Literals Accepted As Data Types

You can now pass plain object literals wherever data type class instances were previously required. New interfaces define the expected shape: [`CoordinateData`](coordinatedata.md), [`CoordinateRegionData`](coordinateregiondata.md), [`CoordinateSpanData`](coordinatespandata.md), [`CameraZoomRangeData`](camerazoomrangedata.md), [`MapPointData`](mappointdata.md), [`MapRectData`](maprectdata.md), [`MapSizeData`](mapsizedata.md), and [`PaddingData`](paddingdata.md).

```javascript
// Version 5 — class instances required.
map.region = new mapkit.CoordinateRegion(
    new mapkit.Coordinate(37.3349, -122.0090),
    new mapkit.CoordinateSpan(0.02, 0.02),
);

// Version 6 — plain objects also accepted.
map.region = {
    center: { latitude: 37.3349, longitude: -122.0090 },
    span: { latitudeDelta: 0.02, longitudeDelta: 0.02 },
};
```

Existing code using class instances continues to work because each class implements its corresponding data interface.

##### Imagesource Support for Annotations

[`ImageAnnotation`](imageannotation.md) and [`MarkerAnnotation`](markerannotation.md) now accept [`ImageSource`](imagesource.md) objects directly, in addition to [`ImageHashObject`](imagehashobject.md) and [`ImageDelegate`](imagedelegate.md). You can also pass `Promise<ImageSource>` for async image loading.

##### Imagesource Support for Tileoverlay

[`imageForTile`](tileoverlay/imagefortile.md) now accepts a callback that returns [`ImageSource`](imagesource.md), `Promise<ImageSource>`, or `null` for client-side tile rendering.

##### Placelookupgetplaceannotation Overload

A new overload of [`getPlace()`](placelookup/getplace.md) accepts a [`MapFeatureAnnotation`](mapfeatureannotation.md) directly.

## See Also

- [MapKit JS Release Notes](mapkit-js-release-notes.md)
  Learn about updates, bug fixes, and API changes for MapKit JS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/migrating-from-version-5-to-version-6)*