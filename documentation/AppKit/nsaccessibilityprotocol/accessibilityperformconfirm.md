# accessibilityPerformConfirm()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Simulates pressing Return in the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformConfirm() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Use this method on elements that take keyboard input, such as a text field.

## See Also

- [func accessibilityPerformCancel() -> Bool](nsaccessibilityprotocol/accessibilityperformcancel.md)
  Cancels the current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformconfirm())*