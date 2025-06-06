# cancelAutoscroll()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Indicates autoscrolling is complete.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func cancelAutoscroll()
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

There will be no more calls into`autoscrollToPoint` until a text interaction gesture starts autoscrolling.

Indicates that the current autoscroll gesture is complete.

#### Overview

When the text system calls this method on your text view, there are no more calls to [`autoscroll(to:)`](betextinput/autoscroll(to:).md) for the current text interaction gesture.

## See Also

- [var textInputView: UIView](betextinput/textinputview.md)
  An affiliated view that provides a coordinate system for all geometric values in this protocol.
- [var textFirstRect: CGRect](betextinput/textfirstrect.md)
  Returns a rect representing the bounds of the first line of marked text, if marked text is set.
- [var textLastRect: CGRect](betextinput/textlastrect.md)
  Returns a rect representing the bounds of the last line of marked text, if marked text is set.
- [var unobscuredContentRect: CGRect](betextinput/unobscuredcontentrect.md)
  Rect used to place UI (such as selection handles) in a location that isn’t obscurred by app UI.
- [var unscaledView: UIView](betextinput/unscaledview.md)
  View representing the web content that is agnostic of zoom state. Used to draw zoom agnostic system UI elements, such as the selection handles
- [var selectionClipRect: CGRect](betextinput/selectioncliprect.md)
  Rect representing the bounds of editable elements, used to ensure and UI don’t overflow outside them
- [func autoscroll(to: CGPoint)](betextinput/autoscroll(to:).md)
  Indicates autoscrolling has been triggered by a text interaction gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/cancelautoscroll())*