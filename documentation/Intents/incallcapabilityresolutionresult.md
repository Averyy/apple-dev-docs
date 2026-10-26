# INCallCapabilityResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the call capability for the call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INCallCapabilityResolutionResult
```

```objc
@interface INCallCapabilityResolutionResult : INIntentResolutionResult
```

#### Overview

You return an `INCallCapabilityResolutionResult` object when resolving parameters containing an [`INCallCapability`](./incallcapability.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully. The resolved value can be different than the original [`INCallCapability`](./incallcapability.md). This flexibility allows app extensions to apply business logic constraints.

Use [`notRequired()`](./inintentresolutionresult/notrequired%28%29.md) to continue with a `nil` value. For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INCallCapability) -> Self](./incallcapabilityresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified call capability.
- [class func confirmationRequired(with: INCallCapability) -> Self](./incallcapabilityresolutionresult/confirmationrequired%28with%29.md)
  Creates a result that asks Siri to verify the request that the user wants to continue.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Inherited By
- [INStartCallCallCapabilityResolutionResult](./instartcallcallcapabilityresolutionresult.md)
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
- [class INCallRecordTypeOptionsResolutionResult](./incallrecordtypeoptionsresolutionresult.md)
  A resolution result for the call types to include in a search.
- [class INStartCallContactResolutionResult](./instartcallcontactresolutionresult.md)
  A resolution result for the contact for the call.
- [class INStartCallCallCapabilityResolutionResult](./instartcallcallcapabilityresolutionresult.md)
  A resolution result for the call capability for the call.
- [class INStartCallCallRecordToCallBackResolutionResult](./instartcallcallrecordtocallbackresolutionresult.md)
  A resolution result for the redial capabilities of a missed call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallcapabilityresolutionresult)*