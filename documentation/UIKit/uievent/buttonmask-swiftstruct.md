# UIEvent.ButtonMask

**Framework**: UIKit  
**Kind**: struct

Constants that indicate which input-device buttons are pressed.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
struct ButtonMask
```

## Topics

### Creating button masks
- [init(rawValue: Int)](uievent/buttonmask-swift.struct/init(rawvalue:).md)
  Creates a button mask with the specified raw value.
- [static func button(Int) -> UIEvent.ButtonMask](uievent/buttonmask-swift.struct/button(_:).md)
  Creates a button mask from the specified button index.
### Accessing button masks
- [static var primary: UIEvent.ButtonMask](uievent/buttonmask-swift.struct/primary.md)
  A constant that represents the primary button on the input device.
- [static var secondary: UIEvent.ButtonMask](uievent/buttonmask-swift.struct/secondary.md)
  A constant that represents the secondary button on the input device.

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

- [var buttonMask: UIEvent.ButtonMask](uievent/buttonmask-swift.property.md)
  A bit mask that represents which input-device buttons are pressed for the current event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/buttonmask-swift.struct)*