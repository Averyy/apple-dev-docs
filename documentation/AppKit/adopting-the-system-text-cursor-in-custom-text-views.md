# Adopting the system text cursor in custom text views

**Framework**: Appkit

Incorporate the system text cursor into your custom text UI in AppKit.

#### Overview

People can enter text into your app in a variety of ways, such as typing, copy and paste, or dictation. macOS 14 introduces enhancements to the system UI for the text cursor to provide a more seamless text experience.

If your app handles text input through standard AppKit views such as [`NSTextView`](nstextview.md) or [`NSTextField`](nstextfield.md), your app automatically uses the system UI for the text cursor. This system UI includes the following elements:

- The text cursor that indicates the insertion point of the text
- Text cursor accessories that indicate state, such as current input source language, dictation, and Caps Lock
- Animation effects that surround the text cursor during dictation

If you have a highly customized UI for displaying text, you can adopt this system UI in your AppKit app.

##### Add the System Text Cursor to a Custom Text View

If your app handles text input through a custom view that builds on [`NSTextInputClient`](nstextinputclient.md), you can display the system text cursor manually. Create an [`NSTextInsertionIndicator`](nstextinsertionindicator.md) view and add it on top of the view that displays text in your app.

```swift
// Set up the text cursor.
let textCursor = NSTextInsertionIndicator(frame: .zero)
documentView.addSubview(textCursor)
```

When your custom text view becomes active or becomes first responder, update the display mode of the text cursor.

```swift
// Show the text cursor when the text view becomes active.
func didBecomeActive() {
    textCursor.displayMode = .automatic
}
```

##### Configure the Text Cursor Animations

Depending on the behavior you need at a particular point in time, you can determine how the text cursor handles animations by selecting one of these display modes:

- Automatic. Set the [`NSTextInsertionIndicator.DisplayMode.automatic`](nstextinsertionindicator/displaymode-swift.enum/automatic.md) display mode to stop and start animations for the text cursor automatically. These animations include a blinking effect that applies to the text cursor during typing and dictation, animated transitions between dictation states, and automatic hiding of the text cursor during tracking loops. This display mode is appropriate in the majority of cases when your custom text view is accepting text input.
- Always visible. Set the [`NSTextInsertionIndicator.DisplayMode.visible`](nstextinsertionindicator/displaymode-swift.enum/visible.md) display mode to always show the text cursor and disable animations. This display mode is appropriate when the text cursor needs to appear without blinking — for example, to indicate a drop destination as part of a drag and drop interaction.

When you use the automatic display mode, you can further customize the animation options depending on the needs of your app.

- By default, the text cursor hides automatically during tracking loops. Include the [`showWhileTracking`](nstextinsertionindicator/automaticmodeoptions-swift.struct/showwhiletracking.md) option in [`automaticModeOptions`](nstextinsertionindicator/automaticmodeoptions-swift.property.md) to show the text cursor during tracking instead.
- By default, the text cursor shows an animated effect during dictation. To completely hide the view that draws the animated effect, remove [`showEffectsView`](nstextinsertionindicator/automaticmodeoptions-swift.struct/showeffectsview.md) from [`automaticModeOptions`](nstextinsertionindicator/automaticmodeoptions-swift.property.md). To customize the placement of this view in your view hierarchy, specify [`effectsViewInserter`](nstextinsertionindicator/effectsviewinserter.md).

The following code shows how to customize the placement of the animated effects view to place it directly below the text cursor.

```swift
// Specify custom view hierarchy placement for the animated effects view.
textCursor.effectsViewInserter = { view in
    documentView.addSubview(view, positioned: .below, relativeTo: textCursor)
}
```

##### Update the Text Cursor Position

Your custom text view is responsible for updating the position of the text cursor when a person inputs text, but the system provides the appropriate animated effect. For example, the following image shows the system animation effect that applies to the text cursor during dictation.

