# deviceMotionAnchor(manager:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Specifies this view as the reference body for the motion manager’s device-motion calculations.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)

## Declaration

```swift
nonisolated
func deviceMotionAnchor(manager: CMMotionManager, isEnabled: Bool = true) -> some View
```

#### Discussion

```swift
@State private var motionManager = CMMotionManager()

var body: some View {
    MyView()
        .deviceMotionAnchor(manager: motionManager)
}
```

If more than one view specifies itself as the body of the same manager, the most recent one to do so becomes the body. Once a view stops being the body, whether because it disappeared or because `isEnabled` became `false`, the manager has no body until some view specifies one again.

Use `isEnabled` to pick between views which are all on screen. For example, a map might anchor device motion to a puck, except while navigating, when it anchors to a vehicle icon instead:

```swift
ZStack {
    Puck()
        .deviceMotionAnchor(manager: motionManager,
                            isEnabled: !isNavigating)
    VehicleIcon()
        .deviceMotionAnchor(manager: motionManager,
                            isEnabled: isNavigating)
}
```

## Parameters

- `manager`: The motion manager to specify this view as the body of.
- `isEnabled`: Whether this view should be the manager’s body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/devicemotionanchor(manager:isenabled:))*