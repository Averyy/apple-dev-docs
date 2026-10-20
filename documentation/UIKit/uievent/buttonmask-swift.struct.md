# UIEvent.ButtonMask

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum UIEventButtonMask : NSInteger;
```

## Topics

### Creating button masks
- [init(rawValue: Int)](./buttonmask-swift.struct/init%28rawvalue%29.md)
  Creates a button mask with the specified raw value.
- [static func button(Int) -> UIEvent.ButtonMask](./buttonmask-swift.struct/button%28_%29.md)
  Creates a button mask from the specified button index.
### Accessing button masks
- [static var primary: UIEvent.ButtonMask](./buttonmask-swift.struct/primary.md)
  A constant that represents the primary button on the input device.
- [static var secondary: UIEvent.ButtonMask](./buttonmask-swift.struct/secondary.md)
  A constant that represents the secondary button on the input device.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting the button mask
- [var buttonMask: UIEvent.ButtonMask](./buttonmask-swift.property.md)
  A bit mask that represents which input-device buttons are pressed for the current event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/buttonmask-swift.struct)*