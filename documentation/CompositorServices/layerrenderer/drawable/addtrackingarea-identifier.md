# addTrackingArea(identifier:)

**Framework**: Compositor Services  
**Kind**: method

Returns a tracking area which is create on the drawable’s list of tracking areas.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func addTrackingArea(identifier: LayerRenderer.Drawable.TrackingArea.Identifier) -> LayerRenderer.Drawable.TrackingArea
```

#### Return Value

A tracking area that was created.

#### Discussion

A tracking area describes a region of a view that interacts with the gaze/cursor. Cannot use [`cp_tracking_area_identifier_invalid`](cp_tracking_area_identifier_invalid.md) as an identifier.

## Parameters

- `identifier`: The unique identifier for the tracking area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/addtrackingarea(identifier:))*