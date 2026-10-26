# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms the details of the media addition request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func confirm(intent: INAddMediaIntent, completion: @escaping @Sendable (INAddMediaIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INAddMediaIntent) async -> INAddMediaIntentResponse
```

```objc
- (void) confirmAddMedia:(INAddMediaIntent *) intent completion:(void (^)(INAddMediaIntentResponse *response)) completion;
```

#### Discussion

Implement this method to determine whether your app can add the requested media. If it can, respond with the [`INAddMediaIntentResponseCode.ready`](../inaddmediaintentresponsecode/ready.md) response code.

If your app can’t add the media, respond with the appropriate failure code.

## Parameters

- `intent`: The [`INAddMediaIntent`](../inaddmediaintent.md) object that contains details about the user’s request.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **`response`**: The [`INAddMediaIntentResponse`](../inaddmediaintentresponse.md) object that contains the response code which determines whether your app can add the media content. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintenthandling/confirm(intent:completion:))*