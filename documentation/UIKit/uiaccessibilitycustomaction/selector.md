# selector

**Framework**: UIKit  
**Kind**: property

The method that performs the action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selector: Selector { get set }
```

#### Discussion

The signature of the selector must take one of the following forms:

```objc
- (BOOL)myPerformActionMethod
- (BOOL)myPerformActionMethod:(UIAccessibilityCustomAction *)action
```

When the user selects a custom action, the assistive technology calls the specified method of the object in the [`target`](uiaccessibilitycustomaction/target.md) property. Use your method to perform the indicated action.

## See Also

- [var name: String](uiaccessibilitycustomaction/name.md)
  The localized name of the action.
- [var attributedName: NSAttributedString](uiaccessibilitycustomaction/attributedname.md)
  The localized name of the action as an attributed string.
- [var image: UIImage?](uiaccessibilitycustomaction/image.md)
  An image that represents the action in assistive apps.
- [var actionHandler: UIAccessibilityCustomAction.Handler?](uiaccessibilitycustomaction/actionhandler.md)
  A handler to perform for the action.
- [var target: AnyObject?](uiaccessibilitycustomaction/target.md)
  The object that performs the action.
- [UIAccessibilityCustomAction.Handler](uiaccessibilitycustomaction/handler.md)
  A closure type that defines a handler to perform for an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/selector)*