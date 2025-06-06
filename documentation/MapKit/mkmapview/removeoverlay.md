# removeOverlay(_:)

**Framework**: MapKit  
**Kind**: method

Removes a single overlay object from the map.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeOverlay(_ overlay: any MKOverlay)
```

#### Discussion

This method removes the overlay regardless of the level that it’s in. Removing an overlay also removes its corresponding renderer, if one is in use. If the specified overlay isn’t associated with the map view, this method does nothing.

## Parameters

- `overlay`: The overlay object to remove.

## See Also

- [func addOverlay(any MKOverlay)](mkmapview/addoverlay(_:).md)
  Adds a single overlay object to the map.
- [func addOverlays([any MKOverlay])](mkmapview/addoverlays(_:).md)
  Adds an array of overlay objects to the map.
- [func removeOverlays([any MKOverlay])](mkmapview/removeoverlays(_:).md)
  Removes one or more overlay objects from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/removeoverlay(_:))*