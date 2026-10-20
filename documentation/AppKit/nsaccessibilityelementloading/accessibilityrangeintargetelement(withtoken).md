# accessibilityRangeInTargetElement(withToken:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the range that specifies the area of interest in text-based accessibility elements with the specified load token.

**Availability**:
- macOS 10.13+

## Declaration

```swift
optional func accessibilityRangeInTargetElement(withToken token: NSAccessibilityLoadingToken) -> NSRange
```

```objc
- (NSRange) accessibilityRangeInTargetElementWithToken:(NSAccessibilityLoadingToken) token;
```

## See Also

### Supporting Accessibility
- [func accessibilityElement(withToken: NSAccessibilityLoadingToken) -> (any NSAccessibilityElementProtocol)?](./accessibilityelement%28withtoken%29.md)
  Loads the target accessibility element with the specified load token.
- [typealias NSAccessibilityLoadingToken](../nsaccessibilityloadingtoken.md)
  A token type for loading accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementloading/accessibilityrangeintargetelement(withtoken:))*