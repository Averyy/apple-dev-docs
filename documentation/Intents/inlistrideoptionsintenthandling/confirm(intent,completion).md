# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms that you can provide the list of ride options.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func confirm(intent: INListRideOptionsIntent, completion: @escaping @Sendable (INListRideOptionsIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INListRideOptionsIntent) async -> INListRideOptionsIntentResponse
```

```objc
- (void) confirmListRideOptions:(INListRideOptionsIntent *) intent completion:(void (^)(INListRideOptionsIntentResponse *response)) completion;
```

#### Discussion

Implement this method to verify that you are able to provide a list of ride options. You might use this method to verify that your service is available and that the user has a valid account. Create a response object with an appropriate code indicating your app’s readiness and execute the provided `completion` block.

When configuring your response object, try to include the available ride options that you would when handling the intent. Providing a complete response object is good way to ensure that you are able to provide the needed information.

Maps does not call this method. The Maps interface lets the user specify the pickup and drop-off locations explicitly, making confirmation of those values unnecessary.

## Parameters

- `intent`: The intent object containing details of the request. Use the information in this object to identify available ride options for the user.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INListRideOptionsIntentResponse`](../inlistrideoptionsintentresponse.md) object containing the status of whether your app is able to return a list of ride options. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintenthandling/confirm(intent:completion:))*