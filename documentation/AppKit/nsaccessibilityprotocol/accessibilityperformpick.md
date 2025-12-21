# accessibilityPerformPick()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Selects the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformPick() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Use this method on selectable elements, such as a menu item.

## See Also

- [func accessibilityPerformPress() -> Bool](nsaccessibilityprotocol/accessibilityperformpress.md)
  Simulates clicking the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformpick())*