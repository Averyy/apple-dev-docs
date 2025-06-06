# accessibilityPerformCancel()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Cancels the current operation.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformCancel() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## See Also

- [func accessibilityPerformConfirm() -> Bool](nsaccessibilityprotocol/accessibilityperformconfirm.md)
  Simulates pressing Return in the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformcancel())*