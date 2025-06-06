# CPButton

**Framework**: CarPlay  
**Kind**: class

A button that displays an image and invokes a handler when the user taps it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPButton
```

#### Overview

You create instances of `CPButton` to provide a template’s actions. The button displays a custom image that communicates its function. When a user taps the button, CarPlay invokes the handler you provide. The template that contains the button manages its appearance.

The framework provides specialized subclasses for common actions, such as [`CPContactCallButton`](cpcontactcallbutton.md) or [`CPContactMessageButton`](cpcontactmessagebutton.md).

## Topics

### Creating a Button
- [init(image: UIImage, handler: ((CPButton) -> Void)?)](cpbutton/init(image:handler:).md)
  Creates a button that displays an image and invokes a handler when the user taps it.
- [let CPButtonMaximumImageSize: CGSize](cpbuttonmaximumimagesize.md)
  The maximum size of a button’s image that CarPlay supports.
### Getting the Button’s Image
- [var image: UIImage?](cpbutton/image.md)
  The button’s image.
### Configuring the Button’s Attributes
- [var title: String?](cpbutton/title.md)
  The button’s title.
- [var isEnabled: Bool](cpbutton/isenabled.md)
  A Boolean value that determines whether the button is in an enabled state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CPContactCallButton](cpcontactcallbutton.md)
- [CPContactDirectionsButton](cpcontactdirectionsbutton.md)
- [CPContactMessageButton](cpcontactmessagebutton.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CPImageSet](cpimageset.md)
  Light and dark representations of an image.
- [let CarPlayErrorDomain: String](carplayerrordomain.md)
  The domain that CarPlay uses for any errors it provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbutton)*