# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified code and user activity object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(code: INCancelRideIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INCancelRideIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Return Value

An initialized response object or `nil` if the object could not be created.

## Discussion

After initializing the response object, update the [`cancellationFee`](./cancellationfee.md) and [`cancellationFeeThreshold`](./cancellationfeethreshold.md) properties with any relevant cancellation conditions. Siri or Maps notifies the user about any proposed cancellation fees during the confirmation phase.

## Parameters

- `code`: The response code indicating your success or failure in handling the intent. For a list of possible values, see [`INCancelRideIntentResponseCode`](../incancelrideintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information that is specific to your app. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintentresponse/init(code:useractivity:))*