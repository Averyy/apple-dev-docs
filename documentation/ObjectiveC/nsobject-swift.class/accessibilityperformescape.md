# accessibilityPerformEscape()

**Framework**: Objective-C Runtime  
**Kind**: method

Dismisses a modal view and returns the success or failure of the action.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityPerformEscape() -> Bool
```

#### Return Value

[`YES`](yes.md) if the modal view is successfully dismissed; otherwise, [`NO`](no.md). By default, this method returns [`NO`](no.md).

#### Discussion

Implement this method on an element or containing view that can be revealed modally or in a hierarchy. When a VoiceOver user performs a dismiss action, this method dismisses the view. For example, you might implement this method for a popover in order to give users a deliberate dismiss action to perform that closes the popover.

## See Also

- [func accessibilityActivate() -> Bool](nsobject-swift.class/accessibilityactivate.md)
  Tells the element to activate itself and report the success or failure of the operation.
- [func accessibilityIncrement()](nsobject-swift.class/accessibilityincrement.md)
  Tells the accessibility element to increment the value of its content.
- [func accessibilityDecrement()](nsobject-swift.class/accessibilitydecrement.md)
  Tells the accessibility element to decrement the value of its content.
- [func accessibilityScroll(UIAccessibilityScrollDirection) -> Bool](nsobject-swift.class/accessibilityscroll(_:).md)
  Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [func accessibilityPerformMagicTap() -> Bool](nsobject-swift.class/accessibilityperformmagictap.md)
  Performs a salient action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformescape())*