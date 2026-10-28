# INPlacemarkResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for placemark information associated with an intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPlacemarkResolutionResult
```

```objc
@interface INPlacemarkResolutionResult : INIntentResolutionResult
```

## Mentions

- [Resolving the Parameters of an Intent](../SiriKit/resolving-the-parameters-of-an-intent.md)

## Overview

An [`INPlacemarkResolutionResult`](./inplacemarkresolutionresult.md) object is what you return when resolving parameters containing an [`CLPlacemark`](../CoreLocation/clplacemark.md) object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: CLPlacemark) -> Self](./inplacemarkresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: CLPlacemark?) -> Self](./inplacemarkresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [CLPlacemark]) -> Self](./inplacemarkresolutionresult/disambiguation%28with%29.md)
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

### Contacts
- [class INPersonResolutionResult](./inpersonresolutionresult.md)
  A resolution result for a user as a parameter of an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplacemarkresolutionresult)*