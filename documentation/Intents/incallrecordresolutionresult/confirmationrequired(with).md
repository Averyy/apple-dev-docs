# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a result that requires the user to confirm the value before proceeding.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func confirmationRequired(with callRecordToConfirm: INCallRecord?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithCallRecordToConfirm:(INCallRecord *) callRecordToConfirm;
```

## Return Value

A new [`INCallRecordResolutionResult`](../incallrecordresolutionresult.md) object.

## Discussion

Use this method when you can’t resolve the parameter to a call record, and it has to get confirmed by the user to proceed.

## Parameters

- `callRecordToConfirm`: The value that resolves the request. It must get confirmed by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordresolutionresult/confirmationrequired(with:))*