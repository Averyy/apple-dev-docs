# checkAuthorizationStatus(for:)

**Framework**: Messages  
**Kind**: method

Confirms the current authorization status for sending critical messages from this app.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
func checkAuthorizationStatus(for recipients: [MSRecipient]) async throws -> [MSRecipient : MSCriticalMessagingAuthorizationStatus]
```

## Mentions

- [Sending SMS messages from an app](critical-messaging-api.md)

#### Return Value

A dictionary that maps recipients to their corresponding authorization status.

#### Discussion

You can call this method multiple times to check the authorization status for multiple recipients. Upon an error, the method throws an error of `MSCriticalMessagingErrorDomain``.

## Parameters

- `recipients`: An array of recipients to check the authorization status for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mscriticalsmsmessenger/checkauthorizationstatus(for:))*