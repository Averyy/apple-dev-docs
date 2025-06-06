# presentationStyle

**Framework**: UIKit  
**Kind**: property

The presentation style of the presented view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var presentationStyle: UIModalPresentationStyle { get }
```

#### Discussion

This property is set to the presentation style of the presented view controller. The presentation controller uses this style to determine the initial appearance of the presented content.

## See Also

- [func adaptivePresentationStyle(for: UITraitCollection) -> UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle(for:).md)
  Returns the presentation style to use for the specified set of traits.
- [var adaptivePresentationStyle: UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle.md)
  Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [var shouldPresentInFullscreen: Bool](uipresentationcontroller/shouldpresentinfullscreen.md)
  A Boolean value indicating whether the presentation covers the entire screen.
- [var shouldRemovePresentersView: Bool](uipresentationcontroller/shouldremovepresentersview.md)
  A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentationstyle)*