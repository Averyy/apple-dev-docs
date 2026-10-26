# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user confirm the value before proceeding.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class func confirmationRequired(with visualCodeTypeToConfirm: INVisualCodeType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithVisualCodeTypeToConfirm:(INVisualCodeType) visualCodeTypeToConfirm;
```

#### Return Value

A new [`INVisualCodeTypeResolutionResult`](../invisualcodetyperesolutionresult.md) object.

#### Discussion

Use this method when you can’t provide the requested type of code but can provide a code of some type.

## Parameters

- `visualCodeTypeToConfirm`: The value that resolves the request, for the user to confirm.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INVisualCodeType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invisualcodetyperesolutionresult/confirmationrequired(with:))*