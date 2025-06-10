# mapControlVisibility(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Configures all Map controls in the environment to have the specified visibility

**Availability**:
- iOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapControlVisibility(_ visibility: Visibility) -> some View
```

#### Discussion

MapCompass, MapScaleView, and MapPitchToggle may automatically show and hide based on the current state of the Map. That may not be appropriate for all use cases, where always showing a control may be desirable.

```None
HStack {
    MapCompass()
    MapScaleView()
    MapPitchToggle()
}
.mapControls(.visible)
```

Other controls don’t have an automatic visibility behavior, so they will always be visible when automatic is specified. Controls may also be hidden via this modifier when conditionalizing the view is not appropriate

```None
MapUserLocationButton()
    .mapControls(.automatic)
MapZoomStepper()
    .mapControls(.hidden)
```

## Parameters

- `visibility`: How modified map controls should show or hide


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapcontrolvisibility(_:))*