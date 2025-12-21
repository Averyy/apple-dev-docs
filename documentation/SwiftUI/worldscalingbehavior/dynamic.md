# dynamic

**Framework**: SwiftUI  
**Kind**: property

The window will scale up as it moves further away, maintaining the same angular size.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static var dynamic: WorldScalingBehavior { get }
```

#### Discussion

Prefer dynamic window scaling for windows that display dense UI or a lot of text. Using dynamic scaling ensures that controls and text remain at a comfortable size regardless of the window’s position.

For further information, see [`Spatial layout`](https://developer.apple.com/design/Human-Interface-Guidelines/spatial-layout#Scale) in the Human Interface Guidelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/worldscalingbehavior/dynamic)*