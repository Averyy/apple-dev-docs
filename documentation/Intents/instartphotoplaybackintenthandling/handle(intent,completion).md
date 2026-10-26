# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles performing the search and returning the number of results.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: INStartPhotoPlaybackIntentHandling is deprecated. There is no replacement.

## Declaration

```swift
func handle(intent: INStartPhotoPlaybackIntent, completion: @escaping @Sendable (INStartPhotoPlaybackIntentResponse) -> Void)
```

```swift
func handle(intent: INStartPhotoPlaybackIntent) async -> INStartPhotoPlaybackIntentResponse
```

```objc
- (void) handleStartPhotoPlayback:(INStartPhotoPlaybackIntent *) intent completion:(void (^)(INStartPhotoPlaybackIntentResponse *response)) completion;
```

#### Discussion

Your implementation of this method must perform the search and return the number of matching photos in the response. If you’re unable to perform the search, return a response object whose result code indicates the reason for the failure. Upon returning a successful response, Siri launches your app to start the slideshow.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved and confirmed the information in this intent.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INStartPhotoPlaybackIntentResponse`](../instartphotoplaybackintentresponse.md) object you create to report the status of the request. You also use this object to specify the number of photos that matched the search parameters. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintenthandling/handle(intent:completion:))*