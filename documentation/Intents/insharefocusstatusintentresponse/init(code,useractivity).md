# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a response with the specified response code and user activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(code: INShareFocusStatusIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INShareFocusStatusIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Parameters

- `code`: Your app’s ability to handle the intent.
- `userActivity`: An object the system can send to your app to continue this interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insharefocusstatusintentresponse/init(code:useractivity:))*