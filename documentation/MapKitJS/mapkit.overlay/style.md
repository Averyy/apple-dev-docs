# style

**Framework**: MapKit JS  
**Kind**: property

Style properties to apply to the overlay.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Style style;
```

#### Discussion

The following example shows a new [`style`](mapkit.overlay/style.md) object replacing the current style properties for a circle overlay:

```javascript
circleOverlay.style = new mapkit.Style({
    strokeColor: "#777",
    lineWidth: 3,
    fillColor: "#FFF",
    fillOpacity: .2
});
```

You can also change style properties individually, as this example shows:

```javascript
circleOverlay.style.fillOpacity = .33;
circleOverlay.style.lineWidth = 4;
```

## See Also

- [data](mapkit.overlay/data.md)
  Custom data to associate with the overlay.
- [visible](mapkit.overlay/visible.md)
  A Boolean value that determines whether an overlay is visible.
- [enabled](mapkit.overlay/enabled.md)
  A Boolean value that determines whether the overlay responds to user interaction.
- [selected](mapkit.overlay/selected.md)
  A Boolean value that indicates whether the user selects the overlay.
- [map](mapkit.overlay/map.md)
  The map you add the overlay to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.overlay/style)*