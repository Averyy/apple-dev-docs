# signalEnumerator(for:)

**Framework**: ContactProvider  
**Kind**: method

Requests that the extension enumerate its contacts for the domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func signalEnumerator(for collection: ContactItem.Identifier = .rootContainer) async throws
```

#### Discussion

You typically call this when you need to invoke the app extension on demand. One example is when the app receives a push notification informing it that updated contact data is available.

## Parameters

- `collection`: The collection to enumerate; defaults to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/signalenumerator(for:))*