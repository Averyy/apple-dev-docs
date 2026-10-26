# INCarSignalOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

The signals produced by the user’s car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
struct INCarSignalOptions
```

```c
enum INCarSignalOptions : NSUInteger;
```

#### Overview

In Swift, you can select more than one option from the option set. In Objective-C, you can select more than one option by combining the enums using a bitwise `OR` operation.

## Topics

### Signal Types
- [static var audible: INCarSignalOptions](./incarsignaloptions/audible.md)
  An audible signal; for example, honking the car horn.
- [static var visible: INCarSignalOptions](./incarsignaloptions/visible.md)
  A visual signal; for example, flashing the hazard lights.
### Initializers
- [init(rawValue: UInt)](./incarsignaloptions/init%28rawvalue%29.md)
  Initializes a new car signal option based on the provided raw value.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incarsignaloptions)*