# accessibilityPerformConfirm()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Simulates pressing Return in the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformConfirm() -> Bool
```

```objc
- (BOOL) accessibilityPerformConfirm;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## Discussion

Use this method on elements that take keyboard input, such as a text field.

## See Also

### Confirming and canceling operations
- [func accessibilityPerformCancel() -> Bool](./accessibilityperformcancel%28%29.md)
  Cancels the current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformconfirm())*