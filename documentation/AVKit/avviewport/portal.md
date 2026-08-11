# portal

**Framework**: AVKit  
**Kind**: property

The viewport configuration to use when immersive content is displayed in a portal.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var portal: AVPortalViewport? { get set }
```

#### Discussion

Set this property to customize how content appears within a portal frame. When nil, the system uses default portal settings.

> **Note**: Spatial videos do not support portal viewport settings.

## See Also

- [class AVPortalViewport](avportalviewport.md)
  Defines the visual parameters for content displayed within a portal frame. Use this configuration to create cinematic viewing experiences with custom framing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avviewport/portal)*