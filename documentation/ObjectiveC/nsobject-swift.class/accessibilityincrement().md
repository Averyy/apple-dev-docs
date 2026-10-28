# accessibilityIncrement()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Tells the accessibility element to increment the value of its content.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityIncrement()
```

```objc
- (void) accessibilityIncrement;
```

## Discussion

If your element has the [`adjustable`](../../UIKit/uiaccessibilitytraits/adjustable.md) trait, you must implement this method. Use this method to increment the value of the element. For example, a [`UISlider`](../../UIKit/uislider.md) object uses this method to increment its value by an appropriate amount.

## See Also

### Performing an action
- [func accessibilityActivate() -> Bool](./accessibilityactivate%28%29.md)
  Tells the element to activate itself and report the success or failure of the operation.
- [func accessibilityDecrement()](./accessibilitydecrement%28%29.md)
  Tells the accessibility element to decrement the value of its content.
- [func accessibilityScroll(UIAccessibilityScrollDirection) -> Bool](./accessibilityscroll%28_%29.md)
  Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [func accessibilityPerformEscape() -> Bool](./accessibilityperformescape%28%29.md)
  Dismisses a modal view and returns the success or failure of the action.
- [func accessibilityPerformMagicTap() -> Bool](./accessibilityperformmagictap%28%29.md)
  Performs a salient action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityincrement())*