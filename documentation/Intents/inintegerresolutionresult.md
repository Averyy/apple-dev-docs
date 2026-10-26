# INIntegerResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for an integer value associated with an intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INIntegerResolutionResult
```

```objc
@interface INIntegerResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INIntegerResolutionResult`](./inintegerresolutionresult.md) object is what you return when resolving integer-based parameters of an intent object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: Int) -> Self](./inintegerresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [static func confirmationRequired(with: Int?) -> Self](./inintegerresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ confirmationRequiredWithValueToConfirm:](./inintegerresolutionresult/confirmationrequiredwithvaluetoconfirm_.md)
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

### Numerical Values
- [class INDoubleResolutionResult](./indoubleresolutionresult.md)
  A resolution result for a double value associated with an intent.
- [class INBooleanResolutionResult](./inbooleanresolutionresult.md)
  A resolution result for a Boolean value associated with an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintegerresolutionresult)*