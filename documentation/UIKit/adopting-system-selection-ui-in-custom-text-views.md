# Adopting system selection UI in custom text views

**Framework**: UIKit

Incorporate the system text-selection experience into your custom text UI in UIKit.

#### Overview

People can enter text into your app in a variety of ways, such as typing, copy and paste, or dictation. iOS 17 introduces changes to the system UI for inserting and selecting text to provide a more seamless text experience.

If your app handles text input through standard UIKit views such as [`UITextView`](uitextview.md) or [`UITextField`](uitextfield.md), your app automatically uses the system UI for inserting and selecting text. This system selection UI includes the following elements:

- The text cursor that indicates the insertion point of the text
- The highlight behind the selected text
- Selection handles for selecting ranges of text
- The loupe for placing the text cursor in large bodies of text

If you have a highly customized UI for displaying text, you can adopt this system selection UI in your UIKit app. In most cases involving text selection display and interaction, use [`UITextInteraction`](uitextinteraction.md), which includes the system selection UI and standard gesture recognizers to let people modify the selection state in your custom text view. If you want to implement the selection gestures yourself, but still want to indicate text selection using the standard system UI, use [`UITextSelectionDisplayInteraction`](uitextselectiondisplayinteraction.md) instead. This article describes the steps for adopting [`UITextSelectionDisplayInteraction`](uitextselectiondisplayinteraction.md).

##### Add the System Selection Ui to a Custom Text View

If your app handles text input through a custom text view that builds on [`UITextInput`](uitextinput.md), you can display the system selection UI manually. Create a [`UITextSelectionDisplayInteraction`](uitextselectiondisplayinteraction.md) interaction and add it to your custom text view that adopts [`UITextInput`](uitextinput.md).

```swift
// Set up the interaction.
let selectionDisplayInteraction = UITextSelectionDisplayInteraction(textInput: documentView,
                                                     delegate: self)
documentView.addInteraction(selectionDisplayInteraction)
```

When your custom text view becomes active or becomes first responder, activate the interaction.

```swift
// Activate the interaction when the text view becomes active.
func didBecomeActive() {
    selectionDisplayInteraction.isActivated = true
}
```

##### Update the Text Selection

When a person interacts with text in your custom text view, notify the interaction as the state of the text selection changes.

```swift
// Notify the interaction when the text selection changes.
func didChangeSelection() {
    selectionDisplayInteraction.setNeedsSelectionUpdate()
}
```

After you call [`setNeedsSelectionUpdate()`](uitextselectiondisplayinteraction/setneedsselectionupdate().md), the interaction retrieves the latest information about the current text selection from [`textInput`](uitextselectiondisplayinteraction/textinput.md) so it can redraw the selection UI.

##### Customize the System Selection Ui Elements

You might want further customization to the system selection UI to match your custom text view’s style and behavior. You can customize various properties on [`UITextSelectionDisplayInteraction`](uitextselectiondisplayinteraction.md).

- The [`cursorView`](uitextselectiondisplayinteraction/cursorview.md) property represents the text cursor. You can customize the state of the text cursor’s blinking animation.
- The [`highlightView`](uitextselectiondisplayinteraction/highlightview.md) property represents the highlight behind the selected text. You can customize the shape of the selection to draw a custom highlight.
- The [`handleViews`](uitextselectiondisplayinteraction/handleviews.md) property represents the selection handles for selecting ranges of text. You can customize the appearance of the handles by defining a custom shape or specifying the orientation of the handles.

##### Enhance Text Cursor Placement with the Text Loupe

Your custom text view can also display the system UI for the loupe, which people use for placing the text cursor in large bodies of text. When a person interacts with your custom text view in a way that you want to display the loupe, such as a pan gesture, call [`begin(at:fromSelectionWidgetView:in:)`](uitextloupesession/begin(at:fromselectionwidgetview:in:).md) on a [`UITextLoupeSession`](uitextloupesession.md) object. The system animates the presentation and placement of the loupe according to the starting point you provide. Call [`move(to:withCaretRect:trackingCaret:)`](uitextloupesession/move(to:withcaretrect:trackingcaret:).md) to track the movement of the loupe as a person moves the text cursor, and [`invalidate()`](uitextloupesession/invalidate().md) to hide the loupe and end the session.

The following code shows how to show the loupe using a pan gesture recognizer.

```swift
// Show a loupe with a pan gesture.
var loupeSession: UITextLoupeSession?

func didRecognizePanGesture(_ gesture: UIPanGestureRecognizer) {
    let location = gesture.location(in: view)
    let cursorView = selectionDisplayInteraction.cursorView
    switch gesture.state {
    case .began:
        loupeSession = UITextLoupeSession.begin(at: location,
                                                fromSelectionWidgetView: cursorView,
                                                in: view)
    case .changed:
        loupeSession?.move(to: location, withCaretRect: cursorView.frame,
                           trackingCaret: true)
    case .ended, .cancelled, .failed:
        loupeSession?.invalidate()
        loupeSession = nil
    default:
        break
    }
}
```

##### Hide the System Selection Ui

When your custom text view becomes inactive or resigns first responder status, make sure to deactivate the interaction.

```swift
// Deactivate the interaction when the text view becomes inactive.
func didBecomeInactive() {
    selectionDisplayInteraction.isActivated = false
}
```

If you implement custom text UI in an AppKit app, see [`Adopting the system text cursor in custom text views`](https://developer.apple.com/documentation/AppKit/adopting-the-system-text-cursor-in-custom-text-views).

> **Note**:  Session 10058: [`What’s new with text and text interactions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10058/)

## See Also

- [class UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md)
  An object that provides the system UI for displaying text selection.
- [protocol UITextSelectionHighlightView](uitextselectionhighlightview.md)
  An interface you use to provide a custom highlight UI behind the selected text.
- [protocol UITextSelectionHandleView](uitextselectionhandleview.md)
  An interface you use to draw custom the selection handles for ranges of text.
- [protocol UITextCursorView](uitextcursorview.md)
  An interface you use to draw the insertion point in a piece of text.
- [class UIStandardTextCursorView](uistandardtextcursorview.md)
  A view that draws the standard system insertion point in a piece of text.
- [class UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [class UITextLoupeSession](uitextloupesession.md)
  An object that manages the presentation of the system magnifier at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/adopting-system-selection-ui-in-custom-text-views)*