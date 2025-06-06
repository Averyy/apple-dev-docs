# isSystemTrackingEnabled

**Framework**: DockKit  
**Kind**: property

An indication of whether system tracking is enabled.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isSystemTrackingEnabled: Bool { get }
```

#### Discussion

This property is `true` if system tracking is enabled; otherwise the property is `false`. To change system tracking behavior, see [`setSystemTrackingEnabled(_:)`](dockaccessorymanager/setsystemtrackingenabled(_:).md).

## See Also

- [func setSystemTrackingEnabled(Bool) async throws](dockaccessorymanager/setsystemtrackingenabled(_:).md)
  Enable and disable system tracking for camera-enabled apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessorymanager/issystemtrackingenabled)*