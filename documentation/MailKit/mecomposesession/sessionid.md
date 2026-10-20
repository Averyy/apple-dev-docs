# sessionID

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the session.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var sessionID: UUID { get }
```

```objc
@property (nonatomic, strong, readonly) NSUUID * sessionID;
```

#### Discussion

A compose session’s identifier is only valid for the duration that Mail shows a compose window. If the user opens a compose window, saves it as a draft, and later reopens it, the compose session may have a different [`sessionID`](./sessionid.md).

## See Also

### Managing Compose Sessions
- [func reload()](./reload%28%29.md)
  Refreshes the compose session with the extension’s new information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesession/sessionid)*