# handler(for:)

**Framework**: MailKit  
**Kind**: method

Returns an object that participates in the composition of a mail message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
optional func handler(for session: MEComposeSession) -> any MEComposeSessionHandler
```

#### Return Value

An object that participates in the composition of a mail message.

#### Discussion

MailKit invokes this method for each compose window it displays.

## Parameters

- `session`: An object that represents a mail compose window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextension/handler(for:))*