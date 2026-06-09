# screenArea(_:)

**Framework**: RealityKit  
**Kind**: method

Switch levels based on projected screen area (0.0 = invisible, 1.0 = fills screen).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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