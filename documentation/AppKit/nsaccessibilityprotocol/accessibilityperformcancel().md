# accessibilityPerformCancel()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Cancels the current operation.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformCancel() -> Bool
```

```objc
- (BOOL) accessibilityPerformCancel;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## See Also

### Confirming and canceling operations
- [func accessibilityPerformConfirm() -> Bool](./accessibilityperformconfirm%28%29.md)
  Simulates pressing Return in the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformcancel())*