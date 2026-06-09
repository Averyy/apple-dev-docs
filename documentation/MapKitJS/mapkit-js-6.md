# MapKit JS 6

**Framework**: MapKit JS

Use the most up-to-date version of MapKit JS on your website.

#### Overview

This document includes release notes for updates to MapKit JS 6. You can learn more about MapKit JS version numbers and how to automatically link to the latest available version in [`Loading the latest version of MapKit JS`](loading-the-latest-version-of-mapkit-js.md).

##### 60

MapKit JS 6.0 adopts modern web platform conventions. For detailed guidance on updating your code, see [`Migrating from Version 5 to Version 6`](migrating-from-version-5-to-version-6.md).

###### New Features

- The map now zooms and pans with wheel events without requiring someone to hold the Shift key.
- [`load(libraryNames)`](mapkit/load.md) now returns `Promise<MapKit>`, and the `data-callback` function now also fires when libraries fail to load.
- You can now pass plain object literals in place of data type class instances. New interfaces define the expected shape: [`CoordinateData`](coordinatedata.md), [`CoordinateRegionData`](coordinateregiondata.md), [`CoordinateSpanData`](coordinatespandata.md), [`CameraZoomRangeData`](camerazoomrangedata.md), [`MapPointData`](mappointdata.md), [`MapRectData`](maprectdata.md), [`MapSizeData`](mapsizedata.md), and [`PaddingData`](paddingdata.md).
- [`ImageAnnotation`](imageannotation.md) and [`MarkerAnnotation`](markerannotation.md) now accept [`ImageSource`](imagesource.md) objects directly, in addition to [`ImageHashObject`](imagehashobject.md) and [`ImageDelegate`](imagedelegate.md). You can also pass `Promise<ImageSource>` for async image loading.
- The [`TileOverlay`](tileoverlay.md) [`imageForTile`](tileoverlay/imagefortile.md) callback now accepts [`ImageSource`](imagesource.md), `Promise<ImageSource>`, or `null` for client-side tile rendering.
- A new overload of [`getPlace(id, options)`](placelookup/getplace.md) accepts a [`MapFeatureAnnotation`](mapfeatureannotation.md) directly.

###### Updates

- All MapKit JS classes that previously extended [`MapKitEventTarget`](mapkiteventtarget.md) now extend the native `EventTarget` interface. The third argument to `addEventListener` is now the standard `EventListenerOptions` object instead of a `thisObject`.
- Optional properties and return values now return `null` instead of `undefined` for absent values.
- Images, including tile images and annotation images, now require CORS. [`ImageSource`](imagesource.md) objects must contain only CORS-clean pixel data.
- [`TileOverlay`](tileoverlay.md) no longer turns off map rotation or snaps zoom to integer levels.

###### Deprecated Features

The framework has deprecated the following:

- Callback parameters and numeric request IDs in asynchronous service APIs. Use `Promise`-based return values with async/await, and `AbortController`/`AbortSignal` for cancellation.
- [`fetchPlace(callback)`](mapfeatureannotation/fetchplace.md) , use [`getPlace(id, options)`](placelookup/getplace.md) instead.
- [`getImageUrl(ratio, callback)`](imagedelegate/getimageurl.md), use [`getImage(ratio)`](imagedelegate/getimage.md) instead.
- [`toMapRect()`](coordinateregion/tomaprect.md) because it’s mathematically imprecise. Use [`MapRect`](maprect.md) directly.
- This release renames the `urlTemplate` property on [`TileOverlay`](tileoverlay.md) to [`imageForTile`](tileoverlay/imagefortile.md).
- Enumeration accessors like `mapkit.Map.MapTypes` now live at the top level of the [`mapkit`](mapkit.md) namespace with singular names like [`MapType`](maptype.md).

## See Also

- [MapKit JS 5](mapkit-js-5.md)
  Use the most up-to-date version of MapKit JS on your website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit-js-6)*