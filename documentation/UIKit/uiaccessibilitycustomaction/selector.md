# selector

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The method that performs the action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var selector: Selector { get set }
```

```objc
@property (nonatomic, assign) SEL selector;
```

## Discussion

The signature of the selector must take one of the following forms:

```objc
- (BOOL)myPerformActionMethod
- (BOOL)myPerformActionMethod:(UIAccessibilityCustomAction *)action
```

When the user selects a custom action, the assistive technology calls the specified method of the object in the [`target`](./target.md) property. Use your method to perform the indicated action.

## See Also

### Accessing the action parameters
- [var name: String](./name.md)
  The localized name of the action.
- [var attributedName: NSAttributedString](./attributedname.md)
  The localized name of the action as an attributed string.
- [var image: UIImage?](./image.md)
  An image that represents the action in assistive apps.
- [var actionHandler: UIAccessibilityCustomAction.Handler?](./actionhandler.md)
  A handler to perform for the action.
- [var target: AnyObject?](./target.md)
  The object that performs the action.
- [UIAccessibilityCustomAction.Handler](./handler.md)
  A closure type that defines a handler to perform for an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/selector)*