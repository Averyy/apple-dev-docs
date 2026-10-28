# INPlayMediaIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch the app before media playback can begin.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INPlayMediaIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Respond with this code when you cannot handle the request through Siri for a reason not covered by any other response code. For example, use this code when the user hasn’t set up an account with your app. Don’t use this code for general errors or to force the user to launch your app.

## See Also

### Failures
- [INPlayMediaIntentResponseCode.failure](./failure.md)
  A failure occurred while confirming or handling the intent.
- [INPlayMediaIntentResponseCode.failureNoUnplayedContent](./failurenounplayedcontent.md)
  The media container has no unplayed content.
- [INPlayMediaIntentResponseCode.failureRestrictedContent](./failurerestrictedcontent.md)
  The app cannot play the media because of content restrictions.
- [INPlayMediaIntentResponseCode.failureUnknownMediaType](./failureunknownmediatype.md)
  The app cannot play the media because the type is unknown or not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode/failurerequiringapplaunch)*