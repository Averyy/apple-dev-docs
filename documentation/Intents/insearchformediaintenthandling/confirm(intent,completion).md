# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms the details of the media search request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func confirm(intent: INSearchForMediaIntent, completion: @escaping @Sendable (INSearchForMediaIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSearchForMediaIntent) async -> INSearchForMediaIntentResponse
```

```objc
- (void) confirmSearchForMedia:(INSearchForMediaIntent *) intent completion:(void (^)(INSearchForMediaIntentResponse *response)) completion;
```

#### Discussion

Implement this method to determine whether your app can search for the requested media. If it can, respond with the [`INSearchForMediaIntentResponseCode.ready`](../insearchformediaintentresponsecode/ready.md) response code.

If your app can’t search for the media, respond with the appropriate failure code.

## Parameters

- `intent`: The [`INSearchForMediaIntent`](../insearchformediaintent.md) object that contains details about the user’s request.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **`response`**: The [`INSearchForMediaIntentResponse`](../insearchformediaintentresponse.md) object that contains the response code which determines whether your app can search for the media content. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintenthandling/confirm(intent:completion:))*