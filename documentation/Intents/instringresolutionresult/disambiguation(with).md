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
class func disambiguation(with stringsToDisambiguate: [String]) -> Self
```

```objc
+ (instancetype) disambiguationWithStringsToDisambiguate:(NSArray<NSString *> *) stringsToDisambiguate;
```

#### Return Value

A new [`INStringResolutionResult`](../instringresolutionresult.md) object.

#### Discussion

Use this method to create a result object when there is more one value that might match the given parameter. The user is asked to select from among the strings you provide.

## Parameters

- `stringsToDisambiguate`: An array of [`NSString`](../../Foundation/nsstring.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: String) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: String?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instringresolutionresult/disambiguation(with:))*