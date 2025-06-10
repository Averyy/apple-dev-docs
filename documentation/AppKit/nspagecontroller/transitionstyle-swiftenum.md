# NSPageController.TransitionStyle

**Framework**: AppKit  
**Kind**: enum

These constants control the transition style of the page controller.

**Availability**:
- macOS 10.8+

## Declaration

```swift
enum TransitionStyle
```

#### Overview

These transition styles are independent of the delegate’s specification of book or history mode. It is perfectly reasonable to create a history style user interface using the book mode delegate methods. Simply set the transition style appropriately.

## Topics

### Constants
- [NSPageController.TransitionStyle.stackHistory](nspagecontroller/transitionstyle-swift.enum/stackhistory.md)
  Pages are stacked on top of each other. Pages animate out to the right to reveal the previous page. Next pages animate in from the right.
- [NSPageController.TransitionStyle.stackBook](nspagecontroller/transitionstyle-swift.enum/stackbook.md)
  Pages are stacked on top of each other. Pages animate out to the left to reveal the next page. Previous pages animate in from the left.
- [NSPageController.TransitionStyle.horizontalStrip](nspagecontroller/transitionstyle-swift.enum/horizontalstrip.md)
  Each page is laid out next to each other in one long horizontal strip
### Initializers
- [init?(rawValue: Int)](nspagecontroller/transitionstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/transitionstyle-swift.enum)*