# isEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that specifies whether the sharing service picker item is enabled.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the sharing button is enabled.

If the sharing popover is currently visible when this property is changed to [`false`](https://developer.apple.com/documentation/swift/false), the popover is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertouchbaritem/isenabled)*