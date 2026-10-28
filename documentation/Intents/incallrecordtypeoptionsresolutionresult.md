# INCallRecordTypeOptionsResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the call types to include in a search.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INCallRecordTypeOptionsResolutionResult
```

```objc
@interface INCallRecordTypeOptionsResolutionResult : INIntentResolutionResult
```

## Overview

An `INCallRecordTypeOptionsResolutionResult` object is what you return when resolving parameters containing a value of type [`INCallRecordTypeOptions`](./incallrecordtypeoptions.md). Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INCallRecordTypeOptions) -> Self](./incallrecordtypeoptionsresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INCallRecordTypeOptions) -> Self](./incallrecordtypeoptionsresolutionresult/confirmationrequired%28with%29.md)
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
- [class INCallRecordTypeResolutionResult](./incallrecordtyperesolutionresult.md)
  A resolution result for the types of calls that your app handled.
- [class INCallDestinationTypeResolutionResult](./incalldestinationtyperesolutionresult.md)
  A resolution result for the destination type of a call.
- [class INCallCapabilityResolutionResult](./incallcapabilityresolutionresult.md)
  A resolution result for the call capability for the call.
- [class INStartCallContactResolutionResult](./instartcallcontactresolutionresult.md)
  A resolution result for the contact for the call.
- [class INStartCallCallCapabilityResolutionResult](./instartcallcallcapabilityresolutionresult.md)
  A resolution result for the call capability for the call.
- [class INStartCallCallRecordToCallBackResolutionResult](./instartcallcallrecordtocallbackresolutionresult.md)
  A resolution result for the redial capabilities of a missed call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtypeoptionsresolutionresult)*