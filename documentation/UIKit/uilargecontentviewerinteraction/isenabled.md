# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the large content viewer is enabled on the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var isEnabled: Bool { get }
```

#### Discussion

It isn’t necessary to check this value before adding a [`UILargeContentViewerInteraction`](uilargecontentviewerinteraction.md) to a view, but it may be helpful if you need to adjust the behavior of coexisting gesture handlers. For example, a button with a long press handler might increase its long press duration so the user can read the text in the large content viewer first.

## See Also

- [class let enabledStatusDidChangeNotification: NSNotification.Name](uilargecontentviewerinteraction/enabledstatusdidchangenotification.md)
  A notification the system posts when it enables or disables the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction/isenabled)*