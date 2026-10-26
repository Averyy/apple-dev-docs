# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func disambiguation(with objectsToDisambiguate: [INObject]) -> Self
```

```objc
+ (instancetype) disambiguationWithObjectsToDisambiguate:(NSArray<INObject *> *) objectsToDisambiguate;
```

#### Return Value

A new [`INObjectResolutionResult`](../inobjectresolutionresult.md) object.

#### Discussion

Use this method to create a result object when there’s more one value that might match the given parameter. Siri prompts the user to select from among the objects you provide.

## Parameters

- `objectsToDisambiguate`: An array of [`INObject`](../inobject.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INObject) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INObject?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobjectresolutionresult/disambiguation(with:))*