# ASSavePasswordRequest.Event.generatedPasswordFilled

**Framework**: Authentication Services  
**Kind**: case

A save event that occurs when generated password is filled into a not yet submitted form.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
case generatedPasswordFilled
```

#### Discussion

The recommended behavior is to save “new” credentials as pending accounts. This event will generally be followed by a userInitiated or formDidDisappear event.

Providers should not request any additional information from the user as that will not be transmitted back to the form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest/event-swift.enum/generatedpasswordfilled)*