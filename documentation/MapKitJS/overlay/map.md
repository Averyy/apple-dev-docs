# map

**Framework**: MapKit JS  
**Kind**: property

The map you add the overlay to.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get map(): Map | null;
set map(_: Map | null);
```

#### Discussion

This property is `null` if you don’t add the overlay to a map, or if you remove it from a map.

## See Also

- [data](overlay/data.md)
  Custom data to associate with the overlay.
- [visible](overlay/visible.md)
  A Boolean value that determines whether an overlay is visible.
- [enabled](overlay/enabled.md)
  A Boolean value that determines whether the overlay responds to user interaction.
- [selected](overlay/selected.md)
  A Boolean value that indicates whether the user selects the overlay.
- [style](overlay/style.md)
  Style properties to apply to the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/overlay/map)*