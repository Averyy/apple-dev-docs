# thermalStateDidChangeNotification

**Framework**: Foundation  
**Kind**: property

Posts when the thermal state of the system changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.10.3+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class let thermalStateDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is a [`ProcessInfo`](processinfo.md) instance.

To receive [`thermalStateDidChangeNotification`](processinfo/thermalstatedidchangenotification.md), you must access the [`thermalState`](processinfo/thermalstate-swift.property.md) prior to registering for the notification.

## See Also

- [static let NSProcessInfoPowerStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md)
  Posts when the power state of a device changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/thermalstatedidchangenotification)*