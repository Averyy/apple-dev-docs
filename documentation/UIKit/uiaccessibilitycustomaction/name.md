# name

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The localized name of the action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

```objc
@property (nonatomic, copy) NSString * name;
```

## See Also

### Accessing the action parameters
- [var attributedName: NSAttributedString](./attributedname.md)
  The localized name of the action as an attributed string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/name)*