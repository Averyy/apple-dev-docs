# INTimeIntervalResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for a time interval associated with an intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INTimeIntervalResolutionResult
```

```objc
@interface INTimeIntervalResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INTimeIntervalResolutionResult`](./intimeintervalresolutionresult.md) object is what you return when resolving time interval related parameters of an intent object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result
- [class func success(with: TimeInterval) -> Self](./intimeintervalresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: TimeInterval) -> Self](./intimeintervalresolutionresult/confirmationrequired%28with%29.md)
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

### Dates and Times
- [class INDateComponentsRangeResolutionResult](./indatecomponentsrangeresolutionresult.md)
  A resolution result for a range of dates in a parameter of an intent.
- [class INDateComponentsResolutionResult](./indatecomponentsresolutionresult.md)
  A resolution result for the date information associated with an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intimeintervalresolutionresult)*