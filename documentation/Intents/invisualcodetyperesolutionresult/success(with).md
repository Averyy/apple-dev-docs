# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified value.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class func success(with resolvedVisualCodeType: INVisualCodeType) -> Self
```

```objc
+ (instancetype) successWithResolvedVisualCodeType:(INVisualCodeType) resolvedVisualCodeType;
```

#### Return Value

A new [`INVisualCodeTypeResolutionResult`](../invisualcodetyperesolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to provide a visual code of the specified type.

## Parameters

- `resolvedVisualCodeType`: The value that resolves the requested value of the intent.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INVisualCodeType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invisualcodetyperesolutionresult/success(with:))*