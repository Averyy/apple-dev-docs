# dismiss()

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Hides the peer picker dialog.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use MCBrowserViewController from the MultipeerConnectivity framework.

## Declaration

```swift
func dismiss()
```

```objc
- (void) dismiss;
```

#### Discussion

The controller’s delegate is responsible for dismissing the peer picker when it is no longer needed.

On iOS 3.1 or later, the peer picker is retained when it is shown, and autoreleased when it is dismissed.

## See Also

### Displaying the Picker Dialog
- [func show()](./show%28%29.md)
  Displays the peer picker dialog to the user.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the picker dialog is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller/dismiss())*