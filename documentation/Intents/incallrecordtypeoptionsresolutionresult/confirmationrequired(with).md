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
class func confirmationRequired(with callRecordTypeOptionsToConfirm: INCallRecordTypeOptions = []) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithCallRecordTypeOptionsToConfirm:(INCallRecordTypeOptions) callRecordTypeOptionsToConfirm;
```

#### Return Value

A new [`INCallRecordTypeOptionsResolutionResult`](../incallrecordtypeoptionsresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter but want the user to confirm the value before proceeding. For example, you might ask for confirmation if you do not support searching for some, but not all, of the types requested by the user.

## Parameters

- `callRecordTypeOptionsToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INCallRecordTypeOptions) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtypeoptionsresolutionresult/confirmationrequired(with:))*