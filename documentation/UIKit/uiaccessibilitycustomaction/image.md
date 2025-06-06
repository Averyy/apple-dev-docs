# image

**Framework**: UIKit  
**Kind**: property

An image that represents the action in assistive apps.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var image: UIImage? { get set }
```

## See Also

- [var name: String](uiaccessibilitycustomaction/name.md)
  The localized name of the action.
- [var attributedName: NSAttributedString](uiaccessibilitycustomaction/attributedname.md)
  The localized name of the action as an attributed string.
- [var actionHandler: UIAccessibilityCustomAction.Handler?](uiaccessibilitycustomaction/actionhandler.md)
  A handler to perform for the action.
- [var target: AnyObject?](uiaccessibilitycustomaction/target.md)
  The object that performs the action.
- [var selector: Selector](uiaccessibilitycustomaction/selector.md)
  The method that performs the action.
- [UIAccessibilityCustomAction.Handler](uiaccessibilitycustomaction/handler.md)
  A closure type that defines a handler to perform for an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/image)*