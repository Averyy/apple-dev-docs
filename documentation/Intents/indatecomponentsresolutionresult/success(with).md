# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedDateComponents: DateComponents) -> Self
```

```objc
+ (instancetype) successWithResolvedDateComponents:(NSDateComponents *) resolvedDateComponents;
```

#### Return Value

A new [`INDateComponentsResolutionResult`](../indatecomponentsresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you are able to resolve a parameter successfully to a specific date.

## Parameters

- `resolvedDateComponents`: The object that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: DateComponents?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [DateComponents]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsresolutionresult/success(with:))*