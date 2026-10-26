# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a response for a play media intent.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(code: INPlayMediaIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INPlayMediaIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Parameters

- `code`: A response code that indicates whether the app can play the media.
- `userActivity`: A user activity that contains private state data that your Intents app extension shares with your main app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponse/init(code:useractivity:))*