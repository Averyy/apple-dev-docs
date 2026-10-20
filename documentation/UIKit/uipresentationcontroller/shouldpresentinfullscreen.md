# shouldPresentInFullscreen

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the presentation covers the entire screen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var shouldPresentInFullscreen: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL shouldPresentInFullscreen;
```

#### Return Value

[`true`](../../Swift/true.md) if the presentation covers the screen or [`false`](../../Swift/false.md) if it covers all or part of the current view controller only.

#### Discussion

The default implementation of this method returns [`true`](../../Swift/true.md), indicating that the presentation covers the entire screen. You can override this method and return [`false`](../../Swift/false.md) to force the presentation to display only in the current context.

If you override this method, do not call `super`.

## See Also

### Getting the presentation attributes
- [var presentationStyle: UIModalPresentationStyle](./presentationstyle.md)
  The presentation style of the presented view controller.
- [func adaptivePresentationStyle(for: UITraitCollection) -> UIModalPresentationStyle](./adaptivepresentationstyle%28for%29.md)
  Returns the presentation style to use for the specified set of traits.
- [var adaptivePresentationStyle: UIModalPresentationStyle](./adaptivepresentationstyle.md)
  Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [var shouldRemovePresentersView: Bool](./shouldremovepresentersview.md)
  A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/shouldpresentinfullscreen)*