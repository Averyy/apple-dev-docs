# init(callRecordResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution involves successfully redialing a call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(callRecordResolutionResult: INCallRecordResolutionResult)
```

```objc
- (instancetype) initWithCallRecordResolutionResult:(INCallRecordResolutionResult *) callRecordResolutionResult;
```

#### Return Value

A new [`INStartCallCallRecordToCallBackResolutionResult`](../instartcallcallrecordtocallbackresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to redial a call.

## Parameters

- `callRecordResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different from the one specified in the intent object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcallrecordtocallbackresolutionresult/init(callrecordresolutionresult:))*