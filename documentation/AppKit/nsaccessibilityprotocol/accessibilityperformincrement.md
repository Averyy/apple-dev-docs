# accessibilityPerformIncrement()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Increments the accessibility element’s value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformIncrement() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Use this method on elements that have an adjustable [`accessibilityValue`](nsaccessibility-c.protocol/accessibilityvalue.md) property.

## See Also

- [func accessibilityIncrementButton() -> Any?](nsaccessibilityprotocol/accessibilityincrementbutton.md)
  Returns the increment button for the stepper accessibility element.
- [func setAccessibilityIncrementButton(Any?)](nsaccessibilityprotocol/setaccessibilityincrementbutton(_:).md)
  Sets the increment button for the stepper accessibility element.
- [func accessibilityDecrementButton() -> Any?](nsaccessibilityprotocol/accessibilitydecrementbutton.md)
  Returns the decrement button for the stepper accessibility element.
- [func setAccessibilityDecrementButton(Any?)](nsaccessibilityprotocol/setaccessibilitydecrementbutton(_:).md)
  Sets the decrement button for the stepper accessibility element.
- [func accessibilityPerformDecrement() -> Bool](nsaccessibilityprotocol/accessibilityperformdecrement.md)
  Decrements the accessibility element’s value.
- [func accessibilityPerformDelete() -> Bool](nsaccessibilityprotocol/accessibilityperformdelete.md)
  Deletes the accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformincrement())*