# attributedName

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The localized name of the action as an attributed string.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var attributedName: NSAttributedString { get set }
```

```objc
@property (nonatomic, copy) NSAttributedString * attributedName;
```

## See Also

### Accessing the action parameters
- [var name: String](./name.md)
  The localized name of the action.
- [var image: UIImage?](./image.md)
  An image that represents the action in assistive apps.
- [var actionHandler: UIAccessibilityCustomAction.Handler?](./actionhandler.md)
  A handler to perform for the action.
- [var target: AnyObject?](./target.md)
  The object that performs the action.
- [var selector: Selector](./selector.md)
  The method that performs the action.
- [UIAccessibilityCustomAction.Handler](./handler.md)
  A closure type that defines a handler to perform for an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/attributedname)*