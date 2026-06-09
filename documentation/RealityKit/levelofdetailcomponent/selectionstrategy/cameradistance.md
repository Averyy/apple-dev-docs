# cameraDistance(_:)

**Framework**: RealityKit  
**Kind**: method

Switch levels based on distance from the camera.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func cameraDistance(_ thresholds: [Float]) -> LevelOfDetailComponent.SelectionStrategy
```

#### Discussion

Each threshold specifies the maximum camera distance for a level. The last threshold is typically `.infinity` to catch all remaining distances.

## See Also

- [static func screenArea([Float]) -> LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/selectionstrategy/screenarea(_:).md)
  Switch levels based on projected screen area (0.0 = invisible, 1.0 = fills screen).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy/cameradistance(_:))*