# dismiss()

**Framework**: GameKit  
**Kind**: method

Hides the peer picker dialog.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func dismiss()
```

#### Discussion

The controller’s delegate is responsible for dismissing the peer picker when it is no longer needed.

On iOS 3.1 or later, the peer picker is retained when it is shown, and autoreleased when it is dismissed.

## See Also

- [func show()](gkpeerpickercontroller/show.md)
  Displays the peer picker dialog to the user.
- [var isVisible: Bool](gkpeerpickercontroller/isvisible.md)
  A Boolean value that indicates whether the picker dialog is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller/dismiss())*