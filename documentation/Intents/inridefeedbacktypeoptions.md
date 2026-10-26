# INRideFeedbackTypeOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Constants indicating the type of feedback needed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct INRideFeedbackTypeOptions
```

```c
enum INRideFeedbackTypeOptions : NSUInteger;
```

## Topics

### Constants
- [static var rate: INRideFeedbackTypeOptions](./inridefeedbacktypeoptions/rate.md)
  A constant indicating that the user must rate the driver.
- [static var tip: INRideFeedbackTypeOptions](./inridefeedbacktypeoptions/tip.md)
  A constant indicating that the user must specify a tip amount.
### Initializers
- [init(rawValue: UInt)](./inridefeedbacktypeoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Requesting Feedback About the Ride
- [var feedbackType: INRideFeedbackTypeOptions](./inridecompletionstatus/feedbacktype.md)
  The type of feedback required for the ride before the user books a new ride can.
- [var defaultTippingOptions: Set<INCurrencyAmount>?](./inridecompletionstatus/defaulttippingoptions.md)
  An array of default tip amounts to display to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridefeedbacktypeoptions)*