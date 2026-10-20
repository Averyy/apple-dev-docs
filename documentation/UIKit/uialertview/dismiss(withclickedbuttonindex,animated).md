# dismiss(withClickedButtonIndex:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the receiver, optionally with animation.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
func dismiss(withClickedButtonIndex buttonIndex: Int, animated: Bool)
```

```objc
- (void) dismissWithClickedButtonIndex:(NSInteger) buttonIndex animated:(BOOL) animated;
```

#### Discussion

In iOS 4.0, you may want to call this method whenever your application moves to the background. An alert view is not dismissed automatically when an application moves to the background. This behavior differs from previous versions of the operating system, where they were canceled automatically when the application was terminated. Dismissing the alert view gives your application a chance to save changes or abort the operation and perform any necessary cleanup in case your application is terminated later.

## Parameters

- `buttonIndex`: The index of the button that was clicked just before invoking this method. The button indices start at `0`.
- `animated`: [`true`](../../Swift/true.md) if the receiver should be removed by animating it first; otherwise, [`false`](../../Swift/false.md) if it should be removed immediately with no animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/dismiss(withclickedbuttonindex:animated:))*