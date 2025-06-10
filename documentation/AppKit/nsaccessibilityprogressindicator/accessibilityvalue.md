# accessibilityValue()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the progress indicator’s value.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityValue() -> NSNumber?
```

#### Return Value

The value of the progress indicator.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityValue`](nsaccessibility-c.protocol/accessibilityvalue.md) property.

> **Note**:  This class must also post an [`valueChanged`](nsaccessibility-swift.struct/notification/valuechanged.md) notification whenever its value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprogressindicator/accessibilityvalue())*