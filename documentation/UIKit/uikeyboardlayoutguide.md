# UIKeyboardLayoutGuide

**Framework**: UIKit  
**Kind**: class

A layout guide that represents the space the keyboard occupies in your app’s layout.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIKeyboardLayoutGuide
```

#### Overview

Configure the keyboard layout guide, and activate or deactivate constraints so your app’s layout adjusts to the keyboard in different situations. See [`Adjusting your layout with keyboard layout guide`](adjusting-your-layout-with-keyboard-layout-guide.md) for an example of how to dynamically respond to keyboard presentation, dismissal, and movement.

## Topics

### Supporting floating and undocked keyboards
- [var followsUndockedKeyboard: Bool](uikeyboardlayoutguide/followsundockedkeyboard.md)
  A Boolean value that determines if the layout guide tracks the keyboard when it’s undocked from the bottom of the screen.
### Adjusting dismissal sensitivity
- [var keyboardDismissPadding: CGFloat](uikeyboardlayoutguide/keyboarddismisspadding.md)
  A value that adds padding above the keyboard to increase the size of the touch area for the scrolling dismissal gesture.
### Configuring safe area usage
- [var usesBottomSafeArea: Bool](uikeyboardlayoutguide/usesbottomsafearea.md)
  A Boolean value that indicates whether the layout guide uses the view’s safe area layout guide.

## Relationships

### Inherits From
- [UITrackingLayoutGuide](uitrackinglayoutguide.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## See Also

- [Adjusting your layout with keyboard layout guide](adjusting-your-layout-with-keyboard-layout-guide.md)
  Respond dynamically to keyboard movement by using the tracking features of the keyboard layout guide.
- [class UITrackingLayoutGuide](uitrackinglayoutguide.md)
  A layout guide that automatically activates and deactivates layout constraints depending on its proximity to edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide)*