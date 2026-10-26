# INStartCallCallRecordToCallBackResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the redial capabilities of a missed call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INStartCallCallRecordToCallBackResolutionResult
```

```objc
@interface INStartCallCallRecordToCallBackResolutionResult : INCallRecordResolutionResult
```

#### Overview

You return an `INStartCallCallRecordToCallBackResolutionResult` object when resolving parameters containing an [`INCallRecord`](./incallrecord.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully. The resolved value can be different from the original [`INCallRecord`](./incallrecord.md). This flexibility allows app extensions to apply business logic constraints.

Use [`notRequired()`](./inintentresolutionresult/notrequired%28%29.md) to continue with a `nil` value. For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Initializers
- [init(callRecordResolutionResult: INCallRecordResolutionResult)](./instartcallcallrecordtocallbackresolutionresult/init%28callrecordresolutionresult%29.md)
  Creates an object whose resolution involves successfully redialing a call.
### Type Methods
- [class func unsupported(forReason: INStartCallCallRecordToCallBackUnsupportedReason) -> Self](./instartcallcallrecordtocallbackresolutionresult/unsupported%28forreason%29.md)
  Creates a result that requires the user to confirm the request, because your app is unable to support the current request.

## Relationships

### Inherits From
- [INCallRecordResolutionResult](./incallrecordresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resolution Results
- [class INCallRecordResolutionResult](./incallrecordresolutionresult.md)
  A resolution result for the details of a call.
- [class INCallRecordTypeResolutionResult](./incallrecordtyperesolutionresult.md)
  A resolution result for the types of calls that your app handled.
- [class INCallDestinationTypeResolutionResult](./incalldestinationtyperesolutionresult.md)
  A resolution result for the destination type of a call.
- [class INCallCapabilityResolutionResult](./incallcapabilityresolutionresult.md)
  A resolution result for the call capability for the call.
- [class INCallRecordTypeOptionsResolutionResult](./incallrecordtypeoptionsresolutionresult.md)
  A resolution result for the call types to include in a search.
- [class INStartCallContactResolutionResult](./instartcallcontactresolutionresult.md)
  A resolution result for the contact for the call.
- [class INStartCallCallCapabilityResolutionResult](./instartcallcallcapabilityresolutionresult.md)
  A resolution result for the call capability for the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcallrecordtocallbackresolutionresult)*