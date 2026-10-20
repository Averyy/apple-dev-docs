# CPLimitableUserInterface

**Framework**: CarPlay  
**Kind**: struct  
**Role**: Structure

The types of limitable user interface elements.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct CPLimitableUserInterface
```

```c
enum CPLimitableUserInterface : NSUInteger;
```

## Topics

### User Interface Limits
- [static var keyboard: CPLimitableUserInterface](./cplimitableuserinterface/keyboard.md)
  Indicates that the car is limiting the keyboard display.
- [static var lists: CPLimitableUserInterface](./cplimitableuserinterface/lists.md)
  Indicates that the car is limiting the display of lists.
### Initializers
- [init(rawValue: UInt)](./cplimitableuserinterface/init%28rawvalue%29.md)
  Initializes a limitable user interface element using the specified raw value.

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

### Getting the Limits
- [var limitedUserInterfaces: CPLimitableUserInterface](./cpsessionconfiguration/limiteduserinterfaces.md)
  A bit mask value that indicates the user interface limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplimitableuserinterface)*