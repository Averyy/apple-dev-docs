# NSAccessibilityLoadingToken

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

A token type for loading accessibility elements.

**Availability**:
- macOS

## Declaration

```swift
typealias NSAccessibilityLoadingToken = any NSSecureCoding & NSObjectProtocol
```

```c
typedef id<NSObject,NSSecureCoding> NSAccessibilityLoadingToken;
```

## See Also

### Supporting Accessibility
- [func accessibilityElement(withToken: NSAccessibilityLoadingToken) -> (any NSAccessibilityElementProtocol)?](./nsaccessibilityelementloading/accessibilityelement%28withtoken%29.md)
  Loads the target accessibility element with the specified load token.
- [func accessibilityRangeInTargetElement(withToken: NSAccessibilityLoadingToken) -> NSRange](./nsaccessibilityelementloading/accessibilityrangeintargetelement%28withtoken%29.md)
  Returns the range that specifies the area of interest in text-based accessibility elements with the specified load token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityloadingtoken)*