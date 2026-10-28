# accessibilityScroll(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Scrolls screen content in an application-specific way and returns the success or failure of the action.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool
```

```objc
- (BOOL) accessibilityScroll:(UIAccessibilityScrollDirection) direction;
```

## Return Value

[`YES`](../yes.md) if the scrolling action succeeds; otherwise, [`NO`](../no.md). By default, this method returns [`NO`](../no.md).

## Discussion

Implement this method if a view in the view hierarchy supports a scroll by page action.

- If the scrolling action succeeds for the specified direction, return [`YES`](../yes.md) and post the [`pageScrolled`](../../UIKit/uiaccessibility/notification/pagescrolled.md) notification.
- If the scrolling action fails, `accessibilityScroll:` is called on a parent view in the hierarchy.

## Parameters

- `direction`: A constant that specifies the direction of the scrolling action. See [`UIAccessibilityScrollDirection`](../../UIKit/uiaccessibilityscrolldirection.md) for descriptions of valid constants.

## See Also

### Performing an action
- [func accessibilityActivate() -> Bool](./accessibilityactivate%28%29.md)
  Tells the element to activate itself and report the success or failure of the operation.
- [func accessibilityIncrement()](./accessibilityincrement%28%29.md)
  Tells the accessibility element to increment the value of its content.
- [func accessibilityDecrement()](./accessibilitydecrement%28%29.md)
  Tells the accessibility element to decrement the value of its content.
- [func accessibilityPerformEscape() -> Bool](./accessibilityperformescape%28%29.md)
  Dismisses a modal view and returns the success or failure of the action.
- [func accessibilityPerformMagicTap() -> Bool](./accessibilityperformmagictap%28%29.md)
  Performs a salient action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityscroll(_:))*