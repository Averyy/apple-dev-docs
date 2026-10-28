# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func disambiguation(with peopleToDisambiguate: [INPerson]) -> Self
```

```objc
+ (instancetype) disambiguationWithPeopleToDisambiguate:(NSArray<INPerson *> *) peopleToDisambiguate;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Return Value

A new [`INPersonResolutionResult`](../inpersonresolutionresult.md) object.

## Discussion

Use this method to create a result object when more than one person might match the given information and you can’t pick one definitively. Ask the user to select from among the people you specify.

## Parameters

- `peopleToDisambiguate`: An array of [`INPerson`](../inperson.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INPerson) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INPerson?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonresolutionresult/disambiguation(with:))*