# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides a list of the user’s electric vehicles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func handle(intent: INListCarsIntent, completion: @escaping @Sendable (INListCarsIntentResponse) -> Void)
```

```swift
func handle(intent: INListCarsIntent) async -> INListCarsIntentResponse
```

```objc
- (void) handleListCars:(INListCarsIntent *) intent completion:(void (^)(INListCarsIntentResponse *response)) completion;
```

## Discussion

Retrieve a list of the user’s electric vehicles and create an instance of [`INCar`](../incar.md) for each, setting [`carIdentifier`](../incar/caridentifier.md) to a unique identifier that represents that vehicle. The identifier matches the vehicle to future [`INGetCarPowerLevelStatusIntent`](../ingetcarpowerlevelstatusintent.md) requests. Do not use the vehicle’s VIN, or equivalent, as the identifier.

Before returning from this method, create a response with the appropriate status code and, if you can retrieve a list of the user’s electric vehicles, set the [`cars`](../inlistcarsintentresponse/cars.md) property to the array of `INCar` objects. Then call the completion block and pass the response.

## Parameters

- `intent`: The intent object that represents the request.
- `completion`: The block you call with your response. You must call this block within your implementation of this method and pass an instance of [`INListCarsIntentResponse`](../inlistcarsintentresponse.md) that contains a status code, and a list of the user’s electric vehicles, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintenthandling/handle(intent:completion:))*