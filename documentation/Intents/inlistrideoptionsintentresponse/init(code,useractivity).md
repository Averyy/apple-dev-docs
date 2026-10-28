# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initialize the response object with the specified code and user activity object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(code: INListRideOptionsIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INListRideOptionsIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Return Value

An initialized response object or `nil` if the object could not be created.

## Discussion

After initializing the response object, create one or more [`INRideOption`](../inrideoption.md) objects and assign them to the [`rideOptions`](./rideoptions.md) property. You can also update the other properties of this object to indicate the forms of payment that you accept and the time when the list of options expires.

If your service does not support the user’s area, specify [`INListRideOptionsIntentResponseCode.failureRequiringAppLaunchNoServiceInArea`](../inlistrideoptionsintentresponsecode/failurerequiringapplaunchnoserviceinarea.md) for the `code` parameter and leave the other properties of this object set to `nil`.

## Parameters

- `code`: The response code indicating your success or failure in handling the intent. For a list of possible values, see [`init(code:userActivity:)`](./init%28code,useractivity%29.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information that is specific to your app. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponse/init(code:useractivity:))*