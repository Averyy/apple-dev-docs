# init(username:service:)

**Framework**: Contacts  
**Kind**: init

Returns a [`CNInstantMessageAddress`](cninstantmessageaddress.md) object initialized with the specified user name and service.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(username: String, service: String)
```

#### Return Value

The initialized [`CNInstantMessageAddress`](cninstantmessageaddress.md) object with the specified user name and service.

#### Discussion

User name and service are required to initialize [`CNInstantMessageAddress`](cninstantmessageaddress.md) object.

## Parameters

- `username`: The user name with which to initialize the   object.
- `service`: The service with which to Initialize the   object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cninstantmessageaddress/init(username:service:))*