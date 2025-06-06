# shouldRemovePresentersView

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldRemovePresentersView: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view should be removed or [`false`](https://developer.apple.com/documentation/swift/false) if it should not.

#### Discussion

The default implementation of this method returns [`false`](https://developer.apple.com/documentation/swift/false). If you implement a presentation that does not cover the presenting view controller’s content entirely, override this method and return [`false`](https://developer.apple.com/documentation/swift/false).

If you override this method, do not call `super`.

## See Also

- [var presentationStyle: UIModalPresentationStyle](uipresentationcontroller/presentationstyle.md)
  The presentation style of the presented view controller.
- [func adaptivePresentationStyle(for: UITraitCollection) -> UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle(for:).md)
  Returns the presentation style to use for the specified set of traits.
- [var adaptivePresentationStyle: UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle.md)
  Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [var shouldPresentInFullscreen: Bool](uipresentationcontroller/shouldpresentinfullscreen.md)
  A Boolean value indicating whether the presentation covers the entire screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/shouldremovepresentersview)*