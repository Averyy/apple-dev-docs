# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with stringToConfirm: INSpeakableString?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithStringToConfirm:(INSpeakableString *) stringToConfirm;
```

#### Return Value

A new [`INSpeakableStringResolutionResult`](../inspeakablestringresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to the specified value but you want the user to confirm that value.

## Parameters

- `stringToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INSpeakableString) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [INSpeakableString]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakablestringresolutionresult/confirmationrequired(with:))*