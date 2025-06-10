# mapCameraKeyframeAnimator(trigger:keyframes:)

**Framework**: Journaling Suggestions  
**Kind**: method

Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.

**Availability**:
- iOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapCameraKeyframeAnimator(trigger: some Equatable, @KeyframesBuilder<MapCamera> keyframes: @escaping (MapCamera) -> some Keyframes<MapCamera>) -> some View
```

#### Discussion

When the trigger value changes, the map calls the `keyframes` closure to generate the keyframes that will animate the camera. The animation will continue for the duration of the keyframes that you specify.

If the user performs a gesture while the animation is in progress, the animation will be immediately removed, allowing the interaction to take control of the camera.

## Parameters

- `trigger`: A value to observe for changes.
- `keyframes`: A keyframes builder closure that is called when starting   a new keyframe animation. The current map camera is provided as the   only parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapcamerakeyframeanimator(trigger:keyframes:))*