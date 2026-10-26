# INCarSignalOptionsResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the signals the intent is managing on the car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INCarSignalOptionsResolutionResult
```

```objc
@interface INCarSignalOptionsResolutionResult : INIntentResolutionResult
```

#### Overview

Return an `INCarSignalOptionsResolutionResult` object when resolving the [`signals`](./inactivatecarsignalintent/signals.md) property of a [`INActivateCarSignalIntent`](./inactivatecarsignalintent.md) object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INCarSignalOptions) -> Self](./incarsignaloptionsresolutionresult/success%28with%29.md)
  Creates a resolution object that indicates the successful resolution of the provided value.
- [class func confirmationRequired(with: INCarSignalOptions) -> Self](./incarsignaloptionsresolutionresult/confirmationrequired%28with%29.md)
  Creates a resolution object that requires confirmation of the provided value.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incarsignaloptionsresolutionresult)*