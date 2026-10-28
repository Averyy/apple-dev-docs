# accessibilityPerformPress()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Simulates clicking the button.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityPerformPress() -> Bool
```

```objc
- (BOOL) accessibilityPerformPress;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## See Also

### Supporting Accessibility
- [func accessibilityLabel() -> String?](./accessibilitylabel%28%29.md)
  Returns a short description of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton/accessibilityperformpress())*