# screenArea(_:)

**Framework**: RealityKit  
**Kind**: method

Switch levels based on projected screen area (0.0 = invisible, 1.0 = fills screen).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func screenArea(_ thresholds: [Float]) -> LevelOfDetailComponent.SelectionStrategy
```

#### Discussion

Each threshold specifies the minimum screen area for a level, in descending order.

## See Also

- [static func cameraDistance([Float]) -> LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/selectionstrategy/cameradistance(_:).md)
  Switch levels based on distance from the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy/screenarea(_:))*