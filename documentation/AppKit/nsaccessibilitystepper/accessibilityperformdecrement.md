# accessibilityPerformDecrement()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Decrements the stepper’s value.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityPerformDecrement() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

This method must post an [`valueChanged`](nsaccessibility-swift.struct/notification/valuechanged.md) notification after changing the stepper’s value.

## See Also

- [func accessibilityLabel() -> String?](nsaccessibilitystepper/accessibilitylabel.md)
  Returns a short description of the stepper.
- [func accessibilityPerformIncrement() -> Bool](nsaccessibilitystepper/accessibilityperformincrement.md)
  Increments the stepper’s value.
- [func accessibilityValue() -> Any?](nsaccessibilitystepper/accessibilityvalue.md)
  Returns the stepper’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper/accessibilityperformdecrement())*