# accessibilityElement(withToken:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Loads the target accessibility element with the specified load token.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func accessibilityElement(withToken token: NSAccessibilityLoadingToken) -> (any NSAccessibilityElementProtocol)?
```

```objc
- (id<NSAccessibilityElement>) accessibilityElementWithToken:(NSAccessibilityLoadingToken) token;
```

## See Also

### Supporting Accessibility
- [func accessibilityRangeInTargetElement(withToken: NSAccessibilityLoadingToken) -> NSRange](./accessibilityrangeintargetelement%28withtoken%29.md)
  Returns the range that specifies the area of interest in text-based accessibility elements with the specified load token.
- [typealias NSAccessibilityLoadingToken](../nsaccessibilityloadingtoken.md)
  A token type for loading accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementloading/accessibilityelement(withtoken:))*