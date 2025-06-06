# isValid

**Framework**: BrowserEngineKit  
**Kind**: property

A Boolean that indicates whether the operating system has granted the capability to the browser extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
var isValid: Bool { get }
```

#### Overview

If the operating system has granted this capability to the browser extension process and you haven’t called [`invalidate()`](processcapability/grant/invalidate().md), then this property’s value is `true`; otherwise, it’s false.

## See Also

- [func invalidate()](processcapability/grant/invalidate.md)
  Invalidates the grant, removing the capability from the process it was granted to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/grant/isvalid)*