# portal

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The viewport configuration to use when the player displays immersive content in a portal.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
var portal: AVPortalViewport? { get set }
```

```objc
@property (nonatomic, strong, nullable) AVPortalViewport * portal;
```

#### Discussion

Set this property to customize how content appears within a portal frame. When this property is `nil`, the system uses default portal settings.

> **Note**: Spatial videos don’t support portal viewport settings.

## See Also

### Configuring the portal viewport
- [class AVPortalViewport](../avportalviewport.md)
  An object that defines the visual parameters for content displayed within a portal frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avviewport/portal)*