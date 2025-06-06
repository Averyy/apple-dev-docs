# sessionID

**Framework**: MailKit  
**Kind**: property

A unique identifier for the session.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var sessionID: UUID { get }
```

#### Discussion

A compose session’s identifier is only valid for the duration that Mail shows a compose window. If the user opens a compose window, saves it as a draft, and later reopens it, the compose session may have a different [`sessionID`](mecomposesession/sessionid.md).

## See Also

- [func reload()](mecomposesession/reload.md)
  Refreshes the compose session with the extension’s new information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesession/sessionid)*