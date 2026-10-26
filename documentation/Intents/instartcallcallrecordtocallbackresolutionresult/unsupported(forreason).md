# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a result that requires the user to confirm the request, because your app is unable to support the current request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func unsupported(forReason reason: INStartCallCallRecordToCallBackUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INStartCallCallRecordToCallBackUnsupportedReason) reason;
```

#### Return Value

A new [`INStartCallCallRecordToCallBackResolutionResult`](../instartcallcallrecordtocallbackresolutionresult.md) object.

#### Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The reason that the callback request isn’t supported. For a list of possible values, see [`INStartCallCallRecordToCallBackUnsupportedReason`](../instartcallcallrecordtocallbackunsupportedreason.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcallrecordtocallbackresolutionresult/unsupported(forreason:))*