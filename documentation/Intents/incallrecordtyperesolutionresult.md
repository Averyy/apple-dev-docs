# INCallRecordTypeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the types of calls that your app handled.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INCallRecordTypeResolutionResult
```

```objc
@interface INCallRecordTypeResolutionResult : INIntentResolutionResult
```

## Overview

An `INCallRecordTypeResolutionResult` object is what you return when resolving parameters containing a value of type [`INCallRecordType`](./incallrecordtype.md). Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INCallRecordType) -> Self](./incallrecordtyperesolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INCallRecordType) -> Self](./incallrecordtyperesolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtyperesolutionresult)*