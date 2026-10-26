# init(intent:response:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes and returns an interaction object with an intent object and your app’s response.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(intent: INIntent, response: INIntentResponse?)
```

```objc
- (instancetype) initWithIntent:(INIntent *) intent response:(INIntentResponse *) response;
```

#### Return Value

An initialized interaction object or `nil` if the object could not be created.

#### Discussion

Use this method to initialize interaction objects that you intend to donate. You do not need to create interaction objects for any custom [`NSUserActivity`](../../Foundation/nsuseractivity.md) objects that you create during the handling of an intent. SiriKit automatically creates an instance of this class before delivering an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object to your app.

## Parameters

- `intent`: The intent object containing the user’s request.
- `response`: The response object that your app provided in response to the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/init(intent:response:))*