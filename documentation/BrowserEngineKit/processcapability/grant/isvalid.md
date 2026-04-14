# isValid

**Framework**: BrowserEngineKit  
**Kind**: property

A Boolean value that indicates whether the system honors a granted capability for the browser extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

If the system grants this capability to the browser extension process and you haven’t called [`invalidate()`](processcapability/grant/invalidate().md), then this property is `true`; otherwise, it’s false.

## See Also

- [func invalidate()](processcapability/grant/invalidate.md)
  Invalidates the grant, removing the capability from the process it was granted to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/grant/isvalid)*