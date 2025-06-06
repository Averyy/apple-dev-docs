# actionHandler

**Framework**: UIKit  
**Kind**: property

A handler to perform for the action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var actionHandler: UIAccessibilityCustomAction.Handler? { get set }
```

#### Discussion

If you set this property, the system chooses this action handler over the [`target`](uiaccessibilitycustomaction/target.md) and [`selector`](uiaccessibilitycustomaction/selector.md).

## See Also

- [var name: String](uiaccessibilitycustomaction/name.md)
  The localized name of the action.
- [var attributedName: NSAttributedString](uiaccessibilitycustomaction/attributedname.md)
  The localized name of the action as an attributed string.
- [var image: UIImage?](uiaccessibilitycustomaction/image.md)
  An image that represents the action in assistive apps.
- [var target: AnyObject?](uiaccessibilitycustomaction/target.md)
  The object that performs the action.
- [var selector: Selector](uiaccessibilitycustomaction/selector.md)
  The method that performs the action.
- [UIAccessibilityCustomAction.Handler](uiaccessibilitycustomaction/handler.md)
  A closure type that defines a handler to perform for an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/actionhandler)*