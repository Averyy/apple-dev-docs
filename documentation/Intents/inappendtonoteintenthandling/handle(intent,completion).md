# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles appending content to a note.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INAppendToNoteIntent, completion: @escaping @Sendable (INAppendToNoteIntentResponse) -> Void)
```

```swift
func handle(intent: INAppendToNoteIntent) async -> INAppendToNoteIntentResponse
```

```objc
- (void) handleAppendToNote:(INAppendToNoteIntent *) intent completion:(void (^)(INAppendToNoteIntentResponse *response)) completion;
```

## Discussion

In your implementation of this method, update the note’s content in your app, create a response object with the updated note information, and call the provided completion handler.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INAppendToNoteIntentResponse`](../inappendtonoteintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintenthandling/handle(intent:completion:))*