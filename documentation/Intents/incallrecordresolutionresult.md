# INCallRecordResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the details of a call.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INCallRecordResolutionResult
```

```objc
@interface INCallRecordResolutionResult : INIntentResolutionResult
```

## Overview

You return an `INCallRecordResolutionResult` object when resolving parameters containing an [`INCallRecord`](./incallrecord.md) value. The `resolvedCallRecord` can be different than the original `INCallRecord`. This flexibility allows app extensions to apply business logic constraints.

Use [`notRequired()`](./inintentresolutionresult/notrequired%28%29.md) to continue with a `nil` value. For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Type Methods
- [class func confirmationRequired(with: INCallRecord?) -> Self](./incallrecordresolutionresult/confirmationrequired%28with%29.md)
  Creates a result that requires the user to confirm the value before proceeding.
- [class func disambiguation(with: [INCallRecord]) -> Self](./incallrecordresolutionresult/disambiguation%28with%29.md)
  Creates a result that requires the user to select from an array of choices.
- [class func success(with: INCallRecord) -> Self](./incallrecordresolutionresult/success%28with%29.md)
  Creates a result that contains the call record that matches the users request.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Inherited By
- [INStartCallCallRecordToCallBackResolutionResult](./instartcallcallrecordtocallbackresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resolution Results
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
- [class INStartCallCallRecordToCallBackResolutionResult](./instartcallcallrecordtocallbackresolutionresult.md)
  A resolution result for the redial capabilities of a missed call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordresolutionresult)*