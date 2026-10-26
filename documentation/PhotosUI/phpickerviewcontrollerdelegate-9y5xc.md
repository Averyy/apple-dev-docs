# PHPickerViewControllerDelegate

**Framework**: PhotosUI  
**Kind**: protocol  
**Role**: Protocol

A protocol the picker uses to communicate user selections.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
@protocol PHPickerViewControllerDelegate <NSObject>
```

## Topics

### Handling User Selection
- [- picker:didFinishPicking:](./phpickerviewcontrollerdelegate-9y5xc/picker_didfinishpicking_.md)
  Notifies the delegate that the user completed a selection or dismissed the picker using the cancel button.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to user selection
- [delegate](./phpickerviewcontroller/delegate-8dlnb.md)
  The picker’s delegate object.
- [PHPickerResult](./phpickerresult-c.class.md)
  Types that represent a selected asset from a person’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontrollerdelegate-9y5xc)*