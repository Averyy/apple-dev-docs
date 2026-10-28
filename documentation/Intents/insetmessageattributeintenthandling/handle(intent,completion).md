# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles modifying the message attributes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handle(intent: INSetMessageAttributeIntent, completion: @escaping @Sendable (INSetMessageAttributeIntentResponse) -> Void)
```

```swift
func handle(intent: INSetMessageAttributeIntent) async -> INSetMessageAttributeIntentResponse
```

```objc
- (void) handleSetMessageAttribute:(INSetMessageAttributeIntent *) intent completion:(void (^)(INSetMessageAttributeIntentResponse *response)) completion;
```

## Discussion

Your implementation of this method must try to modify the attributes of the messages. The response object you provide should indicate whether you were successful at making the changes.

## Parameters

- `intent`: The intent object that contains details about the user’s request. The information in this object has already been resolved and confirmed by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSetMessageAttributeIntentResponse`](../insetmessageattributeintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintenthandling/handle(intent:completion:))*