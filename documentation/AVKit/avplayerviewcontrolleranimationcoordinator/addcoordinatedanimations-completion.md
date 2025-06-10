# addCoordinatedAnimations(_:completion:)

**Framework**: AVKit  
**Kind**: method  
**Required**: Yes

Adds animations to perform alongside the playback controls’ visibility animation.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
func addCoordinatedAnimations(_ animations: (() -> Void)?) async -> Bool
```

## Parameters

- `animations`: The animations to execute.
- `completion`: A closure to execute after the main animation completes. The system runs the specified animations in the same animation context as the main animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrolleranimationcoordinator/addcoordinatedanimations(_:completion:))*