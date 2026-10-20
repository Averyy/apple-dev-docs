# focusHeading

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The heading in which the focus update is occurring.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var focusHeading: UIFocusHeading { get }
```

```objc
@property (nonatomic, assign, readonly) UIFocusHeading focusHeading;
```

#### Discussion

To view all the possible focus heading directions, see the [`UIFocusHeading`](../uifocusheading.md) data type.

## See Also

### Locating focus direction
- [var previouslyFocusedView: UIView?](./previouslyfocusedview.md)
  The view that was focused before the focus update.
- [var nextFocusedView: UIView?](./nextfocusedview.md)
  The view that takes the focus after the focus update.
- [struct UIFocusHeading](../uifocusheading.md)
  The general type of an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/focusheading)*