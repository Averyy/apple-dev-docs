# mapkit.LookAroundPreview

**Framework**: MapKit JS  
**Kind**: init

Creates a Look Around preview you embed on a webpage and initializes it with the constructor options you choose.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
new mapkit.LookAroundPreview(
	optional Element parent,
	mapkit.Coordinate|Place|mapkit.LookAroundScene location,
	optional LookAroundPreviewOptions options
);
```

#### Return Value

A [`mapkit.LookAroundPreview`](mapkit.lookaroundpreview/mapkit.lookaroundpreview.md) instance.

#### Discussion

The Look Around preview’s constructor takes an optional `parent` argument and an optional `options` argument. If you specify the `parent` argument, MapKit JS inserts the preview element into the DOM as a descendant of `parent`.

## Parameters

- `parent`: A DOM element, or the ID of a DOM element, to use as your view’s container.
- `location`: A   that describes the location the preview shows.
- `options`: Options that   defines for initializing the properties of the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.lookaroundpreview/mapkit.lookaroundpreview)*