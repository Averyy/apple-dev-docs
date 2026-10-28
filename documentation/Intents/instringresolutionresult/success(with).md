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
class func success(with resolvedString: String) -> Self
```

```objc
+ (instancetype) successWithResolvedString:(NSString *) resolvedString;
```

## Return Value

A new [`INStringResolutionResult`](../instringresolutionresult.md) object.

## Discussion

Use this method to create a result object when you are able to use the string to handle the intent successfully.

## Parameters

- `resolvedString`: The string that resolves the requested parameter of the intent. This string may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: String?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [String]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instringresolutionresult/success(with:))*