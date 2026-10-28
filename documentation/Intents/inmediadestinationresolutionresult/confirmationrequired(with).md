# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the value before proceeding.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func confirmationRequired(with mediaDestinationToConfirm: INMediaDestination?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithMediaDestinationToConfirm:(INMediaDestination *) mediaDestinationToConfirm;
```

## Return Value

A new [`INMediaDestinationResolutionResult`](../inmediadestinationresolutionresult.md) object.

## Discussion

Use this method when you can’t resolve the parameter to a destination type that’s similar, but not equal to, the one specified in the intent. Don’t use this method to resolve date types your app doesn’t support.

## Parameters

- `mediaDestinationToConfirm`: The value that resolves the request, but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INMediaDestination) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.
- [class func disambiguation(with: [INMediaDestination]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationresolutionresult/confirmationrequired(with:))*