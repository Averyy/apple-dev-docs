# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Activates the car’s signals.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func handle(intent: INActivateCarSignalIntent, completion: @escaping @Sendable (INActivateCarSignalIntentResponse) -> Void)
```

```swift
func handle(intent: INActivateCarSignalIntent) async -> INActivateCarSignalIntentResponse
```

```objc
- (void) handleActivateCarSignal:(INActivateCarSignalIntent *) intent completion:(void (^)(INActivateCarSignalIntentResponse *response)) completion;
```

## Discussion

Your implementation of this method must activate the specified signals on the user’s car. If you are unable to activate the signals, return a response object whose result code indicates the reason for the failure.

## Parameters

- `intent`: An intent object that contains the full details of the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: An [`INActivateCarSignalIntentResponse`](../inactivatecarsignalintentresponse.md) object you create, containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintenthandling/handle(intent:completion:))*