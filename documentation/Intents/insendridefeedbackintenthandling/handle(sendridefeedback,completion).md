# handle(sendRideFeedback:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles the recording of feedback for the specified ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handle(sendRideFeedback sendRideFeedbackintent: INSendRideFeedbackIntent, completion: @escaping @Sendable (INSendRideFeedbackIntentResponse) -> Void)
```

```swift
func handle(sendRideFeedback sendRideFeedbackintent: INSendRideFeedbackIntent) async -> INSendRideFeedbackIntentResponse
```

```objc
- (void) handleSendRideFeedback:(INSendRideFeedbackIntent *) sendRideFeedbackintent completion:(void (^)(INSendRideFeedbackIntentResponse *response)) completion;
```

## Discussion

In your implementation of this method, apply the feedback in the provided intent object to the specified ride.

## Parameters

- `sendRideFeedbackintent`: The intent object containing details about the user’s request. The information in this object has already been confirmed by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSendRideFeedbackIntentResponse`](../insendridefeedbackintentresponse.md) object containing the status of applying the feedback. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintenthandling/handle(sendridefeedback:completion:))*