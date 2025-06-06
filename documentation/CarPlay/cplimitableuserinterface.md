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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var limitedUserInterfaces: CPLimitableUserInterface](cpsessionconfiguration/limiteduserinterfaces.md)
  A bit mask value that indicates the user interface limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplimitableuserinterface)*