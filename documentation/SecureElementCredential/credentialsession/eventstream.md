# eventStream

**Framework**: SecureElementCredential  
**Kind**: property

An asynchronous stream of session events.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
var eventStream: AsyncStream<CredentialSession.Event> { get async }
```

#### Discussion

Consume and handle events as the session produces then. Do this with a `for-await-in` loop over the stream, like the following example:

```swift
for await event in session.eventStream {
    // Handle event.
}
```

## See Also

- [CredentialSession.Event](credentialsession/event.md)
  Events produced by a credential session, such as connectivity events and errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/eventstream)*