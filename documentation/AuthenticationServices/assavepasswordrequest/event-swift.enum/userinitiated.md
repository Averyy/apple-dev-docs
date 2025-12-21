# ASSavePasswordRequest.Event.userInitiated

**Framework**: Authentication Services  
**Kind**: case

The save event that occurs when a user has expressly stated they wish to save the credential.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
case userInitiated
```

#### Discussion

The expected behavior is to save “new” or “updated” credentials.

Providers may request any additional information from the user necessary to support the save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest/event-swift.enum/userinitiated)*