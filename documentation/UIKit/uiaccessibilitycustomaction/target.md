# target

**Framework**: UIKit  
**Kind**: property

The object that performs the action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var target: AnyObject? { get set }
```

## See Also

- [var name: String](uiaccessibilitycustomaction/name.md)
  The localized name of the action.
- [var attributedName: NSAttributedString](uiaccessibilitycustomaction/attributedname.md)
  The localized name of the action as an attributed string.
- [var image: UIImage?](uiaccessibilitycustomaction/image.md)
  An image that represents the action in assistive apps.
- [var actionHandler: UIAccessibilityCustomAction.Handler?](uiaccessibilitycustomaction/actionhandler.md)
  A handler to perform for the action.
- [var selector: Selector](uiaccessibilitycustomaction/selector.md)
  The method that performs the action.
- [UIAccessibilityCustomAction.Handler](uiaccessibilitycustomaction/handler.md)
  A closure type that defines a handler to perform for an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/target)*