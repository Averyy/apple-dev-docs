# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles searching the photos and returning the number of results.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INSearchForPhotosIntent, completion: @escaping @Sendable (INSearchForPhotosIntentResponse) -> Void)
```

```swift
func handle(intent: INSearchForPhotosIntent) async -> INSearchForPhotosIntentResponse
```

```objc
- (void) handleSearchForPhotos:(INSearchForPhotosIntent *) intent completion:(void (^)(INSearchForPhotosIntentResponse *response)) completion;
```

#### Discussion

Your implementation of this method must perform the search and return the number of matching photos in the response. If you aren’t to perform the search, return a response object whose result code indicates the reason for the failure. Upon returning a successful response, Siri launches your display the photos.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSearchForPhotosIntentResponse`](../insearchforphotosintentresponse.md) object you create to report the status of the request. You also use this object to specify the number of photos that matched the search parameters. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintenthandling/handle(intent:completion:))*