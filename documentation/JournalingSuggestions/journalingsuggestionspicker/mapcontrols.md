# mapControls(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Configures all `Map` views in the associated environment to have standard size and position controls

**Availability**:
- iOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapControls(@ViewBuilder _ content: () -> some View) -> some View
```

#### Discussion

You provide the controls you want to appear atop your map. When using a control in conjunction with `.mapControls` you don’t need to specify a scope. Views that are not MapKit controls will be ignored.

```None
Map()
.mapControls {
    MapScaleView()
    MapUserLocationButton()
}
```

Controls can be modified individually or all at once. Custom frames and alignments set on controls are ignored.

```None
Map()
.mapControls {
    MapCompass()
        .mapControls(.visible)
    MapPitchToggle()
        .buttonBorderShape(.circular)
        .tint(.purple)
}
.controlSize(.large)
```

On watchOS, space is at a premium. When using the mapControls modifier, MapUserLocationButton and MapCompass are automatically combined if present.

```None
Map()
.mapControls {
    MapUserLocationButton()
    MapCompass()
}
```

## Parameters

- `content`: A view builder returning the controls you wish your 


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapcontrols(_:))*