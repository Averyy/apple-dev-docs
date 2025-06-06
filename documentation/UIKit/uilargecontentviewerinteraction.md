# UILargeContentViewerInteraction

**Framework**: UIKit  
**Kind**: class

An interaction that enables a gesture to present the large content viewer for cases when supporting the largest dynamic type sizes isn’t appropriate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UILargeContentViewerInteraction
```

#### Overview

Don’t use the large content viewer as a replacement for proper Dynamic Type support. For example, Dynamic Type allows items in a list to grow or shrink vertically to accommodate the user’s preferred font size. Rely on the large content viewer only in situations where items must remain small due to unavoidable design constraints. For example, buttons in a tab bar remain small to leave more room for the main app content.

For more information about allowing your app’s content to adjust to varying font sizes, see [`Add Dynamic Type support`](creating-self-sizing-table-view-cells#Add-Dynamic-Type-support.md) and the [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/accessibility/overview/text-size-and-weight/).

## Topics

### Creating large content viewer interactions
- [init(delegate: (any UILargeContentViewerInteractionDelegate)?)](uilargecontentviewerinteraction/init(delegate:).md)
  Creates an interaction object with the specified delegate.
### Customizing large content viewer interactions
- [var delegate: (any UILargeContentViewerInteractionDelegate)?](uilargecontentviewerinteraction/delegate.md)
  An object that can fine-tune the large content viewer interactions, especially in the presence of other gesture recognizers.
- [var gestureRecognizerForExclusionRelationship: UIGestureRecognizer](uilargecontentviewerinteraction/gesturerecognizerforexclusionrelationship.md)
  A gesture recognizer that you can use to set up simultaneous recognition or failure relationships with other gesture recognizers.
### Detecting the large content viewer
- [class var isEnabled: Bool](uilargecontentviewerinteraction/isenabled.md)
  A Boolean value that indicates whether the large content viewer is enabled on the device.
- [class let enabledStatusDidChangeNotification: NSNotification.Name](uilargecontentviewerinteraction/enabledstatusdidchangenotification.md)
  A notification the system posts when it enables or disables the large content viewer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [protocol UILargeContentViewerInteractionDelegate](uilargecontentviewerinteractiondelegate.md)
  An object that customizes the behavior of the large content viewer interactions.
- [protocol UILargeContentViewerItem](uilargecontentvieweritem.md)
  Methods that provide details about how to display your custom content in the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction)*