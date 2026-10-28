# accessibilityPerformPick()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Selects the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformPick() -> Bool
```

```objc
- (BOOL) accessibilityPerformPick;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## Discussion

Use this method on selectable elements, such as a menu item.

## See Also

### Selecting elements
- [func accessibilityPerformPress() -> Bool](./accessibilityperformpress%28%29.md)
  Simulates clicking the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformpick())*