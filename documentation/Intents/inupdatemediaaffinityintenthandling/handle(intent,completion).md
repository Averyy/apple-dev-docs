# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles the media update affinity request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func handle(intent: INUpdateMediaAffinityIntent, completion: @escaping @Sendable (INUpdateMediaAffinityIntentResponse) -> Void)
```

```swift
func handle(intent: INUpdateMediaAffinityIntent) async -> INUpdateMediaAffinityIntentResponse
```

```objc
- (void) handleUpdateMediaAffinity:(INUpdateMediaAffinityIntent *) intent completion:(void (^)(INUpdateMediaAffinityIntentResponse *response)) completion;
```

## Discussion

Implement this method to update the affinity for the media item.

## Parameters

- `intent`: The [`INUpdateMediaAffinityIntent`](../inupdatemediaaffinityintent.md) object that contains details about the user’s request. The Intents app extension confirms the information in this intent before the system calls the [`handle(intent:completion:)`](./handle%28intent,completion%29.md) method.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **`response`**: The [`INUpdateMediaAffinityIntentResponse`](../inupdatemediaaffinityintentresponse.md) object you create to report the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintenthandling/handle(intent:completion:))*