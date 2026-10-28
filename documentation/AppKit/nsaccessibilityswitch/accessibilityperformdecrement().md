# accessibilityPerformDecrement()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Decrements the switch’s value.

**Availability**:
- macOS

## Declaration

```swift
optional func accessibilityPerformDecrement() -> Bool
```

```objc
- (BOOL) accessibilityPerformDecrement;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## Discussion

This method must post an [`valueChanged`](../nsaccessibility-swift.struct/notification/valuechanged.md) notification after changing the switch’s value.

## See Also

### Supporting Accessibility
- [func accessibilityPerformIncrement() -> Bool](./accessibilityperformincrement%28%29.md)
  Increments the switch’s value.
- [func accessibilityValue() -> String?](./accessibilityvalue%28%29.md)
  Returns the switch’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch/accessibilityperformdecrement())*