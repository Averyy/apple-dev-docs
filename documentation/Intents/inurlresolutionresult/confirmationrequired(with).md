# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func confirmationRequired(with urlToConfirm: URL?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithURLToConfirm:(NSURL *) urlToConfirm;
```

## Return Value

A new [`INURLResolutionResult`](../inurlresolutionresult.md) object.

## Discussion

Use this method when you can’t resolve the parameter to a destination type that’s similar to, but not equal to, the one specified in the intent. Don’t use this method to resolve date types that your app doesn’t support.

## Parameters

- `urlToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result
- [class func success(with: URL) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [URL]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inurlresolutionresult/confirmationrequired(with:))*