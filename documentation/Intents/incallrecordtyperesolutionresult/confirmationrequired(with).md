# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func confirmationRequired(with callRecordTypeToConfirm: INCallRecordType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithCallRecordTypeToConfirm:(INCallRecordType) callRecordTypeToConfirm;
```

#### Return Value

A new [`INCallRecordTypeResolutionResult`](../incallrecordtyperesolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter but want the user to confirm the value before proceeding. For example, you might ask for confirmation if the user asks to search for missed calls but your app does not track missed calls.

## Parameters

- `callRecordTypeToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INCallRecordType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtyperesolutionresult/confirmationrequired(with:))*