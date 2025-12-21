# accessibilityPerformDecrement()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Decrements the slider’s value.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityPerformDecrement() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

This method must post an [`valueChanged`](nsaccessibility-swift.struct/notification/valuechanged.md) notification after changing the slider’s value.

## See Also

- [func accessibilityLabel() -> String?](nsaccessibilityslider/accessibilitylabel.md)
  Returns a short description of the slider.
- [func accessibilityPerformIncrement() -> Bool](nsaccessibilityslider/accessibilityperformincrement.md)
  Increments the slider’s value.
- [func accessibilityValue() -> Any?](nsaccessibilityslider/accessibilityvalue.md)
  Returns the slider’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityslider/accessibilityperformdecrement())*