# locationHeadingAnchor(manager:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Specifies this view as the reference body for the location manager’s heading calculations.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+

## Declaration

```swift
nonisolated
func locationHeadingAnchor(manager: CLLocationManager, isEnabled: Bool = true) -> some View
```

#### Discussion

```swift
@State private var locationManager = CLLocationManager()

var body: some View {
    MyView()
        .locationHeadingAnchor(manager: locationManager)
}
```

If more than one view specifies itself as the body of the same manager, the most recent one to do so becomes the body. Once a view stops being the body, whether because it disappeared or because `isEnabled` became `false`, the manager has no body until some view specifies one again.

Use `isEnabled` to pick between views which are all on screen. For example, a map might anchor headings to a puck, except while navigating, when it anchors them to a vehicle icon instead:

```swift
ZStack {
    Puck()
        .locationHeadingAnchor(manager: locationManager,
                               isEnabled: !isNavigating)
    VehicleIcon()
        .locationHeadingAnchor(manager: locationManager,
                               isEnabled: isNavigating)
}
```

## Parameters

- `manager`: The location manager to specify this view as the body of.
- `isEnabled`: Whether this view should be the manager’s body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/locationheadinganchor(manager:isenabled:))*