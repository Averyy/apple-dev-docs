# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with stringToConfirm: String?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithStringToConfirm:(NSString *) stringToConfirm;
```

#### Return Value

A new [`INStringResolutionResult`](../instringresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to the specified string but you want the user to confirm that value.

## Parameters

- `stringToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: String) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [String]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instringresolutionresult/confirmationrequired(with:))*