# UIAccessibilityAction

**Framework**: Objective-C Runtime

A set of methods that accessibility elements can use to support specific actions.

#### Overview

The `UIAccessibilityAction` informal protocol provides a way for accessibility elements to support specific actions, such as selecting values in a range or scrolling through information on the screen. For example, to respond to a scrolling gesture, you implement the [`accessibilityScroll(_:)`](nsobject-swift.class/accessibilityscroll(_:).md) method and post [`pageScrolled`](https://developer.apple.com/documentation/UIKit/UIAccessibility/Notification/pageScrolled) with the new page status (such as “Page 3 of 9”). Or, to make an element such as a slider or picker view accessible, you first need to characterize it by including the [`adjustable`](https://developer.apple.com/documentation/UIKit/UIAccessibilityTraits/adjustable) trait. Then, you must implement the [`accessibilityIncrement()`](nsobject-swift.class/accessibilityincrement().md) and [`accessibilityDecrement()`](nsobject-swift.class/accessibilitydecrement().md) methods. When you do this, assistive technology users can adjust the element using gestures specific to the assistive technology.

## Topics

### Performing an action
- [func accessibilityActivate() -> Bool](nsobject-swift.class/accessibilityactivate.md)
  Tells the element to activate itself and report the success or failure of the operation.
- [func accessibilityIncrement()](nsobject-swift.class/accessibilityincrement.md)
  Tells the accessibility element to increment the value of its content.
- [func accessibilityDecrement()](nsobject-swift.class/accessibilitydecrement.md)
  Tells the accessibility element to decrement the value of its content.
- [func accessibilityScroll(UIAccessibilityScrollDirection) -> Bool](nsobject-swift.class/accessibilityscroll(_:).md)
  Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [func accessibilityPerformEscape() -> Bool](nsobject-swift.class/accessibilityperformescape.md)
  Dismisses a modal view and returns the success or failure of the action.
- [func accessibilityPerformMagicTap() -> Bool](nsobject-swift.class/accessibilityperformmagictap.md)
  Performs a salient action.
### Accessing custom actions
- [var accessibilityCustomActions: [UIAccessibilityCustomAction]?](nsobject-swift.class/accessibilitycustomactions.md)
  An array of custom actions to display along with the built-in actions.
### Constants
- [enum UIAccessibilityScrollDirection](../UIKit/UIAccessibilityScrollDirection.md)
  The direction of a scrolling action.

## See Also

- [Accessibility Programming Guide for iOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785)
- [UIAccessibility](../UIKit/uiaccessibility-protocol.md)
  A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [UIAccessibilityContainer](../UIKit/uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [UIAccessibilityFocus](uiaccessibilityfocus.md)
  An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [UIAccessibilityDragging](uiaccessibilitydragging.md)
  A pair of properties to allow you to fine-tune how drags and drops are exposed to assistive technologies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/uiaccessibilityaction)*