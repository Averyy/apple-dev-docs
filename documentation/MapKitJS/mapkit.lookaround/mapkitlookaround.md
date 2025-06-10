# mapkit.LookAround

**Framework**: MapKit JS  
**Kind**: init

Creates a Look Around object you embed on a webpage and initializes it with the constructor options you choose.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
new mapkit.LookAround(
	optional Element parent,
	mapkit.Coordinate|Place|mapkit.LookAroundScene location,
	optional LookAroundOptions options
);
```

#### Return Value

A [`mapkit.LookAround`](mapkit.lookaround/mapkit.lookaround.md) instance.

#### Discussion

The Look Around view’s constructor takes an optional `parent` argument and an optional `options` argument. If you specify the `parent` argument, MapKit JS inserts the preview element into the DOM as a descendant of `parent`.

## Parameters

- `parent`: A DOM element, or the ID of a DOM element, to use as your map’s container.
- `location`: A   that describes the location the Look Around view shows.
- `options`: Options that   defines for initializing the properties of the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.lookaround/mapkit.lookaround)*