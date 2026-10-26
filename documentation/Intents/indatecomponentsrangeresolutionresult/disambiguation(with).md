# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func disambiguation(with dateComponentsRangesToDisambiguate: [INDateComponentsRange]) -> Self
```

```objc
+ (instancetype) disambiguationWithDateComponentsRangesToDisambiguate:(NSArray<INDateComponentsRange *> *) dateComponentsRangesToDisambiguate;
```

#### Return Value

A new [`INDateComponentsRangeResolutionResult`](../indatecomponentsrangeresolutionresult.md) object.

#### Discussion

Use this method when you cannot resolve the object uniquely and need the user to select from a limited set of possible values.

## Parameters

- `dateComponentsRangesToDisambiguate`: An array of date ranges from which the user should select. Specify as few items as possible, and preferably no more than five.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INDateComponentsRange) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INDateComponentsRange?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrangeresolutionresult/disambiguation(with:))*