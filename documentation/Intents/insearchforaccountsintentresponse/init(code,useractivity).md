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
- watchOS 4.0+

## Declaration

```swift
init(code: INSearchForAccountsIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INSearchForAccountsIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Return Value

An initialized response object or `nil` if the object could not be created.

## Discussion

After initializing the response object, put the account details in the [`accounts`](./accounts.md) property. Always provide as much account information as is relevant.

## Parameters

- `code`: The response code indicating your success or failure in handling the intent. For a list of possible values, see [`INSearchForAccountsIntentResponseCode`](../insearchforaccountsintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add app-specific information. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponse/init(code:useractivity:))*