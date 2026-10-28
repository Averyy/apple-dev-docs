# accessibilityPerformPress()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Simulates clicking the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformPress() -> Bool
```

```objc
- (BOOL) accessibilityPerformPress;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## Discussion

Use this method on elements that behave like buttons.

## See Also

### Selecting elements
- [func accessibilityPerformPick() -> Bool](./accessibilityperformpick%28%29.md)
  Selects the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformpress())*