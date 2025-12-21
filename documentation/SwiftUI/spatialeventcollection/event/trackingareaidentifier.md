# trackingAreaIdentifier

**Framework**: SwiftUI  
**Kind**: property

The tracking area identifier of the event, if the gesture is attached to a `CompositorLayer`, or `nil` if the event didn’t hit a tracking area or the gesture isn’t attached to a `CompositorLayer`.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var trackingAreaIdentifier: LayerRenderer.Drawable.TrackingArea.Identifier { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/trackingareaidentifier)*