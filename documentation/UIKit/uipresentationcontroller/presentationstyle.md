# presentationStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The presentation style of the presented view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var presentationStyle: UIModalPresentationStyle { get }
```

```objc
@property (nonatomic, readonly) UIModalPresentationStyle presentationStyle;
```

#### Discussion

This property is set to the presentation style of the presented view controller. The presentation controller uses this style to determine the initial appearance of the presented content.

## See Also

### Getting the presentation attributes
- [func adaptivePresentationStyle(for: UITraitCollection) -> UIModalPresentationStyle](./adaptivepresentationstyle%28for%29.md)
  Returns the presentation style to use for the specified set of traits.
- [var adaptivePresentationStyle: UIModalPresentationStyle](./adaptivepresentationstyle.md)
  Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [var shouldPresentInFullscreen: Bool](./shouldpresentinfullscreen.md)
  A Boolean value indicating whether the presentation covers the entire screen.
- [var shouldRemovePresentersView: Bool](./shouldremovepresentersview.md)
  A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentationstyle)*