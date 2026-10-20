# accessibilityPerformDecrement()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decrements the accessibility element’s value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformDecrement() -> Bool
```

```objc
- (BOOL) accessibilityPerformDecrement;
```

#### Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Use this method on elements that have an adjustable [`accessibilityValue`](../nsaccessibility-c.protocol/accessibilityvalue.md) property.

## See Also

### Incrementing, decrementing, and deleting values
- [func accessibilityIncrementButton() -> Any?](./accessibilityincrementbutton%28%29.md)
  Returns the increment button for the stepper accessibility element.
- [func setAccessibilityIncrementButton(Any?)](./setaccessibilityincrementbutton%28_%29.md)
  Sets the increment button for the stepper accessibility element.
- [func accessibilityDecrementButton() -> Any?](./accessibilitydecrementbutton%28%29.md)
  Returns the decrement button for the stepper accessibility element.
- [func setAccessibilityDecrementButton(Any?)](./setaccessibilitydecrementbutton%28_%29.md)
  Sets the decrement button for the stepper accessibility element.
- [func accessibilityPerformIncrement() -> Bool](./accessibilityperformincrement%28%29.md)
  Increments the accessibility element’s value.
- [func accessibilityPerformDelete() -> Bool](./accessibilityperformdelete%28%29.md)
  Deletes the accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformdecrement())*