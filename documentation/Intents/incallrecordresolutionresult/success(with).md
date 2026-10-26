# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a result that contains the call record that matches the users request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func success(with resolvedCallRecord: INCallRecord) -> Self
```

```objc
+ (instancetype) successWithResolvedCallRecord:(INCallRecord *) resolvedCallRecord;
```

#### Return Value

A new [`INCallRecordResolutionResult`](../incallrecordresolutionresult.md) object.

#### Discussion

Use this method for when the app extension wants to tell Siri to proceed, with a given `INCallRecord`.

## Parameters

- `resolvedCallRecord`: The value that resolves the users request. This value may be different than the original [`INCallRecord`](../incallrecord.md). This allows app extensions to apply business logic constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordresolutionresult/success(with:))*