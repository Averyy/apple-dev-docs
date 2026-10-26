# accessibilityValue()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the stepper’s value.

**Availability**:
- macOS

## Declaration

```swift
optional func accessibilityValue() -> Any?
```

```objc
- (id) accessibilityValue;
```

#### Return Value

The value for the stepper.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityValue`](../nsaccessibility-c.protocol/accessibilityvalue.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityLabel() -> String?](./accessibilitylabel%28%29.md)
  Returns a short description of the stepper.
- [func accessibilityPerformDecrement() -> Bool](./accessibilityperformdecrement%28%29.md)
  Decrements the stepper’s value.
- [func accessibilityPerformIncrement() -> Bool](./accessibilityperformincrement%28%29.md)
  Increments the stepper’s value.
### Related Documentation
- [accessibilityValue](../nsaccessibility-c.protocol/accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper/accessibilityvalue())*