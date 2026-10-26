# INPlayMediaIntentResponseCode.failureRestrictedContent

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app cannot play the media because of content restrictions.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case failureRestrictedContent
```

```c
INPlayMediaIntentResponseCodeFailureRestrictedContent
```

#### Discussion

Respond with this code when you cannot handle the request because of a geographic region restriction or similar constraint.

## See Also

### Failures
- [INPlayMediaIntentResponseCode.failure](./failure.md)
  A failure occurred while confirming or handling the intent.
- [INPlayMediaIntentResponseCode.failureNoUnplayedContent](./failurenounplayedcontent.md)
  The media container has no unplayed content.
- [INPlayMediaIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch the app before media playback can begin.
- [INPlayMediaIntentResponseCode.failureUnknownMediaType](./failureunknownmediatype.md)
  The app cannot play the media because the type is unknown or not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode/failurerestrictedcontent)*