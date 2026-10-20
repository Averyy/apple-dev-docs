# action

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The selector identifying the action method called after the user selects the command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var action: Selector { get }
```

```objc
@property (nonatomic, readonly) SEL action;
```

## See Also

### Getting information about the command
- [var title: String](./title.md)
  The command’s title.
- [var image: UIImage?](./image.md)
  The command’s image.
- [var discoverabilityTitle: String?](./discoverabilitytitle.md)
  An elaborated title that explains the purpose of the command.
- [var attributes: UIMenuElement.Attributes](./attributes.md)
  The attributes indicating the style of the command.
- [var state: UIMenuElement.State](./state.md)
  The state of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand/action)*