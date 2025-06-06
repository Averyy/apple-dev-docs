# accessibilityPerformMagicTap()

**Framework**: Objective-C Runtime  
**Kind**: method

Performs a salient action.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityPerformMagicTap() -> Bool
```

#### Return Value

[`YES`](yes.md) if the magic tap action succeeds; otherwise, [`NO`](no.md). By default, this method returns [`NO`](no.md).

#### Discussion

The exact action performed by this method depends your app, typically toggling the most important state of the app. For example, in the Phone app it answers and ends phone calls, in the Music app it plays and pauses playback, in the Clock app it starts and stops a timer, and in the Camera app it takes a picture.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformmagictap())*