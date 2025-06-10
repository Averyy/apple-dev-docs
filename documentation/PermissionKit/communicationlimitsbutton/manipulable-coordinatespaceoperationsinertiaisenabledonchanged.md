# manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)

**Framework**: PermissionKit  
**Kind**: method

Allows this view to be manipulated using common hand gestures.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func manipulable(coordinateSpace: some CoordinateSpaceProtocol = .local, operations: Manipulable.Operation.Set = .all, inertia: Manipulable.Inertia = .medium, isEnabled: Bool = true, onChanged: ((Manipulable.Event) -> Void)? = nil) -> some View
```

#### Return Value

A view that can be manipulated using common hand gestures.

#### Discussion

When a person ends the manipulation gesture, the view will return to its initial transform from before the gesture began.

```None
Model3D(named: "ToyRocket")
    .manipulable()
```

## Parameters

- `coordinateSpace`: The coordinate space of the manipulation gesture   event locations.
- `operations`: The set of allowed operations that can be applied when   a person manipulates this view.
- `inertia`: The inertia of this view that defines how much it resists   being manipulated.
- `isEnabled`: The Boolean value that indicates whether the manipulation   gesture added by this view modifier is enabled or not.
- `onChanged`: The action to perform with each new manipulation gesture   event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:))*