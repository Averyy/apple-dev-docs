# dismiss(withClickedButtonIndex:animated:)

**Framework**: UIKit  
**Kind**: method

Dismisses the receiver, optionally with animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func dismiss(withClickedButtonIndex buttonIndex: Int, animated: Bool)
```

#### Discussion

In iOS 4.0, you may want to call this method whenever your application moves to the background. An alert view is not dismissed automatically when an application moves to the background. This behavior differs from previous versions of the operating system, where they were canceled automatically when the application was terminated. Dismissing the alert view gives your application a chance to save changes or abort the operation and perform any necessary cleanup in case your application is terminated later.

## Parameters

- `buttonIndex`: The index of the button that was clicked just before invoking this method. The button indices start at  .
- `animated`:   if the receiver should be removed by animating it first; otherwise,   if it should be removed immediately with no animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/dismiss(withclickedbuttonindex:animated:))*