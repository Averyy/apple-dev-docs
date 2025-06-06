# handlesGameControllerEvents(matching:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func handlesGameControllerEvents(matching types: GCUIEventTypes) -> some View
```

#### Discussion

```swift
SpriteView(scene: MyGameScene())
.handlesGameControllerEvents(matching: .gamepad)
.focused(true)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/handlesgamecontrollerevents(matching:))*