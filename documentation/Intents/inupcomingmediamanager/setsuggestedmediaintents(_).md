# setSuggestedMediaIntents(_:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Provides Siri with a list of media intents to suggest to the user.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func setSuggestedMediaIntents(_ intents: NSOrderedSet)
```

```objc
- (void) setSuggestedMediaIntents:(NSOrderedSet<INPlayMediaIntent *> *) intents;
```

## Discussion

Use this method to have Siri suggest media content to the user that:

- Becomes available in your app, such as a new episode in a TV series.
- The user hasn’t listened to or watched, but may be interested in.
- The user hasn’t finished listening to or watching.

To replace the list, call the method again, passing in a new set of intents. If you want to remove the suggested media intents, call the method passing in an empty array.

## Parameters

- `intents`: An ordered list of media intents that you want Siri to suggest to the user. Begin the list with the most important or useful intents for the user, followed by less important or useful ones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupcomingmediamanager/setsuggestedmediaintents(_:))*