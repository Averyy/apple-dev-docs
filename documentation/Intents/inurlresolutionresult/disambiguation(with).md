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
class func disambiguation(with urlsToDisambiguate: [URL]) -> Self
```

```objc
+ (instancetype) disambiguationWithURLsToDisambiguate:(NSArray<NSURL *> *) urlsToDisambiguate;
```

## Return Value

A new [`INURLResolutionResult`](../inurlresolutionresult.md) object.

## Discussion

Use this method to create a result object when more than one URL matches the given information and you can’t pick one definitively. Ask the user to select from among the notes that you specify.

For each [`NSURL`](../../Foundation/nsurl.md) object that you provide, include enough information to be able to locate the URL again later. When the user selects one of the URLs, SiriKit puts the details from your [`NSURL`](../../Foundation/nsurl.md) object into the intent and asks you to resolve the intent again.

## Parameters

- `urlsToDisambiguate`: An array of [`NSURL`](../../Foundation/nsurl.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result
- [class func success(with: URL) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: URL?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inurlresolutionresult/disambiguation(with:))*