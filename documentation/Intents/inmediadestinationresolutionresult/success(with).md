# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves successfully matching the specified parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func success(with resolvedMediaDestination: INMediaDestination) -> Self
```

```objc
+ (instancetype) successWithResolvedMediaDestination:(INMediaDestination *) resolvedMediaDestination;
```

## Return Value

A new [`INMediaDestinationResolutionResult`](../inmediadestinationresolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to add a media item to the specified destination.

## Parameters

- `resolvedMediaDestination`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INMediaDestination?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.
- [class func disambiguation(with: [INMediaDestination]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationresolutionresult/success(with:))*