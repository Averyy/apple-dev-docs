# accessibilityDecrement()

**Framework**: Objective-C Runtime  
**Kind**: method

Tells the accessibility element to decrement the value of its content.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityDecrement()
```

#### Discussion

If your element has the [`adjustable`](https://developer.apple.com/documentation/UIKit/UIAccessibilityTraits/adjustable) trait, you must implement this method. Use this method to decrement the value of the element. For example, a [`UISlider`](https://developer.apple.com/documentation/UIKit/UISlider) object uses this method to decrement its value by an appropriate amount.

## See Also

- [func accessibilityActivate() -> Bool](nsobject-swift.class/accessibilityactivate.md)
  Tells the element to activate itself and report the success or failure of the operation.
- [func accessibilityIncrement()](nsobject-swift.class/accessibilityincrement.md)
  Tells the accessibility element to increment the value of its content.
- [func accessibilityScroll(UIAccessibilityScrollDirection) -> Bool](nsobject-swift.class/accessibilityscroll(_:).md)
  Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [func accessibilityPerformEscape() -> Bool](nsobject-swift.class/accessibilityperformescape.md)
  Dismisses a modal view and returns the success or failure of the action.
- [func accessibilityPerformMagicTap() -> Bool](nsobject-swift.class/accessibilityperformmagictap.md)
  Performs a salient action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitydecrement())*