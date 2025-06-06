# shouldPresentInFullscreen

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the presentation covers the entire screen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldPresentInFullscreen: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the presentation covers the screen or [`false`](https://developer.apple.com/documentation/swift/false) if it covers all or part of the current view controller only.

#### Discussion

The default implementation of this method returns [`true`](https://developer.apple.com/documentation/swift/true), indicating that the presentation covers the entire screen. You can override this method and return [`false`](https://developer.apple.com/documentation/swift/false) to force the presentation to display only in the current context.

If you override this method, do not call `super`.

## See Also

- [var presentationStyle: UIModalPresentationStyle](uipresentationcontroller/presentationstyle.md)
  The presentation style of the presented view controller.
- [func adaptivePresentationStyle(for: UITraitCollection) -> UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle(for:).md)
  Returns the presentation style to use for the specified set of traits.
- [var adaptivePresentationStyle: UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle.md)
  Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [var shouldRemovePresentersView: Bool](uipresentationcontroller/shouldremovepresentersview.md)
  A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/shouldpresentinfullscreen)*