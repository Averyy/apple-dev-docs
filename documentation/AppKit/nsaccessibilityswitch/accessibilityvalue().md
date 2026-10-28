# accessibilityValue()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the switch’s value.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityValue() -> String?
```

```objc
- (NSString *) accessibilityValue;
```

## Return Value

The value for the switch.

## Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityValue`](../nsaccessibility-c.protocol/accessibilityvalue.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityPerformDecrement() -> Bool](./accessibilityperformdecrement%28%29.md)
  Decrements the switch’s value.
- [func accessibilityPerformIncrement() -> Bool](./accessibilityperformincrement%28%29.md)
  Increments the switch’s value.
### Related Documentation
- [accessibilityValue](../nsaccessibility-c.protocol/accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch/accessibilityvalue())*