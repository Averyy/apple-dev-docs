# INStartCallContactResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the contact for the call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INStartCallContactResolutionResult
```

```objc
@interface INStartCallContactResolutionResult : INPersonResolutionResult
```

## Overview

You return an `INStartCallContactResolutionResult` object when resolving parameters containing an [`INPerson`](./inperson.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully. The resolved value can be different than the original [`INPerson`](./inperson.md). This flexibility allows app extensions to apply business logic constraints.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [init(personResolutionResult: INPersonResolutionResult)](./instartcallcontactresolutionresult/init%28personresolutionresult%29.md)
  Creates an object whose resolution involves the succesful start of a call with the specified contact.
- [class func unsupported(forReason: INStartCallContactUnsupportedReason) -> Self](./instartcallcontactresolutionresult/unsupported%28forreason%29.md)
  Creates an object specifying that resolution of the parameter wasn’t supported, for the specified reason.
- [enum INStartCallContactUnsupportedReason](./instartcallcontactunsupportedreason.md)
  Constants indicating the reason the app can’t support starting a call with the contact.

## Relationships

### Inherits From
- [INPersonResolutionResult](./inpersonresolutionresult.md)
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
- [class INStartCallCallCapabilityResolutionResult](./instartcallcallcapabilityresolutionresult.md)
  A resolution result for the call capability for the call.
- [class INStartCallCallRecordToCallBackResolutionResult](./instartcallcallrecordtocallbackresolutionresult.md)
  A resolution result for the redial capabilities of a missed call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcontactresolutionresult)*