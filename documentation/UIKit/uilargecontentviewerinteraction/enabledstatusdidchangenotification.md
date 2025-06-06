# enabledStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification the system posts when it enables or disables the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let enabledStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

Observe this notification to know whether to enable or disable your custom interaction behaviors. For example, if you add an interaction to a button that needs to cooperate with other gesture recognizers when the large content viewer settings are enabled. This notification lets you enable or disable the interaction accordingly.

## See Also

- [class var isEnabled: Bool](uilargecontentviewerinteraction/isenabled.md)
  A Boolean value that indicates whether the large content viewer is enabled on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction/enabledstatusdidchangenotification)*