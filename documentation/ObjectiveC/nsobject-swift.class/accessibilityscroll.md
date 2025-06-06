# accessibilityScroll(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Scrolls screen content in an application-specific way and returns the success or failure of the action.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool
```

#### Return Value

[`YES`](yes.md) if the scrolling action succeeds; otherwise, [`NO`](no.md). By default, this method returns [`NO`](no.md).

#### Discussion

Implement this method if a view in the view hierarchy supports a scroll by page action.

- If the scrolling action succeeds for the specified direction, return [`YES`](yes.md) and post the [`pageScrolled`](https://developer.apple.com/documentation/UIKit/UIAccessibility/Notification/pageScrolled) notification.
- If the scrolling action fails, `accessibilityScroll:` is called on a parent view in the hierarchy.

## Parameters

- `direction`: A constant that specifies the direction of the scrolling action. See   for descriptions of valid constants.

## See Also

- [func accessibilityActivate() -> Bool](nsobject-swift.class/accessibilityactivate.md)
  Tells the element to activate itself and report the success or failure of the operation.
- [func accessibilityIncrement()](nsobject-swift.class/accessibilityincrement.md)
  Tells the accessibility element to increment the value of its content.
- [func accessibilityDecrement()](nsobject-swift.class/accessibilitydecrement.md)
  Tells the accessibility element to decrement the value of its content.
- [func accessibilityPerformEscape() -> Bool](nsobject-swift.class/accessibilityperformescape.md)
  Dismisses a modal view and returns the success or failure of the action.
- [func accessibilityPerformMagicTap() -> Bool](nsobject-swift.class/accessibilityperformmagictap.md)
  Performs a salient action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityscroll(_:))*