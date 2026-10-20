# isSystemTrackingEnabled

**Framework**: DockKit  
**Kind**: property  
**Role**: Instance Property

An indication of whether system tracking is enabled.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var isSystemTrackingEnabled: Bool { get }
```

#### Discussion

This property is `true` if system tracking is enabled; otherwise the property is `false`. To change system tracking behavior, see [`setSystemTrackingEnabled(_:)`](./setsystemtrackingenabled%28_%29.md).

## See Also

### Changing tracking behavior
- [func setSystemTrackingEnabled(Bool) async throws](./setsystemtrackingenabled%28_%29.md)
  Enable and disable system tracking for camera-enabled apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessorymanager/issystemtrackingenabled)*