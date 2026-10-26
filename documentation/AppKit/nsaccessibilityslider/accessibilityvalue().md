# accessibilityValue()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the slider’s value.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityValue() -> Any?
```

```objc
- (id) accessibilityValue;
```

#### Return Value

The value for the slider.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityValue`](../nsaccessibility-c.protocol/accessibilityvalue.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityLabel() -> String?](./accessibilitylabel%28%29.md)
  Returns a short description of the slider.
- [func accessibilityPerformDecrement() -> Bool](./accessibilityperformdecrement%28%29.md)
  Decrements the slider’s value.
- [func accessibilityPerformIncrement() -> Bool](./accessibilityperformincrement%28%29.md)
  Increments the slider’s value.
### Related Documentation
- [accessibilityValue](../nsaccessibility-c.protocol/accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityslider/accessibilityvalue())*