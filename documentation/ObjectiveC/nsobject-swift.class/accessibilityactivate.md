# accessibilityActivate()

**Framework**: Objective-C Runtime  
**Kind**: method

Tells the element to activate itself and report the success or failure of the operation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityActivate() -> Bool
```

#### Return Value

[`YES`](yes.md) if the element was activated or [`NO`](no.md) if it was not.

#### Discussion

You can use this method to make complex controls more readily accessible to users. The accessibility system calls this method when a VoiceOver user double taps the selected element. Your implementation of this method should activate the element and perform whatever other tasks it deems appropriate. For example, you might use the method to activate a control that requires a complex gesture and would be difficult for VoiceOver users to perform, possibly because the gesture has a different meaning when VoiceOver is running.

After performing any tasks, return an appropriate Boolean value to indicate success or failure.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityactivate())*