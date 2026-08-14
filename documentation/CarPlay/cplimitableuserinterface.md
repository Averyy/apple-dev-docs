# CPLimitableUserInterface

**Framework**: CarPlay  
**Kind**: struct

The types of limitable user interface elements.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct CPLimitableUserInterface
```

## Topics

### User Interface Limits
- [static var keyboard: CPLimitableUserInterface](cplimitableuserinterface/keyboard.md)
  Indicates that the car is limiting the keyboard display.
- [static var lists: CPLimitableUserInterface](cplimitableuserinterface/lists.md)
  Indicates that the car is limiting the display of lists.
### Initializers
- [init(rawValue: UInt)](cplimitableuserinterface/init(rawvalue:).md)
  Initializes a limitable user interface element using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var limitedUserInterfaces: CPLimitableUserInterface](cpsessionconfiguration/limiteduserinterfaces.md)
  A bit mask value that indicates the user interface limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplimitableuserinterface)*