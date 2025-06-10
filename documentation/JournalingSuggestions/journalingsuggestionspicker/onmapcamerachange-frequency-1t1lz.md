# onMapCameraChange(frequency:_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Performs an action when Map camera framing changes

**Availability**:
- iOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func onMapCameraChange(frequency: MapCameraUpdateFrequency = .onEnd, _ action: @escaping (MapCameraUpdateContext) -> Void) -> some View
```

## Parameters

- `frequency`: How frequently the action should be performed during a camera interaction.
- `action`: A closure to run when the camera framing changes.   The closure takes a   parameter that indicates   the camera and the framed area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/onmapcamerachange(frequency:_:)-1t1lz)*