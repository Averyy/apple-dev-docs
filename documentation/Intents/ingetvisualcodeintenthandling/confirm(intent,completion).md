# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can provide the requested visual code.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func confirm(intent: INGetVisualCodeIntent, completion: @escaping @Sendable (INGetVisualCodeIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INGetVisualCodeIntent) async -> INGetVisualCodeIntentResponse
```

```objc
- (void) confirmGetVisualCode:(INGetVisualCodeIntent *) intent completion:(void (^)(INGetVisualCodeIntentResponse *response)) completion;
```

#### Discussion

Implement this method to verify that you’re able to produce the requested visual code. You might use this method to verify the user’s account credentials and verify that their account can handle the specified type of transaction.

At some point in your implementation, execute the provided handler block with a response object containing the status of whether you can provide the code. For more information about creating the response object, see [`INGetVisualCodeIntentResponse`](../ingetvisualcodeintentresponse.md).

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved the properties of this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INGetVisualCodeIntentResponse`](../ingetvisualcodeintentresponse.md) object containing the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintenthandling/confirm(intent:completion:))*