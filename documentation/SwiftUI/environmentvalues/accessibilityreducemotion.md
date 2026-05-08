# accessibilityReduceMotion

**Framework**: SwiftUI  
**Kind**: property

Whether the system preference for Reduce Motion is enabled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var accessibilityReduceMotion: Bool { get }
```

#### Discussion

If this property’s value is true, UI should avoid large animations, especially those that simulate the third dimension.

## See Also

- [var accessibilityDimFlashingLights: Bool](environmentvalues/accessibilitydimflashinglights.md)
  Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [var accessibilityPlayAnimatedImages: Bool](environmentvalues/accessibilityplayanimatedimages.md)
  Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion)*