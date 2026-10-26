# INSearchForMediaIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app successfully performed the search.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case success
```

```c
INSearchForMediaIntentResponseCodeSuccess
```

#### Discussion

Use this code when your app has successfully searched for the media.

## See Also

### Response Code
- [INSearchForMediaIntentResponseCode.unspecified](./unspecified.md)
  An unknown state.
- [INSearchForMediaIntentResponseCode.ready](./ready.md)
  The app is ready to perform the search.
- [INSearchForMediaIntentResponseCode.continueInApp](./continueinapp.md)
  The system should launch your app in the foreground to search for the media.
- [INSearchForMediaIntentResponseCode.inProgress](./inprogress.md)
  The app is currently trying to process the search request.
- [INSearchForMediaIntentResponseCode.failure](./failure.md)
  The app is unable to search for the media.
- [INSearchForMediaIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user needs to launch your app to search for the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintentresponsecode/success)*