# RealityViewLayoutOption

**Framework**: RealityKit  
**Kind**: struct

Options that specify the frame sizing and content alignment option for `RealityView`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct RealityViewLayoutOption
```

## Topics

### Type Properties
- [static let centered: RealityViewLayoutOption](realityviewlayoutoption/centered.md)
  The option that centers the visual content within a flexible frame.
- [static let fixedSize: RealityViewLayoutOption](realityviewlayoutoption/fixedsize.md)
  The option that fixes the size of the frame to equal the size of the visual content and centers the content within the new frame size.
- [static let flexible: RealityViewLayoutOption](realityviewlayoutoption/flexible.md)
  The option that applies the default layout behavior of `RealityView`, where the content is not centered and the frame is flexible (takes up as much space as the SwiftUI layout provides).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct RealityView](realityview.md)
  A view that contains RealityKit content.
- [struct RealityViewContent](realityviewcontent.md)
  The content of a visionOS reality view.
- [struct RealityViewCameraContent](realityviewcameracontent.md)
  The content of a reality view that is displayed through a camera.
- [protocol RealityViewContentProtocol](realityviewcontentprotocol.md)
  A protocol representing the content of a reality view.
- [struct RealityViewDefaultPlaceholder](realityviewdefaultplaceholder.md)
  A view that represents the default placeholder for a RealityView.
- [struct RealityViewEntityCollection](realityviewentitycollection.md)
  A collection of entities in a RealityView.
- [protocol EntityCollection](entitycollection.md)
  An ordered, mutable collection of entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewlayoutoption)*