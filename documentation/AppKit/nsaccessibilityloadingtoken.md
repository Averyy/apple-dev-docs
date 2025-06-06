# NSAccessibilityLoadingToken

**Framework**: AppKit  
**Kind**: typealias

A token type for loading accessibility elements.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias NSAccessibilityLoadingToken = any NSSecureCoding & NSObjectProtocol
```

## See Also

- [func accessibilityElement(withToken: NSAccessibilityLoadingToken) -> (any NSAccessibilityElementProtocol)?](nsaccessibilityelementloading/accessibilityelement(withtoken:).md)
  Loads the target accessibility element with the specified load token.
- [func accessibilityRangeInTargetElement(withToken: NSAccessibilityLoadingToken) -> NSRange](nsaccessibilityelementloading/accessibilityrangeintargetelement(withtoken:).md)
  Returns the range that specifies the area of interest in text-based accessibility elements with the specified load token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityloadingtoken)*