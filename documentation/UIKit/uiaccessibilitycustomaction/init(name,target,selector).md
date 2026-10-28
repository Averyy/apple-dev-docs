# init(name:target:selector:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a custom action object with the specified name, target, and selector.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(name: String, target: Any?, selector: Selector)
```

```objc
- (instancetype) initWithName:(NSString *) name target:(id) target selector:(SEL) selector;
```

## Return Value

An initialized custom action object.

## Parameters

- `name`: The localized name of the action. Provide a short and descriptive name for the action.
- `target`: The object that performs the action.
- `selector`: The selector of `target` to call when you want to perform the action. The method signature must take one of the following forms:

  ```objc
  - (BOOL)myPerformActionMethod
  - (BOOL)myPerformActionMethod:(UIAccessibilityCustomAction *)action
  ```

## See Also

### Creating a custom action
- [init(name: String, actionHandler: UIAccessibilityCustomAction.Handler)](./init%28name,actionhandler%29.md)
  Creates a custom action object with the specified name and action handler.
- [init(name: String, image: UIImage?, actionHandler: UIAccessibilityCustomAction.Handler)](./init%28name,image,actionhandler%29.md)
  Creates a custom action object with the specified name, image, and action handler.
- [init(name: String, image: UIImage?, target: Any?, selector: Selector)](./init%28name,image,target,selector%29.md)
  Creates a custom action object with the specified name, image, target, and selector.
- [init(attributedName: NSAttributedString, actionHandler: UIAccessibilityCustomAction.Handler)](./init%28attributedname,actionhandler%29.md)
  Creates a custom action object with the specified attributed name and action handler.
- [init(attributedName: NSAttributedString, target: Any?, selector: Selector)](./init%28attributedname,target,selector%29.md)
  Creates a custom action object with the specified attributed name, target, and selector.
- [init(attributedName: NSAttributedString, image: UIImage?, actionHandler: UIAccessibilityCustomAction.Handler)](./init%28attributedname,image,actionhandler%29.md)
  Creates a custom action object with the specified attributed name, image, and action handler.
- [init(attributedName: NSAttributedString, image: UIImage?, target: Any?, selector: Selector)](./init%28attributedname,image,target,selector%29.md)
  Creates a custom action object with the specified attributed name, image, target, and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/init(name:target:selector:))*