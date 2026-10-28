# accessibilityPerformIncrement()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Increments the slider’s value.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityPerformIncrement() -> Bool
```

```objc
- (BOOL) accessibilityPerformIncrement;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## Discussion

This method must post an [`valueChanged`](../nsaccessibility-swift.struct/notification/valuechanged.md) notification after changing the slider’s value.

## See Also

### Supporting Accessibility
- [func accessibilityLabel() -> String?](./accessibilitylabel%28%29.md)
  Returns a short description of the slider.
- [func accessibilityPerformDecrement() -> Bool](./accessibilityperformdecrement%28%29.md)
  Decrements the slider’s value.
- [func accessibilityValue() -> Any?](./accessibilityvalue%28%29.md)
  Returns the slider’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityslider/accessibilityperformincrement())*