# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms that you can modify the attributes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func confirm(intent: INSetMessageAttributeIntent, completion: @escaping @Sendable (INSetMessageAttributeIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSetMessageAttributeIntent) async -> INSetMessageAttributeIntentResponse
```

```objc
- (void) confirmSetMessageAttribute:(INSetMessageAttributeIntent *) intent completion:(void (^)(INSetMessageAttributeIntentResponse *response)) completion;
```

#### Discussion

This method validates that your messaging service is available and that modifying the specified messages is possible. At some point in your implementation, execute the provided completion block with an appropriate response object.

## Parameters

- `intent`: The intent object that containing details about the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler whle implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSetMessageAttributeIntentResponse`](../insetmessageattributeintentresponse.md) object that contains the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintenthandling/confirm(intent:completion:))*