# attributedName

**Framework**: UIKit  
**Kind**: property

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
@MainActor var attributedName: NSAttributedString { get set }
```

## See Also

- [var name: String](uiaccessibilitycustomaction/name.md)
  The localized name of the action.
- [var image: UIImage?](uiaccessibilitycustomaction/image.md)
  An image that represents the action in assistive apps.
- [var actionHandler: UIAccessibilityCustomAction.Handler?](uiaccessibilitycustomaction/actionhandler.md)
  A handler to perform for the action.
- [var target: AnyObject?](uiaccessibilitycustomaction/target.md)
  The object that performs the action.
- [var selector: Selector](uiaccessibilitycustomaction/selector.md)
  The method that performs the action.
- [UIAccessibilityCustomAction.Handler](uiaccessibilitycustomaction/handler.md)
  A closure type that defines a handler to perform for an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/attributedname)*