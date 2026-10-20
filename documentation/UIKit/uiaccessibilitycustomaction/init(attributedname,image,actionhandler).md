# init(attributedName:image:actionHandler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a custom action object with the specified attributed name, image, and action handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(attributedName: NSAttributedString, image: UIImage?, actionHandler: @escaping UIAccessibilityCustomAction.Handler)
```

```objc
- (instancetype) initWithAttributedName:(NSAttributedString *) attributedName image:(UIImage *) image actionHandler:(UIAccessibilityCustomActionHandler) actionHandler;
```

## See Also

### Creating a custom action
- [init(name: String, actionHandler: UIAccessibilityCustomAction.Handler)](./init%28name,actionhandler%29.md)
  Creates a custom action object with the specified name and action handler.
- [init(name: String, target: Any?, selector: Selector)](./init%28name,target,selector%29.md)
  Creates a custom action object with the specified name, target, and selector.
- [init(name: String, image: UIImage?, actionHandler: UIAccessibilityCustomAction.Handler)](./init%28name,image,actionhandler%29.md)
  Creates a custom action object with the specified name, image, and action handler.
- [init(name: String, image: UIImage?, target: Any?, selector: Selector)](./init%28name,image,target,selector%29.md)
  Creates a custom action object with the specified name, image, target, and selector.
- [init(attributedName: NSAttributedString, actionHandler: UIAccessibilityCustomAction.Handler)](./init%28attributedname,actionhandler%29.md)
  Creates a custom action object with the specified attributed name and action handler.
- [init(attributedName: NSAttributedString, target: Any?, selector: Selector)](./init%28attributedname,target,selector%29.md)
  Creates a custom action object with the specified attributed name, target, and selector.
- [init(attributedName: NSAttributedString, image: UIImage?, target: Any?, selector: Selector)](./init%28attributedname,image,target,selector%29.md)
  Creates a custom action object with the specified attributed name, image, target, and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/init(attributedname:image:actionhandler:))*