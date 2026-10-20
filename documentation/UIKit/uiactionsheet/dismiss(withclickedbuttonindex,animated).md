# dismiss(withClickedButtonIndex:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the action sheet immediately using an optional animation.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
func dismiss(withClickedButtonIndex buttonIndex: Int, animated: Bool)
```

```objc
- (void) dismissWithClickedButtonIndex:(NSInteger) buttonIndex animated:(BOOL) animated;
```

#### Discussion

You can use this method to dismiss the action sheet programmatically as needed. The action sheet also calls this method itself in response to the user tapping one of the buttons in the action sheet.

In iOS 4.0, you may want to call this method whenever your application moves to the background. An action sheet is not dismissed automatically when an application moves to the background. This behavior differs from previous versions of the operating system, where they were canceled automatically when the application was terminated. Dismissing the action sheet gives your application a chance to save changes or abort the operation and perform any necessary cleanup in case your application is terminated later.

## Parameters

- `buttonIndex`: The index of the button that was clicked. Button indices start at `0`.
- `animated`: Specify [`true`](../../Swift/true.md) to animate the dismissal of the action sheet or [`false`](../../Swift/false.md) to remove the action sheet without an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/dismiss(withclickedbuttonindex:animated:))*