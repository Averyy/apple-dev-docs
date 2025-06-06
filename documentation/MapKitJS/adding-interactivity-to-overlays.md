# Adding interactivity to overlays

**Framework**: MapKit JS

Configure and respond to overlays to make them interactive.

#### Overview

Use overlays to make specific areas of your map interactive. To enable interactivity with an overlay, you configure the map, create an overlay, and add an event listener to receive events when a user selects or deselects the overlay.

##### Configure the Overlay

A map instance emits `select` and `deselect` events from overlays when a user selects and deselects the overlay, respectively. To configure an overlay so that a map emits these events, add it to the map and do the following:

- Set the [`enabled`](mapkit.overlay/enabled.md) property to `true`.
- Set the [`visible`](mapkit.overlay/visible.md) property to `true`.
- Ensure the overlay isn’t so small that MapKit JS can’t draw it.
- Ensure the overlay appears at least partially within the visible map rectangle.

Additionally, the shape needs to have one of the following settings:

- A fill color that’s not `null` that enables the overlay to receive a tap.
- A stroke color that’s not `null` with a line width greater than `0` that enables a tap or click for the shape’s outline.

To make an overlay transparent and selectable, don’t change the overlay [`visible`](mapkit.overlay/visible.md) property to `false`. Instead, set the `opacity` of the overlay’s style [`fillOpacity`](mapkit.style/fillopacity.md) or [`strokeOpacity`](mapkit.style/strokeopacity.md) property to `0`, as in the following example:

```javascript
regionOverlay.style.fillOpacity = 0
rectangle.style.strokeOpacity = 0
```

##### Add an Event Listener to Respond to Map Events

When the user taps or clicks the overlay, MapKit JS changes the overlay’s [`selected`](mapkit.overlay/selected.md) property and propagates an event from the [`mapkit.Map`](mapkit.map.md) object. Use [`addEventListener`](mapkit/addeventlistener.md) to receive events from the [`mapkit.Map`](mapkit.map.md) object when the user selects an overlay. To stop receiving events, use [`removeEventListener`](mapkit/removeeventlistener.md).

> 💡 **Tip**:  Because MapKit JS places annotations on top of overlays, the user can inadvertently select the annotation when an annotation and an overlay are both visible. To keep an annotation visible and allow the selection of the overlay, set the annotation’s [`enabled`](mapkit.annotation/enabled.md) property to `false`.

 Because MapKit JS places annotations on top of overlays, the user can inadvertently select the annotation when an annotation and an overlay are both visible. To keep an annotation visible and allow the selection of the overlay, set the annotation’s [`enabled`](mapkit.annotation/enabled.md) property to `false`.

MapKit JS emits a `select` or `deselect` event when the overlay’s [`selected`](mapkit.overlay/selected.md) property changes. Each event that originates from an overlay has an `overlay` property, which is the [`mapkit.Overlay`](mapkit.overlay.md) object that changes state.

The following example shows the logging of a message when the user selects an overlay on the map:

```javascript
map.addEventListener('select', function(event) {
    if (event.overlay)
        console.log("You selected an overlay.");
});
```

See [`Handling map events`](handling-map-events.md) for a list of map events.

## See Also

- [mapkit.Overlay](mapkit.overlay.md)
  An abstract base object that defines the methods and attributes for map overlays.
- [mapkit.Style](mapkit.style.md)
  A set of observable attributes for overlays, including the color and opacity of strokes and fills, and line styles.
- [mapkit.CircleOverlay](mapkit.circleoverlay.md)
  A circular overlay with a configurable radius that centers on a specific geographic coordinate.
- [mapkit.PolylineOverlay](mapkit.polylineoverlay.md)
  An overlay of connected line segments that don’t form a closed shape.
- [mapkit.PolygonOverlay](mapkit.polygonoverlay.md)
  An overlay consisting of one or more points that forms a closed shape.
- [OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.
- [mapkit.TileOverlay](mapkit.tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/adding-interactivity-to-overlays)*