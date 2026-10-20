# shouldRemovePresentersView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var shouldRemovePresentersView: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL shouldRemovePresentersView;
```

#### Return Value

[`true`](../../Swift/true.md) if the view should be removed or [`false`](../../Swift/false.md) if it should not.

#### Discussion

The default implementation of this method returns [`false`](../../Swift/false.md). If you implement a presentation that does not cover the presenting view controller’s content entirely, override this method and return [`false`](../../Swift/false.md).

If you override this method, do not call `super`.

## See Also

### Getting the presentation attributes
- [var presentationStyle: UIModalPresentationStyle](./presentationstyle.md)
  The presentation style of the presented view controller.
- [func adaptivePresentationStyle(for: UITraitCollection) -> UIModalPresentationStyle](./adaptivepresentationstyle%28for%29.md)
  Returns the presentation style to use for the specified set of traits.
- [var adaptivePresentationStyle: UIModalPresentationStyle](./adaptivepresentationstyle.md)
  Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [var shouldPresentInFullscreen: Bool](./shouldpresentinfullscreen.md)
  A Boolean value indicating whether the presentation covers the entire screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/shouldremovepresentersview)*