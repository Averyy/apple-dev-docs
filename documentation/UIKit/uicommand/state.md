# state

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The state of the command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var state: UIMenuElement.State { get set }
```

```objc
@property (nonatomic) UIMenuElementState state;
```

## See Also

### Getting information about the command
- [var title: String](./title.md)
  The command’s title.
- [var image: UIImage?](./image.md)
  The command’s image.
- [var action: Selector](./action.md)
  The selector identifying the action method called after the user selects the command.
- [var discoverabilityTitle: String?](./discoverabilitytitle.md)
  An elaborated title that explains the purpose of the command.
- [var attributes: UIMenuElement.Attributes](./attributes.md)
  The attributes indicating the style of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand/state)*