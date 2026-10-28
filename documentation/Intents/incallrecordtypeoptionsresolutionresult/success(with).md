# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func success(with resolvedCallRecordTypeOptions: INCallRecordTypeOptions = []) -> Self
```

```objc
+ (instancetype) successWithResolvedCallRecordTypeOptions:(INCallRecordTypeOptions) resolvedCallRecordTypeOptions;
```

## Return Value

A new [`INCallRecordTypeOptionsResolutionResult`](../incallrecordtypeoptionsresolutionresult.md) object.

## Discussion

Use this method to create a resolution result object that indicates the types of calls that you can return from a search.

## Parameters

- `resolvedCallRecordTypeOptions`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INCallRecordTypeOptions) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtypeoptionsresolutionresult/success(with:))*