# accessibilityPerformDecrement()

**Framework**: AppKit  
**Kind**: method

Decrements the switch’s value.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func accessibilityPerformDecrement() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

This method must post an [`valueChanged`](nsaccessibility-swift.struct/notification/valuechanged.md) notification after changing the switch’s value.

## See Also

- [func accessibilityPerformIncrement() -> Bool](nsaccessibilityswitch/accessibilityperformincrement.md)
  Increments the switch’s value.
- [func accessibilityValue() -> String?](nsaccessibilityswitch/accessibilityvalue.md)
  Returns the switch’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch/accessibilityperformdecrement())*