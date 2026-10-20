# isEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the sharing service picker item is enabled.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

#### Discussion

If [`true`](../../Swift/true.md), the sharing button is enabled.

If the sharing popover is currently visible when this property is changed to [`false`](../../Swift/false.md), the popover is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertouchbaritem/isenabled)*