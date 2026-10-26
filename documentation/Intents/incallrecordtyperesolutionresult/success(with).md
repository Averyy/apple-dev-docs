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
class func success(with resolvedCallRecordType: INCallRecordType) -> Self
```

```objc
+ (instancetype) successWithResolvedCallRecordType:(INCallRecordType) resolvedCallRecordType;
```

#### Return Value

A new [`INCallRecordTypeResolutionResult`](../incallrecordtyperesolutionresult.md) object.

#### Discussion

Use this method to create a resolution result object when you recognize the specified type of call and are able to use it to resolve an intent.

## Parameters

- `resolvedCallRecordType`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INCallRecordType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtyperesolutionresult/success(with:))*