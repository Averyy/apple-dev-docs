# ASSavePasswordRequest.Event.formDidDisappear

**Framework**: Authentication Services  
**Kind**: case

The save event that occurs when a form is submitted or removed from the screen without prompting the user.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
case formDidDisappear
```

#### Discussion

The recommended behavior is to save “new” credentials, and ask the user if they wish to overwrite “updated” credentials.

Providers may request any additional information from the user necessary to support the save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest/event-swift.enum/formdiddisappear)*