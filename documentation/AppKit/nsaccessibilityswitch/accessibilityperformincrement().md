# accessibilityPerformIncrement()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Increments the switch’s value.

**Availability**:
- macOS

## Declaration

```swift
optional func accessibilityPerformIncrement() -> Bool
```

```objc
- (BOOL) accessibilityPerformIncrement;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## Discussion

This method must post an [`valueChanged`](../nsaccessibility-swift.struct/notification/valuechanged.md) notification after changing the switch’s value.

## See Also

### Supporting Accessibility
- [func accessibilityPerformDecrement() -> Bool](./accessibilityperformdecrement%28%29.md)
  Decrements the switch’s value.
- [func accessibilityValue() -> String?](./accessibilityvalue%28%29.md)
  Returns the switch’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch/accessibilityperformincrement())*