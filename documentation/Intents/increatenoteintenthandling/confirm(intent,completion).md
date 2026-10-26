# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can create the note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func confirm(intent: INCreateNoteIntent, completion: @escaping @Sendable (INCreateNoteIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INCreateNoteIntent) async -> INCreateNoteIntentResponse
```

```objc
- (void) confirmCreateNote:(INCreateNoteIntent *) intent completion:(void (^)(INCreateNoteIntentResponse *response)) completion;
```

#### Discussion

Implement this method to validate that you can create the note, but do not create the note yet. If creating the note involves contacting a remote server, validate that your server is available and ready to handle requests. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to create the note.

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INCreateNoteIntentResponse`](../increatenoteintentresponse.md) object containing the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintenthandling/confirm(intent:completion:))*