# accessibilityPerformDecrement()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decrements the stepper’s value.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityPerformDecrement() -> Bool
```

```objc
- (BOOL) accessibilityPerformDecrement;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## Discussion

This method must post an [`valueChanged`](../nsaccessibility-swift.struct/notification/valuechanged.md) notification after changing the stepper’s value.

## See Also

### Supporting Accessibility
- [func accessibilityLabel() -> String?](./accessibilitylabel%28%29.md)
  Returns a short description of the stepper.
- [func accessibilityPerformIncrement() -> Bool](./accessibilityperformincrement%28%29.md)
  Increments the stepper’s value.
- [func accessibilityValue() -> Any?](./accessibilityvalue%28%29.md)
  Returns the stepper’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper/accessibilityperformdecrement())*