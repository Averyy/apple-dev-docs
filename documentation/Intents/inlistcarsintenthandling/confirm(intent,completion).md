# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms that you can provide a list of the user’s electric vehicles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
optional func confirm(intent: INListCarsIntent, completion: @escaping @Sendable (INListCarsIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INListCarsIntent) async -> INListCarsIntentResponse
```

```objc
- (void) confirmListCars:(INListCarsIntent *) intent completion:(void (^)(INListCarsIntentResponse *response)) completion;
```

#### Discussion

Implement this method to confirm that you can provide a list of the user’s electric vehicles.

Perform any processing that your app requires to retrieve a list of the user’s electric vehicles, and then create a response object with a status code that indicates your app’s readiness to handle the intent. You must then call the completion block and pass the response.

## Parameters

- `intent`: The intent object that represents the request.
- `completion`: The block you call with your response. You must call this block within your implementation of this method and pass an instance of [`INListCarsIntentResponse`](../inlistcarsintentresponse.md) that contains the appropriate status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintenthandling/confirm(intent:completion:))*