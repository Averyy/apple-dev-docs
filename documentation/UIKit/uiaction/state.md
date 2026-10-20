# state

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The state of the action.

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

### Getting information about the action
- [var title: String](./title.md)
  The action’s title.
- [var image: UIImage?](./image.md)
  The action’s image.
- [var identifier: UIAction.Identifier](./identifier-swift.property.md)
  The unique identifier for the action.
- [var discoverabilityTitle: String?](./discoverabilitytitle.md)
  An elaborated title that explains the purpose of the action.
- [var attributes: UIMenuElement.Attributes](./attributes.md)
  The attributes indicating the style of the action.
- [var sender: Any?](./sender.md)
  The object responsible for the action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/state)*