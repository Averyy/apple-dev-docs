# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms the details of the update media affinity request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func confirm(intent: INUpdateMediaAffinityIntent, completion: @escaping @Sendable (INUpdateMediaAffinityIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INUpdateMediaAffinityIntent) async -> INUpdateMediaAffinityIntentResponse
```

```objc
- (void) confirmUpdateMediaAffinity:(INUpdateMediaAffinityIntent *) intent completion:(void (^)(INUpdateMediaAffinityIntentResponse *response)) completion;
```

#### Discussion

Implement this method to determine whether your app can update the affinity for the requested media. If it can, respond with the [`INUpdateMediaAffinityIntentResponseCode.ready`](../inupdatemediaaffinityintentresponsecode/ready.md) response code.

If your app can’t update the affinity for the media item, respond with the appropriate failure code.

## Parameters

- `intent`: The [`INUpdateMediaAffinityIntent`](../inupdatemediaaffinityintent.md) object that contains details about the user’s request.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **`response`**: The [`INUpdateMediaAffinityIntentResponse`](../inupdatemediaaffinityintentresponse.md) object that contains the response code which determines whether your app can update the affinity for a media item. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintenthandling/confirm(intent:completion:))*