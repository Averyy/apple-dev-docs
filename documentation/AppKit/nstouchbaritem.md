# NSTouchBarItem

**Framework**: AppKit  
**Kind**: class

A UI control shown in the Touch Bar on supported models of MacBook Pro.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSTouchBarItem
```

#### Overview

An instance of the [`NSTouchBarItem`](nstouchbaritem.md) class is called an . It appears to the user on the Touch Bar, typically along with other items, within the (invisible) bounds of the view for an [`NSTouchBar`](nstouchbar.md) object, called a .

You use an item by adding it or its identifier to one or another of a bar’s arrays, depending on your app’s architecture and on the user customization you want to support. Because of the close interaction between bars and items, be sure you have read the overview for the [`NSTouchBar`](nstouchbar.md) class before continuing here to learn about items.

AppKit provides a rich set of subclasses of [`NSTouchBarItem`](nstouchbaritem.md), each of which is described in the corresponding class reference document:

- An [`NSCandidateListTouchBarItem`](nscandidatelisttouchbaritem.md) object (a ), along with its delegate, provides a list of textual suggestions for the current text view
- An [`NSColorPickerTouchBarItem`](nscolorpickertouchbaritem.md) object (a ) provides a system-defined color picker
- An [`NSCustomTouchBarItem`](nscustomtouchbaritem.md) object (a ) contains a responder of your choice, such as a view, a button, or a scrubber (an instance of the [`NSScrubber`](nsscrubber.md) class)
- An [`NSGroupTouchBarItem`](nsgrouptouchbaritem.md) object (a ) provides a bar to contain other items
- An [`NSPopoverTouchBarItem`](nspopovertouchbaritem.md) object (a ) provides a two-state control that, when touched or pressed, expands into its second state, showing the contents of a bar it owns
- An [`NSSharingServicePickerTouchBarItem`](nssharingservicepickertouchbaritem.md) object (a ), along with its delegate, provides a list of objects eligible for sharing
- An [`NSSliderTouchBarItem`](nsslidertouchbaritem.md) object (a ) provides a slider control for choosing a value in a range

The two most commonly-used item classes are [`NSCustomTouchBarItem`](nscustomtouchbaritem.md) and [`NSPopoverTouchBarItem`](nspopovertouchbaritem.md).

Refer to the following sample code projects which demonstrate how to use [`NSTouchBarItem`](nstouchbaritem.md) and related classes:

- [`Creating and Customizing the Touch Bar`](creating-and-customizing-the-touch-bar.md)
- [`Integrating a Toolbar and Touch Bar into Your App`](integrating-a-toolbar-and-touch-bar-into-your-app.md)

##### Custom Items

You typically use a  (an instance of the [`NSCustomTouchBarItem`](nscustomtouchbaritem.md) class) to hold a view. For example, to place a button in the Touch Bar, proceed as follows:

1. Use an [`NSButton`](nsbutton.md) convenience initializer such as [`init(title:image:target:action:)`](nsbutton/init(title:image:target:action:).md) to create and configure the button.
2. Set the [`view`](nstouchbaritem/view.md) property for a custom item to point to the new button.

> **Note**:  When you create custom items, it’s important to use convenience initializers, available starting in macOS 10.12, for the [`NSButton`](nsbutton.md), [`NSSegmentedControl`](nssegmentedcontrol.md), and [`NSSlider`](nsslider.md) classes. These initializers take care of sizing their controls correctly for the Touch Bar, and they configure appearance appropriately for the Touch Bar. If you don’t use the convenience initializers, it’s your app’s responsibility to ensure correct sizing and appearance.

##### Popover Items

A  (an instance of the [`NSPopoverTouchBarItem`](nspopovertouchbaritem.md) class) — the second commonly-used type — lets you provide a new bar (an [`NSTouchBar`](nstouchbar.md) object) when a user taps, or presses-and-holds, on the collapsed representation of the popover item.

In its expanded state, a popover appears as an overlay above other items in the Touch Bar.

To show a bar when a user taps a popover item, specify a bar in the item’s [`popoverTouchBar`](nspopovertouchbaritem/popovertouchbar.md) property. Enable press-and-hold by specifying a bar in the [`pressAndHoldTouchBar`](nspopovertouchbaritem/pressandholdtouchbar.md) property. The press-and-hold feature is suitable only for a simple popover, such as one that contains a single segmented control (an instance of the [`NSSegmentedControl`](nssegmentedcontrol.md) class) or slider (an instance of the [`NSSliderTouchBarItem`](nsslidertouchbaritem.md) class).

> **Note**:  If your popover bar requires significant user interaction and contains many items or many scroll views, don’t enable press-and-hold; doing so can result in an awkward user experience.

The system automatically shows a chevron in the popover item under the following conditions: You specify the same [`NSTouchBar`](nstouchbar.md) object for both [`pressAndHoldTouchBar`](nspopovertouchbaritem/pressandholdtouchbar.md) and [`popoverTouchBar`](nspopovertouchbaritem/popovertouchbar.md) properties,  you use the default view for the popover item’s [`collapsedRepresentation`](nspopovertouchbaritem/collapsedrepresentation.md) property.

If you provide a popover item that contains a scrubber (an [`NSScrubber`](nsscrubber.md) instance), you’ll likely want to dismiss both the scrubber and the popover after the user makes their selection in the scrubber. A good approach to achieve this user interaction is to subclass [`NSPopoverTouchBarItem`](nspopovertouchbaritem.md), employing your instance of the subclass as the scrubber’s delegate. You can then configure the delegate object, within its [`didFinishInteracting(with:)`](nsscrubberdelegate/didfinishinteracting(with:).md) method, to call the popover’s [`dismissPopover(_:)`](nspopovertouchbaritem/dismisspopover(_:).md) method.

If you place a segmented control in a bar for a popover item, take care  to use [`NSSegmentedControl.SwitchTracking.momentary`](nssegmentedcontrol/switchtracking/momentary.md) option of the [`NSSegmentedControl.SwitchTracking`](nssegmentedcontrol/switchtracking.md) enumeration because doing so interferes with the user’s operation of the control.

##### Other Common Item Types

To provide a , always use the [`NSSliderTouchBarItem`](nsslidertouchbaritem.md) class, which employs a standard slider but is optimized for user interaction with the Touch Bar. (That is, don’t instead add an [`NSSlider`](nsslider.md) object directly to a custom item.)

A  (an instance of the [`NSGroupTouchBarItem`](nsgrouptouchbaritem.md) class) is a container that provides a bar, in its [`groupTouchBar`](nsgrouptouchbaritem/grouptouchbar.md) property, with its own array of items. You can enable customization for the items in a group’s contained bar, in the same way you would for items directly within a top-level bar. Using a group item lets you provide different user customization rules for different parts of the Touch Bar. Using a group item also lets you enable centering of the group within the Touch Bar.

A  lets you add custom spacing between items in a bar. Specify a spacing item for a bar by assigning the [`fixedSpaceSmall`](nstouchbaritem/identifier-swift.struct/fixedspacesmall.md), [`fixedSpaceLarge`](nstouchbaritem/identifier-swift.struct/fixedspacelarge.md), or [`flexibleSpace`](nstouchbaritem/identifier-swift.struct/flexiblespace.md) identifier to an item, and adding that item to the bar’s items array. The system automatically instantiates and configures spacing items based on the identifiers you specify.

##### Configuration

You must configure each item with a unique identifier, and can optionally assign a visibility priority or tag it as a principal item.

 You must provide a unique identifier for each item in the bar, apart from spacing items. Specify an identifier, of type [`NSTouchBarItem.Identifier`](nstouchbaritem/identifier-swift.struct.md) (called an ), for each item when you initialize it. The item identifier serves as a persistable weak reference to the item. The system uses item identifiers to populate bars and to track and record changes for user customization.

 If the system is showing a bar in the Touch Bar, but horizontal space is constrained and the bar defines more items than will fit, the system hides some of the items. You influence this hide/show behavior by setting a value for the [`visibilityPriority`](nstouchbaritem/visibilitypriority.md) property of each item.

Lower-visibility-priority items get hidden by the system, as needed, before higher-visibility-priority items do.

To set visibility priority, use the constants in the [`NSTouchBarItem.Priority`](nstouchbaritem/priority.md) enumeration, or assign an integer value. The value `0` indicates [`normal`](nstouchbaritem/priority/normal.md) visibility priority. Visibility priority increases with increasing numerical value. The [`low`](nstouchbaritem/priority/low.md) constant provides a value of `-1000`; the [`high`](nstouchbaritem/priority/high.md) constant, a value `+1000`. You can use integers outside of this range if you need to.

The system hides or shows groups of identical-priority items (defined within a single bar) together. The one exception to this rule is for items whose visibility priority is [`normal`](nstouchbaritem/priority/normal.md); these items get hidden one-by-one, with the normal-priority item farthest to the right getting hidden first. If horizontal space later increases in the Touch Bar, and hidden, normal-priority items become eligible for display, the system first shows the most recently-hidden of those items.

 Within a bar, you can optionally specify an item as having special significance by employing the [`principalItemIdentifier`](nstouchbar/principalitemidentifier.md) property. The system attempts to center a principal item within the Touch Bar. If you want a group of items to appear centered in the Touch Bar, designate the group item (of type [`NSTouchBarItem`](nstouchbaritem.md)) as the principal item.

If more than one bar in the responder chain is eligible to be visible in the Touch Bar, and more than one of those has a principal item, the system determines which one to center in the Touch Bar.

###### Fonts Images and Colors

When using a button in a custom item, don’t attempt to set the button title’s font. In the Touch Bar, the system specifies fonts for standard controls.

If you need to specify a font, such as for custom drawing, use the [`systemFont(ofSize:)`](nsfont/systemfont(ofsize:).md) class method (or related methods) of the [`NSFont`](nsfont.md) class. Use a font size of `0` to automatically obtain appropriate sizing for the Touch Bar.

If you use an image in a button or other control in the Touch Bar, take care to employ a template image. Template images in the Touch Bar respond automatically to system white-point changes, and automatically react to user interactions. The overview in this document lists the built-in Touch Bar template images.

To use your own image assets, use Retina-resolution images, designated as `@2x` in your asset catalog and with a maximum height of 30 points (corresponding to 60 pixels).

To set colors on objects within an [`NSTouchBarItem`](nstouchbaritem.md) object, use AppKit named colors and use a bezel color property (available starting in macOS 10.12.1). Named colors appear correctly in the Touch Bar, support appearance vibrancy, and respond to system white-point changes. In a button or a segmented control, employ the bezel color property to ensure appropriate appearance in the Touch Bar.

To set the background color on a button within a custom item, use code like this:

```swift
myButton.bezelColor = NSColor.controlColor 
```

To set color on text and glyphs in the Touch Bar, use the following colors from the [`NSColor`](nscolor.md) class:

- [`labelColor`](nscolor/labelcolor.md)
- [`secondaryLabelColor`](nscolor/secondarylabelcolor.md)
- [`tertiaryLabelColor`](nscolor/tertiarylabelcolor.md)
- [`quaternaryLabelColor`](nscolor/quaternarylabelcolor.md)

The system automatically changes the relative brightness and the white-point of these colors, depending on the ambient light, and depending on other factors such as keyboard backlight level. Always use these colors, or colors that dynamically derive from these colors, for control backgrounds, text, icons, and glyphs in the Touch Bar.

###### Handling Touch Events

The easiest way to handle touch events in an item is to use AppKit controls, such as by adding a button, a segmented control, or a scrubber to the item. Standard AppKit controls convey touch events to your specified targets automatically, so use standard controls whenever possible in your app.

If standard controls are insufficient, you can create composite views with a combination of standard controls, custom views, and gesture recognizers that you manually add to those custom views.

If you require the lowest-level of control for touch event processing, you can use the [`NSTouch`](nstouch.md) class directly. You might go this route, for example, to provide good user feedback in the case of a control placed within a scroll view.Direct use of touch methods allows fine-grained control over interaction. You can, for example, highlight a control immediately upon a user touching it, and then remove the highlight if the user then, without lifting the finger, performs a scroll gesture.

If using the [`NSTouch`](nstouch.md) class directly, be sure to implement the [`touchesCancelled(with:)`](nsgesturerecognizer/touchescancelled(with:).md) responder method, because users can perform touch interactions that result in canceled touches.

## Topics

### Creating a bar item
- [init(identifier: NSTouchBarItem.Identifier)](nstouchbaritem/init(identifier:).md)
  Creates a new item with the specified identifier.
- [NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct.md)
  An identifier for an item in the Touch Bar.
- [init?(coder: NSCoder)](nstouchbaritem/init(coder:).md)
  Initializes and returns a new item from a storyboard or nib file.
### Identifying a bar item
- [var identifier: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.property.md)
  The identifier for this item.
- [NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct.md)
  An identifier for an item in the Touch Bar.
### Managing item visibility
- [var visibilityPriority: NSTouchBarItem.Priority](nstouchbaritem/visibilitypriority.md)
  Determines which items are shown in a bar when space is limited.
- [NSTouchBarItem.Priority](nstouchbaritem/priority.md)
  Priorities for the visibility of a Touch Bar item.
- [var isVisible: Bool](nstouchbaritem/isvisible.md)
  A Boolean value that reflects whether or not the item is visible.
### Configuring bar customization
- [var customizationLabel: String](nstouchbaritem/customizationlabel.md)
  The user-visible string identifying this item during bar customization.
### Subclassing bar items
- [var viewController: NSViewController?](nstouchbaritem/viewcontroller.md)
  The view controller associated with this item.
- [var view: NSView?](nstouchbaritem/view.md)
  The view associated with this item.
### Using template images
- [class let touchBarAddDetailTemplateName: String](nsimage/touchbaradddetailtemplatename.md)
  A template image for showing additional detail for an item.
- [class let touchBarAddTemplateName: String](nsimage/touchbaraddtemplatename.md)
  A template image for creating a new item.
- [class let touchBarAlarmTemplateName: String](nsimage/touchbaralarmtemplatename.md)
  A template image for setting or showing an alarm.
- [class let touchBarAudioInputMuteTemplateName: String](nsimage/touchbaraudioinputmutetemplatename.md)
  A template image for muting audio input or denoting that audio input is muted.
- [class let touchBarAudioInputTemplateName: String](nsimage/touchbaraudioinputtemplatename.md)
  A template image for denoting audio input.
- [class let touchBarAudioOutputMuteTemplateName: String](nsimage/touchbaraudiooutputmutetemplatename.md)
  A template image for muting audio output or for denoting that audio output is muted.
- [class let touchBarAudioOutputVolumeHighTemplateName: String](nsimage/touchbaraudiooutputvolumehightemplatename.md)
  A template image for setting the audio output volume to a high level, or for denoting that the audio is at the peak volume.
- [class let touchBarAudioOutputVolumeLowTemplateName: String](nsimage/touchbaraudiooutputvolumelowtemplatename.md)
  A template image for setting the audio output volume to a low level, or for denoting that it is set to a low level.
- [class let touchBarAudioOutputVolumeMediumTemplateName: String](nsimage/touchbaraudiooutputvolumemediumtemplatename.md)
  A template image for setting the audio output volume to a medium level, or for denoting that it is set to a medium level.
- [class let touchBarAudioOutputVolumeOffTemplateName: String](nsimage/touchbaraudiooutputvolumeofftemplatename.md)
  A template image for setting the audio output volume to silent, or for denoting that it is set to silent.
- [class let touchBarBookmarksTemplateName: String](nsimage/touchbarbookmarkstemplatename.md)
  A template image for showing app-specific bookmarks.
- [class let touchBarColorPickerFillName: String](nsimage/touchbarcolorpickerfillname.md)
  A template image for showing a color picker so the user can select a fill color.
- [class let touchBarColorPickerFontName: String](nsimage/touchbarcolorpickerfontname.md)
  A template image for showing a color picker so the user can select a text color.
- [class let touchBarColorPickerStrokeName: String](nsimage/touchbarcolorpickerstrokename.md)
  A template image for showing a color picker so the user can select a stroke color.
- [class let touchBarCommunicationAudioTemplateName: String](nsimage/touchbarcommunicationaudiotemplatename.md)
  A template image for initiating or denoting audio communication.
- [class let touchBarCommunicationVideoTemplateName: String](nsimage/touchbarcommunicationvideotemplatename.md)
  A template image for initiating or denoting video communication.
- [class let touchBarComposeTemplateName: String](nsimage/touchbarcomposetemplatename.md)
  A template image for opening a new document or view in edit mode.
- [class let touchBarDeleteTemplateName: String](nsimage/touchbardeletetemplatename.md)
  A template image for deleting the current or selected item.
- [class let touchBarDownloadTemplateName: String](nsimage/touchbardownloadtemplatename.md)
  A template image for downloading an item.
- [class let touchBarEnterFullScreenTemplateName: String](nsimage/touchbarenterfullscreentemplatename.md)
  A template image for entering full screen mode.
- [class let touchBarExitFullScreenTemplateName: String](nsimage/touchbarexitfullscreentemplatename.md)
  A template image for exiting full screen mode.
- [class let touchBarFastForwardTemplateName: String](nsimage/touchbarfastforwardtemplatename.md)
  A template image for moving forward through media playback or slides.
- [class let touchBarFolderTemplateName: String](nsimage/touchbarfoldertemplatename.md)
  A template image for opening or representing a folder.
- [class let touchBarFolderCopyToTemplateName: String](nsimage/touchbarfoldercopytotemplatename.md)
  A template image for copying an item to a destination.
- [class let touchBarFolderMoveToTemplateName: String](nsimage/touchbarfoldermovetotemplatename.md)
  A template image for moving an item to a destination.
- [class let touchBarGetInfoTemplateName: String](nsimage/touchbargetinfotemplatename.md)
  A template image for showing information about an item.
- [class let touchBarGoBackTemplateName: String](nsimage/touchbargobacktemplatename.md)
  A template image for returning to the previous screen or location.
- [class let touchBarGoDownTemplateName: String](nsimage/touchbargodowntemplatename.md)
  A template image for moving to the next item in a list.
- [class let touchBarGoForwardTemplateName: String](nsimage/touchbargoforwardtemplatename.md)
  A template image for moving to the next screen or location.
- [class let touchBarGoUpTemplateName: String](nsimage/touchbargouptemplatename.md)
  A template image for moving to the previous item in a list.
- [class let touchBarHistoryTemplateName: String](nsimage/touchbarhistorytemplatename.md)
  A template image for showing history information, such as recent downloads.
- [class let touchBarIconViewTemplateName: String](nsimage/touchbariconviewtemplatename.md)
  A template image for showing items in an icon view.
- [class let touchBarListViewTemplateName: String](nsimage/touchbarlistviewtemplatename.md)
  A template image for showing items in a list view.
- [class let touchBarMailTemplateName: String](nsimage/touchbarmailtemplatename.md)
  A template image for creating an email message.
- [class let touchBarNewFolderTemplateName: String](nsimage/touchbarnewfoldertemplatename.md)
  A template image for creating a new folder.
- [class let touchBarNewMessageTemplateName: String](nsimage/touchbarnewmessagetemplatename.md)
  A template image for creating a new message, or for denoting the use of messaging.
- [class let touchBarOpenInBrowserTemplateName: String](nsimage/touchbaropeninbrowsertemplatename.md)
  A template image for opening an item in the user’s browser.
- [class let touchBarPauseTemplateName: String](nsimage/touchbarpausetemplatename.md)
  A template image for pausing media playback or slides.
- [class let touchBarPlayTemplateName: String](nsimage/touchbarplaytemplatename.md)
  A template image for starting or resuming playback of media or slides.
- [class let touchBarPlayPauseTemplateName: String](nsimage/touchbarplaypausetemplatename.md)
  A template image for toggling between playing and pausing media or slides.
- [class let touchBarPlayheadTemplateName: String](nsimage/touchbarplayheadtemplatename.md)
  A template image for denoting the current playback position within a timeline track.
- [class let touchBarQuickLookTemplateName: String](nsimage/touchbarquicklooktemplatename.md)
  A template image for opening an item in Quick Look.
- [class let touchBarRecordStartTemplateName: String](nsimage/touchbarrecordstarttemplatename.md)
  A template image for starting recording.
- [class let touchBarRecordStopTemplateName: String](nsimage/touchbarrecordstoptemplatename.md)
  A template image for stopping recording or stopping playback of media or slides.
- [class let touchBarRefreshTemplateName: String](nsimage/touchbarrefreshtemplatename.md)
  A template image for refreshing displayed data.
- [class let touchBarRewindTemplateName: String](nsimage/touchbarrewindtemplatename.md)
  A template image for moving backwards through media or slides.
- [class let touchBarRotateLeftTemplateName: String](nsimage/touchbarrotatelefttemplatename.md)
  A template image for rotating an item counterclockwise.
- [class let touchBarRotateRightTemplateName: String](nsimage/touchbarrotaterighttemplatename.md)
  A template image for rotating an item clockwise.
- [class let touchBarSearchTemplateName: String](nsimage/touchbarsearchtemplatename.md)
  A template image for showing a search field or for initiating a search.
- [class let touchBarShareTemplateName: String](nsimage/touchbarsharetemplatename.md)
  A template image for sharing content with others directly or via social media.
- [class let touchBarSidebarTemplateName: String](nsimage/touchbarsidebartemplatename.md)
  A template image for showing a sidebar in the current view.
- [class let touchBarSkipBackTemplateName: String](nsimage/touchbarskipbacktemplatename.md)
  A template image for skipping to the previous chapter or location during media playback.
- [class let touchBarSkipToStartTemplateName: String](nsimage/touchbarskiptostarttemplatename.md)
  A template image for skipping to the start of media playback.
- [class let touchBarSkipBack30SecondsTemplateName: String](nsimage/touchbarskipback30secondstemplatename.md)
  A template image for skipping back 30 seconds during media playback.
- [class let touchBarSkipBack15SecondsTemplateName: String](nsimage/touchbarskipback15secondstemplatename.md)
  A template image for skipping back 15 seconds during media playback.
- [class let touchBarSkipAhead15SecondsTemplateName: String](nsimage/touchbarskipahead15secondstemplatename.md)
  A template image for skipping ahead 15 seconds during media playback.
- [class let touchBarSkipAhead30SecondsTemplateName: String](nsimage/touchbarskipahead30secondstemplatename.md)
  A template image for skipping ahead 30 seconds during media playback.
- [class let touchBarSkipToEndTemplateName: String](nsimage/touchbarskiptoendtemplatename.md)
  A template image for skipping to the end of media playback.
- [class let touchBarSkipAheadTemplateName: String](nsimage/touchbarskipaheadtemplatename.md)
  A template image for skipping to the next chapter or location during media playback.
- [class let touchBarSlideshowTemplateName: String](nsimage/touchbarslideshowtemplatename.md)
  A template image for starting a slideshow.
- [class let touchBarTagIconTemplateName: String](nsimage/touchbartagicontemplatename.md)
  A template image for applying a tag to an item.
- [class let touchBarTextBoxTemplateName: String](nsimage/touchbartextboxtemplatename.md)
  A template image for inserting a text box.
- [class let touchBarTextListTemplateName: String](nsimage/touchbartextlisttemplatename.md)
  A template image for inserting a list or converting text to list form.
- [class let touchBarTextBoldTemplateName: String](nsimage/touchbartextboldtemplatename.md)
  A template image for making selected text bold.
- [class let touchBarTextItalicTemplateName: String](nsimage/touchbartextitalictemplatename.md)
  A template image for italicizing the selected text.
- [class let touchBarTextUnderlineTemplateName: String](nsimage/touchbartextunderlinetemplatename.md)
  A template image for underlining text.
- [class let touchBarTextStrikethroughTemplateName: String](nsimage/touchbartextstrikethroughtemplatename.md)
  A template image for striking through text.
- [class let touchBarTextJustifiedAlignTemplateName: String](nsimage/touchbartextjustifiedaligntemplatename.md)
  A template image for fully justifying text.
- [class let touchBarTextLeftAlignTemplateName: String](nsimage/touchbartextleftaligntemplatename.md)
  A template image for aligning text to the left.
- [class let touchBarTextCenterAlignTemplateName: String](nsimage/touchbartextcenteraligntemplatename.md)
  A template image for centering text.
- [class let touchBarTextRightAlignTemplateName: String](nsimage/touchbartextrightaligntemplatename.md)
  A template image for aligning text to the right.
- [class let touchBarUserTemplateName: String](nsimage/touchbarusertemplatename.md)
  A template image for showing or representing user information.
- [class let touchBarUserAddTemplateName: String](nsimage/touchbaruseraddtemplatename.md)
  A template image for creating a new user account.
- [class let touchBarUserGroupTemplateName: String](nsimage/touchbarusergrouptemplatename.md)
  A template image for showing or representing a group of users.
- [class let touchBarVolumeUpTemplateName: String](nsimage/touchbarvolumeuptemplatename.md)
  A template image for increasing the audio output volume.
- [class let touchBarVolumeDownTemplateName: String](nsimage/touchbarvolumedowntemplatename.md)
  A template image for reducing the audio output volume.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSButtonTouchBarItem](nsbuttontouchbaritem.md)
- [NSCandidateListTouchBarItem](nscandidatelisttouchbaritem.md)
- [NSColorPickerTouchBarItem](nscolorpickertouchbaritem.md)
- [NSCustomTouchBarItem](nscustomtouchbaritem.md)
- [NSGroupTouchBarItem](nsgrouptouchbaritem.md)
- [NSPickerTouchBarItem](nspickertouchbaritem.md)
- [NSPopoverTouchBarItem](nspopovertouchbaritem.md)
- [NSSharingServicePickerTouchBarItem](nssharingservicepickertouchbaritem.md)
- [NSSliderTouchBarItem](nsslidertouchbaritem.md)
- [NSStepperTouchBarItem](nssteppertouchbaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSCandidateListTouchBarItem](nscandidatelisttouchbaritem.md)
  A bar item that, along with its delegate, provides a list of textual suggestions for the current text view.
- [class NSColorPickerTouchBarItem](nscolorpickertouchbaritem.md)
  A bar item that provides a system-defined color picker.
- [class NSCustomTouchBarItem](nscustomtouchbaritem.md)
  A bar item that contains a responder of your choice, such as a view, a button, or a scrubber.
- [class NSGroupTouchBarItem](nsgrouptouchbaritem.md)
  A bar item that provides a bar to contain other items.
- [class NSPopoverTouchBarItem](nspopovertouchbaritem.md)
  A bar item that provides a two-state control that can expand into its second state, showing the contents of a bar that it owns.
- [class NSSharingServicePickerTouchBarItem](nssharingservicepickertouchbaritem.md)
  A bar item that, along with its delegate, provides a list of objects eligible for sharing.
- [class NSSliderTouchBarItem](nsslidertouchbaritem.md)
  A bar item that provides a slider control for choosing a value in a range.
- [class NSStepperTouchBarItem](nssteppertouchbaritem.md)
  A bar item that provides a stepper control for incrementing or decrementing a value.
- [class NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions.md)
  An object that specifies how user interface elements resize themselves when space is constrained.
- [class NSButtonTouchBarItem](nsbuttontouchbaritem.md)
  A bar item that provides a button.
- [class NSPickerTouchBarItem](nspickertouchbaritem.md)
  A bar item that provides a picker control with multiple options.
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem)*