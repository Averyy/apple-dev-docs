# promptsUserIfNeeded

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether to display errors, authentication requests, or other UI elements to the user.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var promptsUserIfNeeded: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the system presents a user interface to request or display relevant information. The system waits until the user dismisses the UI before calling any relevant completion handlers. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/promptsuserifneeded)*