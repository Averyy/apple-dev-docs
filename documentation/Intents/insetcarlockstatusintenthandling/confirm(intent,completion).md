# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms that your app can lock or unlock the car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func confirm(intent: INSetCarLockStatusIntent, completion: @escaping @Sendable (INSetCarLockStatusIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSetCarLockStatusIntent) async -> INSetCarLockStatusIntentResponse
```

```objc
- (void) confirmSetCarLockStatus:(INSetCarLockStatusIntent *) intent completion:(void (^)(INSetCarLockStatusIntentResponse *response)) completion;
```

## Discussion

Implement this method to validate that your app can lock or unlock the car given the data in the provided intent. For example, you should validate that the app can currently access the car. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to lock or unlock the car.

## Parameters

- `intent`: An intent object that contains the full details of the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: An [`INSetCarLockStatusIntentResponse`](../insetcarlockstatusintentresponse.md) object that indicates whether your app is able to lock or unlock the car. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintenthandling/confirm(intent:completion:))*