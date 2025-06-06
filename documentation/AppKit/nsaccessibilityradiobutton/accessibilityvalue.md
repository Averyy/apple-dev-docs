# accessibilityValue()

**Framework**: Appkit  
**Kind**: method  
**Required**: Yes

Returns the radio button’s value.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityValue() -> NSNumber?
```

#### Return Value

`@YES` if selected; otherwise, `@NO`.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityValue`](nsaccessibility-c.protocol/accessibilityvalue.md) property.

> **Note**:  This class must also post an [`valueChanged`](nsaccessibility-swift.struct/notification/valuechanged.md) notification whenever its value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityradiobutton/accessibilityvalue())*