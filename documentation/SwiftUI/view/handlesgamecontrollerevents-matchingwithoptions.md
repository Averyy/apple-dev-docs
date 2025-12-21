# handlesGameControllerEvents(matching:withOptions:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the game controllers events which should be delivered through the GameController framework when the view or one of its descendants has focus.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func handlesGameControllerEvents(matching types: GCUIEventTypes, withOptions options: GameControllerEventHandlingOptions?) -> some View
```

#### Discussion

```swift
SpriteView(scene: MyGameScene())
.handlesGameControllerEvents(matching: .gamepad, withOptions: .defaultOptions)
.focused(true)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/handlesgamecontrollerevents(matching:withoptions:))*