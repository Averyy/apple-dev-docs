# INPlayMediaIntentResponseCode.failureNoUnplayedContent

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The media container has no unplayed content.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case failureNoUnplayedContent
```

```c
INPlayMediaIntentResponseCodeFailureNoUnplayedContent
```

#### Discussion

Respond with this code when a media container such as a playlist has no unplayed media items.

## See Also

### Failures
- [INPlayMediaIntentResponseCode.failure](./failure.md)
  A failure occurred while confirming or handling the intent.
- [INPlayMediaIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch the app before media playback can begin.
- [INPlayMediaIntentResponseCode.failureRestrictedContent](./failurerestrictedcontent.md)
  The app cannot play the media because of content restrictions.
- [INPlayMediaIntentResponseCode.failureUnknownMediaType](./failureunknownmediatype.md)
  The app cannot play the media because the type is unknown or not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode/failurenounplayedcontent)*