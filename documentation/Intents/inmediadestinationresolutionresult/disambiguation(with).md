# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func disambiguation(with mediaDestinationsToDisambiguate: [INMediaDestination]) -> Self
```

```objc
+ (instancetype) disambiguationWithMediaDestinationsToDisambiguate:(NSArray<INMediaDestination *> *) mediaDestinationsToDisambiguate;
```

## Return Value

A new [`INMediaDestinationResolutionResult`](../inmediadestinationresolutionresult.md) object.

## Discussion

Use this method to create a result object when more than one media destination matches the given information and you can’t definitevely pick one. Ask the user to select from among the notes that you specify.

For each [`INMediaDestinationReference`](../inmediadestinationreference.md) object you provide, include enough information to be able to locate the destination  later. When the user selects one of the destinations, SiriKit puts the details from your [`INMediaDestinationReference`](../inmediadestinationreference.md) object into the intent and asks you to resolve the adding of media again.

## Parameters

- `mediaDestinationsToDisambiguate`: An array of [`INMediaDestinationReference`](../inmediadestinationreference.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INMediaDestination) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.
- [class func confirmationRequired(with: INMediaDestination?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationresolutionresult/disambiguation(with:))*