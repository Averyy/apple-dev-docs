# UIAccessibilityCustomAction

**Framework**: UIKit  
**Kind**: class

A custom action to perform on an accessible object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAccessibilityCustomAction
```

#### Overview

Apps that support custom actions can create instances of this class, specifying the user-readable name of the action and the object and selector to use when performing the action. Assistive apps display custom actions in response to specific user cues. For example, VoiceOver lets users access actions quickly using the Actions rotor.

After creating an instance of this class, add it to the [`accessibilityCustomActions`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/accessibilityCustomActions) property of an appropriate accessible object.

## Topics

### Creating a custom action
- [init(name: String, actionHandler: UIAccessibilityCustomAction.Handler)](uiaccessibilitycustomaction/init(name:actionhandler:).md)
  Creates a custom action object with the specified name and action handler.
- [init(name: String, target: Any?, selector: Selector)](uiaccessibilitycustomaction/init(name:target:selector:).md)
  Creates a custom action object with the specified name, target, and selector.
- [init(name: String, image: UIImage?, actionHandler: UIAccessibilityCustomAction.Handler)](uiaccessibilitycustomaction/init(name:image:actionhandler:).md)
  Creates a custom action object with the specified name, image, and action handler.
- [init(name: String, image: UIImage?, target: Any?, selector: Selector)](uiaccessibilitycustomaction/init(name:image:target:selector:).md)
  Creates a custom action object with the specified name, image, target, and selector.
- [init(attributedName: NSAttributedString, actionHandler: UIAccessibilityCustomAction.Handler)](uiaccessibilitycustomaction/init(attributedname:actionhandler:).md)
  Creates a custom action object with the specified attributed name and action handler.
- [init(attributedName: NSAttributedString, target: Any?, selector: Selector)](uiaccessibilitycustomaction/init(attributedname:target:selector:).md)
  Creates a custom action object with the specified attributed name, target, and selector.
- [init(attributedName: NSAttributedString, image: UIImage?, actionHandler: UIAccessibilityCustomAction.Handler)](uiaccessibilitycustomaction/init(attributedname:image:actionhandler:).md)
  Creates a custom action object with the specified attributed name, image, and action handler.
- [init(attributedName: NSAttributedString, image: UIImage?, target: Any?, selector: Selector)](uiaccessibilitycustomaction/init(attributedname:image:target:selector:).md)
  Creates a custom action object with the specified attributed name, image, target, and selector.
### Accessing the action parameters
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
- [var selector: Selector](uiaccessibilitycustomaction/selector.md)
  The method that performs the action.
- [UIAccessibilityCustomAction.Handler](uiaccessibilitycustomaction/handler.md)
  A closure type that defines a handler to perform for an action.
### Type Properties
- [class let editCategory: String](uiaccessibilitycustomaction/editcategory.md)
### Instance Properties
- [var category: String?](uiaccessibilitycustomaction/category.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIAccessibilityAction](../ObjectiveC/uiaccessibilityaction.md)
  A set of methods that accessibility elements can use to support specific actions.
- [UIAccessibilityCustomAction.Handler](uiaccessibilitycustomaction/handler.md)
  A closure type that defines a handler to perform for an action.
- [Delivering an exceptional accessibility experience](../Accessibility/delivering_an_exceptional_accessibility_experience.md)
  Make improvements to your app’s interaction model to support assistive technologies such as VoiceOver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction)*