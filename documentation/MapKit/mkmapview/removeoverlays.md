# removeOverlays(_:)

**Framework**: MapKit  
**Kind**: method

Removes one or more overlay objects from the map.

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
func removeOverlays(_ overlays: [any MKOverlay])
```

#### Discussion

This method removes the specified overlays regardless of which level each one is in. Removing an overlay also removes its corresponding renderer, if one is in use. The method ignores an overlay object if it isn’t associated with the map view.

## Parameters

- `overlays`: An array of objects, each of which conforms to the   protocol.

## See Also

- [func addOverlay(any MKOverlay)](mkmapview/addoverlay(_:).md)
  Adds a single overlay object to the map.
- [func addOverlays([any MKOverlay])](mkmapview/addoverlays(_:).md)
  Adds an array of overlay objects to the map.
- [func removeOverlay(any MKOverlay)](mkmapview/removeoverlay(_:).md)
  Removes a single overlay object from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/removeoverlays(_:))*