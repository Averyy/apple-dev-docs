# INCarAirCirculationModeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the air circulation mode to use in a car.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INCarAirCirculationModeResolutionResult
```

```objc
@interface INCarAirCirculationModeResolutionResult : INIntentResolutionResult
```

## Overview

An [`INCarAirCirculationModeResolutionResult`](./incaraircirculationmoderesolutionresult.md) object is what you return when resolving parameters containing a [`INCarAirCirculationMode`](./incaraircirculationmode.md) value. Use the creation method that best reflects your ability to successfully resolve the parameter. For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INCarAirCirculationMode) -> Self](./incaraircirculationmoderesolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INCarAirCirculationMode) -> Self](./incaraircirculationmoderesolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ successWithResolvedValue:](./incaraircirculationmoderesolutionresult/successwithresolvedvalue_.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [+ confirmationRequiredWithValueToConfirm:](./incaraircirculationmoderesolutionresult/confirmationrequiredwithvaluetoconfirm_.md)
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

### CarPlay Resolution Results
- [class INCarSeatResolutionResult](./incarseatresolutionresult.md)
  A resolution result for a specific seat of the car.
- [class INCarDefrosterResolutionResult](./incardefrosterresolutionresult.md)
  A resolution result for which defroster to use in a car.
- [class INCarAudioSourceResolutionResult](./incaraudiosourceresolutionresult.md)
  A resolution result for the audio source to use in a car.
- [class INRadioTypeResolutionResult](./inradiotyperesolutionresult.md)
  A resolution result for the type of radio to use in a car.
- [class INRelativeReferenceResolutionResult](./inrelativereferenceresolutionresult.md)
  A resolution result for a choice between the next or previous option.
- [class INRelativeSettingResolutionResult](./inrelativesettingresolutionresult.md)
  A resolution result for whether you can select the minimum, current, or maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incaraircirculationmoderesolutionresult)*