![Screenshot of text that says “The quick brown fox jumps over the” with the text cursor at the end of the text. The text cursor shows a blue glowing effect that trails through the text behind it, gradually dimming in opacity as it reaches the word “over.”](https://docs-assets.developer.apple.com/published/9e3cf9b424c226b3116f31f758c76a8d/media-4213258%402x.png)

As a person types or inserts text during dictation, update the [`frame`](nsview/frame.md) of the [`NSTextInsertionIndicator`](nstextinsertionindicator.md) view. The view automatically changes its appearance in response to that movement, matching the system UI for the corresponding type of input (typing or dictation).

##### Configure the Placements of Text Cursor Accessories

The system text cursor displays accessories that indicate state, such as current input source language, dictation, and Caps Lock. For example, the following image shows the text cursor with the dictation indicator and the current input language set to English.

![Screenshot of text that says “The quick brown fox jumps over the” with the text cursor at the end of the text. The text cursor shows a dictation indicator accessory and a language indicator accessory that reads EN to represent the English language.](https://docs-assets.developer.apple.com/published/cb559fac35d45dd0f5304fa3db3cdf2e/media-4277103%402x.png)

When a person changes the input language, the accessory expands to show the language selection UI in the language switcher accessory.

![Screenshot of the text cursor in a text input field. The text cursor shows the language switcher accessory with three possible input languages: English, Russian, Arabic, and Japanese.](https://docs-assets.developer.apple.com/published/ffaaab086b99f0c1cc7f2c001045e760/media-4277104%402x.png)

[`NSTextInsertionIndicator`](nstextinsertionindicator.md) draws these accessories automatically, but you can specify where in relation to the text cursor to draw them. In your custom text view, you can override the placement of these accessories by specifying [`preferredTextAccessoryPlacement()`](nstextinputclient/preferredtextaccessoryplacement().md) in your implementation of [`NSTextInputClient`](nstextinputclient.md). When the system renders the text cursor in your custom view, it uses the return value of this method to determine where to draw the accessories.

##### Indicate the Offscreen Text Cursor Position During Dictation

The system text cursor shows a dictation indicator accessory during an active dictation session. When a person scrolls the text cursor offscreen during dictation, the system also draws a scroll-away indicator to indicate the position of the cursor. For example, the following image shows a scroll-away indicator that points downwards, indicating that the text cursor is out of view below.

![Screenshot of text in a text input field with an active dictation session. A scroll-away indicator points downwards, indicating that the text cursor is out of view below.](https://docs-assets.developer.apple.com/published/a115c25ef1f35d3210de878287a3418b/media-4277102%402x.png)

For the system to show the scroll-away indicator on a custom text view, you need to complete the following steps:

- Adopt [`NSTextInputClient`](nstextinputclient.md) and implement [`unionRectInVisibleSelectedRange`](nstextinputclient/unionrectinvisibleselectedrange.md) and [`documentVisibleRect`](nstextinputclient/documentvisiblerect.md). These properties provide the system with the coordinate information it needs to draw the scroll-away indicator in the appropriate position.
- Notify the system when a person starts or stops scrolling, so the system can display the indicator at the appropriate time. Call [`textInputClientWillStartScrollingOrZooming()`](nstextinputcontext/textinputclientwillstartscrollingorzooming().md) when scrolling starts, and [`textInputClientDidEndScrollingOrZooming()`](nstextinputcontext/textinputclientdidendscrollingorzooming().md) when scrolling ends.

##### Hide the System Text Cursor

When your custom text view resigns first responder status, update the display mode of the text cursor to [`NSTextInsertionIndicator.DisplayMode.hidden`](nstextinsertionindicator/displaymode-swift.enum/hidden.md).

```swift
// Hide the text cursor when the text view becomes inactive.
func didBecomeInactive() {
    textCursor.displayMode = .hidden
}
```

If you implement custom text UI in a UIKit app, see [`Adopting system selection UI in custom text views`](https://developer.apple.com/documentation/UIKit/adopting-system-selection-ui-in-custom-text-views).

> **Note**:  Session 10058: [`What’s new with text and text interactions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10058/)

## See Also

- [class NSTextInputContext](nstextinputcontext.md)
  An object that represents the Cocoa text input system.
- [protocol NSTextInputClient](nstextinputclient.md)
  A set of methods that text views need to implement to interact properly with the text input management system.
- [class NSTextAlternatives](nstextalternatives.md)
  A list of alternative strings for a piece of text.
- [protocol NSTextContent](nstextcontent.md)
  A protocol that describes specific kinds of input content types.
- [class NSTextInsertionIndicator](nstextinsertionindicator.md)
  A view that represents the insertion indicator in text.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.
- [NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/adopting-the-system-text-cursor-in-custom-text-views)*