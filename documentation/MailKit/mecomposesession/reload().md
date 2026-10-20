# reload()

**Framework**: MailKit  
**Kind**: method  
**Role**: Instance Method

Refreshes the compose session with the extension’s new information.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func reload()
```

```objc
- (void) reloadSession;
```

#### Discussion

Call this method from your extension to regenerate address annotations to replace existing annotations for the session. In response, MailKit invokes [`annotateAddressesForSession(_:completion:)`](../mecomposesessionhandler/annotateaddressesforsession%28_,completion%29.md) for all addresses in the To, Cc, and Bcc fields.

## See Also

### Managing Compose Sessions
- [var sessionID: UUID](./sessionid.md)
  A unique identifier for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesession/reload())*