# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles providing the image for the specified visual code.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INGetVisualCodeIntent, completion: @escaping @Sendable (INGetVisualCodeIntentResponse) -> Void)
```

```swift
func handle(intent: INGetVisualCodeIntent) async -> INGetVisualCodeIntentResponse
```

```objc
- (void) handleGetVisualCode:(INGetVisualCodeIntent *) intent completion:(void (^)(INGetVisualCodeIntentResponse *response)) completion;
```

#### Discussion

Your implementation of this method should create an image for the requested visual code. Place that image in your response object and call the provided handler block.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved and confirmed the information in this intent.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INGetVisualCodeIntentResponse`](../ingetvisualcodeintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintenthandling/handle(intent:completion:))*