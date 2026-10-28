# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Validates whether your app is able to initiate the video call.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
optional func confirm(intent: INStartVideoCallIntent, completion: @escaping @Sendable (INStartVideoCallIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INStartVideoCallIntent) async -> INStartVideoCallIntentResponse
```

```objc
- (void) confirmStartVideoCall:(INStartVideoCallIntent *) intent completion:(void (^)(INStartVideoCallIntentResponse *response)) completion;
```

## Discussion

Use this method to validate that your app is able to initiate the call to the specified users. You might check the availability of your calling network, verify that the current user is logged in and able to place the call, verify that the intended recipients are able to receive the call, or perform other tasks specific to your app.

## Parameters

- `intent`: The intent object containing details about the user’s request. The user has already resolved the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INStartVideoCallIntentResponse`](../instartvideocallintentresponse.md) object containing the status of whether your app is able to make the call. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintenthandling/confirm(intent:completion:))*