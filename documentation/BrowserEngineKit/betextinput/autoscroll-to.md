# autoscroll(to:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Indicates autoscrolling has been triggered by a text interaction gesture.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func autoscroll(to point: CGPoint)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

Called repeatedly during range adjustment gestures, or when placing the text cursor.

The given point is in the coordinate space of the `textInputView`.

Indicates that a text gesture initiated autoscrolling.

#### Overview

The text system calls the method repeatedly when a gesture requires the text view to scroll, for example, when a person adjusts the text selection range, or places the text cursor. The text system sends [`cancelAutoscroll()`](betextinput/cancelautoscroll().md) when there are no further updates.

## Parameters

- `point`: The location to which to autoscroll, in the coordinate system of your view’s  .

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
- [func cancelAutoscroll()](betextinput/cancelautoscroll.md)
  Indicates autoscrolling is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/autoscroll(to:))*