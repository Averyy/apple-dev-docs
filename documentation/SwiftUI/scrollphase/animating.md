# ScrollPhase.animating

**Framework**: SwiftUI  
**Kind**: case

The animating phase where the scroll view is animating towards a final target.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case animating
```

#### Discussion

This phase is the result of a programmatic scroll when using a [`ScrollViewReader`](scrollviewreader.md) or [`scrollPosition(id:anchor:)`](view/scrollposition(id:anchor:).md) modifier.

SwiftUI provides you a value of this type when using the [`onScrollPhaseChange(_:)`](view/onscrollphasechange(_:).md) modifier with a scrollable view like [`ScrollView`](scrollview.md) or [`List`](list.md).

## See Also

- [ScrollPhase.decelerating](scrollphase/decelerating.md)
  The decelerating phase where the user use has stopped interacting with the scroll view and the scroll view is decelerating towards its final target.
- [ScrollPhase.idle](scrollphase/idle.md)
  The idle phase where no kind of scrolling is occurring.
- [ScrollPhase.interacting](scrollphase/interacting.md)
  The interacting phase where the user is interacting with the scroll view.
- [ScrollPhase.tracking](scrollphase/tracking.md)
  The tracking phase where the scroll view is tracking a potential scroll by the user but the user hasn’t started a scroll.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollphase/animating)*