# textInputView

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

An affiliated view that provides a coordinate system for all geometric values in this protocol.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var textInputView: UIView { get }
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)
- [Supporting extended text interactions](support-extended-text-interactions.md)

## See Also

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
- [func cancelAutoscroll()](betextinput/cancelautoscroll.md)
  Indicates autoscrolling is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/textinputview)*