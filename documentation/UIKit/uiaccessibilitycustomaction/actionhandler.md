# actionHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A handler to perform for the action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var actionHandler: UIAccessibilityCustomAction.Handler? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIAccessibilityCustomActionHandler actionHandler;
```

#### Discussion

If you set this property, the system chooses this action handler over the [`target`](./target.md) and [`selector`](./selector.md).

## See Also

### Accessing the action parameters
- [var name: String](./name.md)
  The localized name of the action.
- [var attributedName: NSAttributedString](./attributedname.md)
  The localized name of the action as an attributed string.
- [var image: UIImage?](./image.md)
  An image that represents the action in assistive apps.
- [var target: AnyObject?](./target.md)
  The object that performs the action.
- [var selector: Selector](./selector.md)
  The method that performs the action.
- [UIAccessibilityCustomAction.Handler](./handler.md)
  A closure type that defines a handler to perform for an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/actionhandler)*