# accessibilityPerformMagicTap()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Performs a salient action.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityPerformMagicTap() -> Bool
```

```objc
- (BOOL) accessibilityPerformMagicTap;
```

#### Return Value

[`YES`](../yes.md) if the magic tap action succeeds; otherwise, [`NO`](../no.md). By default, this method returns [`NO`](../no.md).

#### Discussion

The exact action performed by this method depends your app, typically toggling the most important state of the app. For example, in the Phone app it answers and ends phone calls, in the Music app it plays and pauses playback, in the Clock app it starts and stops a timer, and in the Camera app it takes a picture.

## See Also

### Performing an action
- [func accessibilityActivate() -> Bool](./accessibilityactivate%28%29.md)
  Tells the element to activate itself and report the success or failure of the operation.
- [func accessibilityIncrement()](./accessibilityincrement%28%29.md)
  Tells the accessibility element to increment the value of its content.
- [func accessibilityDecrement()](./accessibilitydecrement%28%29.md)
  Tells the accessibility element to decrement the value of its content.
- [func accessibilityScroll(UIAccessibilityScrollDirection) -> Bool](./accessibilityscroll%28_%29.md)
  Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [func accessibilityPerformEscape() -> Bool](./accessibilityperformescape%28%29.md)
  Dismisses a modal view and returns the success or failure of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformmagictap())*