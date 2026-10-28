# INDateComponentsResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the date information associated with an intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INDateComponentsResolutionResult
```

```objc
@interface INDateComponentsResolutionResult : INIntentResolutionResult
```

## Overview

An [`INDateComponentsResolutionResult`](./indatecomponentsresolutionresult.md) object is what you return when resolving parameters containing a [`NSDateComponents`](../Foundation/nsdatecomponents.md) object. Use the creation method that best reflects your ability to successfully resolve the parameter. For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: DateComponents) -> Self](./indatecomponentsresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: DateComponents?) -> Self](./indatecomponentsresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [DateComponents]) -> Self](./indatecomponentsresolutionresult/disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.

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

### Dates and Times
- [class INDateComponentsRangeResolutionResult](./indatecomponentsrangeresolutionresult.md)
  A resolution result for a range of dates in a parameter of an intent.
- [class INTimeIntervalResolutionResult](./intimeintervalresolutionresult.md)
  A resolution result for a time interval associated with an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsresolutionresult)*