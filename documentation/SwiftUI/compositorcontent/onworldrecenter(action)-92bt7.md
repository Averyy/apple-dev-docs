# onWorldRecenter(action:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when recentering the content with the digital crown.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func onWorldRecenter(action: @escaping @MainActor (WorldRecenterPhase) -> Void) -> some CompositorContent
```

**Other overloads**:

```swift
nonisolated
func onWorldRecenter(action: @escaping @MainActor () -> Void) -> some CompositorContent
```

## Discussion

When the user recenters their content, first it will fade out, and the action will be called with a ‘began’ phase. After the app is repositioned, the action will be called again with an ‘ended’ phase and the app will fade back in. These actions will be called if the app is not backgrounded or suspended.

## Parameters

- `action`: A closure to run when the content is recentered. The closure takes a `phase` parameter that indicates the phase of the recentering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/onworldrecenter(action:)-92bt7)*