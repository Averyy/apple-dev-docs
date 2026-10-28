# INRestaurantGuestResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the identity of a user involved in booking a reservation at a restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INRestaurantGuestResolutionResult
```

```objc
@interface INRestaurantGuestResolutionResult : INIntentResolutionResult
```

## Overview

An [`INRestaurantGuestResolutionResult`](./inrestaurantguestresolutionresult.md) object is what you return when resolving parameters containing a [`INRestaurantGuest`](./inrestaurantguest.md) object. Use the creation method that best reflects your ability to successfully resolve the parameter. For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INRestaurantGuest) -> Self](./inrestaurantguestresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INRestaurantGuest?) -> Self](./inrestaurantguestresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [INRestaurantGuest]) -> Self](./inrestaurantguestresolutionresult/disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resolution Results
- [class INRestaurantResolutionResult](./inrestaurantresolutionresult.md)
  A resolution result for the restaurant selected by a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestresolutionresult)*