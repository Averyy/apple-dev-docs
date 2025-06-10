# UIFocusHeading

**Framework**: UIKit  
**Kind**: struct

The general type of an event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct UIFocusHeading
```

#### Overview

You obtain the direction of the focus from the [`focusHeading`](uifocusupdatecontext/focusheading.md) property.

## Topics

### Constants
- [static var up: UIFocusHeading](uifocusheading/up.md)
  The focus update is heading in the up direction.
- [static var down: UIFocusHeading](uifocusheading/down.md)
  The focus update is heading in the down direction.
- [static var left: UIFocusHeading](uifocusheading/left.md)
  The focus update is heading in the left direction.
- [static var right: UIFocusHeading](uifocusheading/right.md)
  The focus update is heading in the right direction.
- [static var next: UIFocusHeading](uifocusheading/next.md)
  The focus update is heading to the next item.
- [static var previous: UIFocusHeading](uifocusheading/previous.md)
  The focus update is heading to the previous item.
- [static var first: UIFocusHeading](uifocusheading/first.md)
  The focus update is heading to the first item.
- [static var last: UIFocusHeading](uifocusheading/last.md)
  The focus update is heading to the last item.
### Initializers
- [init(rawValue: UInt)](uifocusheading/init(rawvalue:).md)
  Creates a focus heading structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var previouslyFocusedView: UIView?](uifocusupdatecontext/previouslyfocusedview.md)
  The view that was focused before the focus update.
- [var nextFocusedView: UIView?](uifocusupdatecontext/nextfocusedview.md)
  The view that takes the focus after the focus update.
- [var focusHeading: UIFocusHeading](uifocusupdatecontext/focusheading.md)
  The heading in which the focus update is occurring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusheading)*