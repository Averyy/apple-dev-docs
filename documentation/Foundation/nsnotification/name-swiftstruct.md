# NSNotification.Name

**Framework**: Foundation  
**Kind**: struct

A structure that defines the name of a notification.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Name
```

## Topics

### AddressBook
- [static let abDatabaseChanged: NSNotification.Name](nsnotification/name-swift.struct/abdatabasechanged.md)
  Posted when this process has changed the Address Book database.
- [static let abDatabaseChangedExternally: NSNotification.Name](nsnotification/name-swift.struct/abdatabasechangedexternally.md)
  Posted when a process other than the current one has changed the Address Book database.
- [static let ABPeoplePickerDisplayedPropertyDidChange: NSNotification.Name](nsnotification/name-swift.struct/abpeoplepickerdisplayedpropertydidchange.md)
  Posted when the displayed property in the record list is changed.
- [static let ABPeoplePickerGroupSelectionDidChange: NSNotification.Name](nsnotification/name-swift.struct/abpeoplepickergroupselectiondidchange.md)
  Posted when the selection in the group list is changed.
- [static let ABPeoplePickerNameSelectionDidChange: NSNotification.Name](nsnotification/name-swift.struct/abpeoplepickernameselectiondidchange.md)
  Posted when the selection in the name list is changed.
- [static let ABPeoplePickerValueSelectionDidChange: NSNotification.Name](nsnotification/name-swift.struct/abpeoplepickervalueselectiondidchange.md)
  Posted when the selection in a multivalue property is changed.
### AppKit
- [static let unsupportedAttributeAddedNotification: NSNotification.Name](nsnotification/name-swift.struct/unsupportedattributeaddednotification.md)
- [class let didProcessEditingNotification: NSNotification.Name](../appkit/nstextstorage/didprocesseditingnotification.md)
  A notification that posts after a text storage finishes processing edits.
- [class let willProcessEditingNotification: NSNotification.Name](../appkit/nstextstorage/willprocesseditingnotification.md)
  A notification that posts before a text storage begins processing edits.
- [class let didChangeSelectionNotification: NSNotification.Name](../appkit/nstextview/didchangeselectionnotification.md)
  Posted when the selected range of characters changes.
- [class let didChangeTypingAttributesNotification: NSNotification.Name](../appkit/nstextview/didchangetypingattributesnotification.md)
  Posted when there is a change in the typing attributes within a text view.
- [class let willChangeNotifyingTextViewNotification: NSNotification.Name](../appkit/nstextview/willchangenotifyingtextviewnotification.md)
  Posted when a new text view is established as the text view that sends notifications.
- [class let didRemoveItemNotification: NSNotification.Name](../appkit/nstoolbar/didremoveitemnotification.md)
  Posted after an item is removed from a toolbar.
- [class let willAddItemNotification: NSNotification.Name](../appkit/nstoolbar/willadditemnotification.md)
  Posts before the toolbar adds a new item.
- [class let boundsDidChangeNotification: NSNotification.Name](../appkit/nsview/boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](../appkit/nsview/didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.
- [class let frameDidChangeNotification: NSNotification.Name](../appkit/nsview/framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [class let didBecomeKeyNotification: NSNotification.Name](../appkit/nswindow/didbecomekeynotification.md)
  A notification that the window object became the key window.
- [class let didBecomeMainNotification: NSNotification.Name](../appkit/nswindow/didbecomemainnotification.md)
  A notification that the window object became the main window.
- [class let didChangeBackingPropertiesNotification: NSNotification.Name](../appkit/nswindow/didchangebackingpropertiesnotification.md)
  A notification that the window object backing properties changed.
- [class let didChangeOcclusionStateNotification: NSNotification.Name](../appkit/nswindow/didchangeocclusionstatenotification.md)
  A notification that the window object’s occlusion state changed.
- [class let didChangeScreenNotification: NSNotification.Name](../appkit/nswindow/didchangescreennotification.md)
  A notification that a portion of the window object’s frame moved onto or off of a screen.
- [class let didChangeScreenProfileNotification: NSNotification.Name](../appkit/nswindow/didchangescreenprofilenotification.md)
  A notification that the screen containing the window changed.
- [class let didDeminiaturizeNotification: NSNotification.Name](../appkit/nswindow/diddeminiaturizenotification.md)
  A notification that the window is no longer minimized.
- [class let didEndLiveResizeNotification: NSNotification.Name](../appkit/nswindow/didendliveresizenotification.md)
  A notification that the user resized the window object.
- [class let didEndSheetNotification: NSNotification.Name](../appkit/nswindow/didendsheetnotification.md)
  A notification that the window object closed an attached sheet.
- [class let didEnterFullScreenNotification: NSNotification.Name](../appkit/nswindow/didenterfullscreennotification.md)
  A notification that the window entered full-screen mode.
- [class let didEnterVersionBrowserNotification: NSNotification.Name](../appkit/nswindow/didenterversionbrowsernotification.md)
  A notification that the window object entered version browser mode.
- [class let didExitFullScreenNotification: NSNotification.Name](../appkit/nswindow/didexitfullscreennotification.md)
  A notification that the window object exited full-screen mode.
- [class let didExitVersionBrowserNotification: NSNotification.Name](../appkit/nswindow/didexitversionbrowsernotification.md)
  A notification that the window object exited version browser mode.
- [class let didExposeNotification: NSNotification.Name](../appkit/nswindow/didexposenotification.md)
  A notification that a window exposed a portion of its nonretained content.
- [class let didMiniaturizeNotification: NSNotification.Name](../appkit/nswindow/didminiaturizenotification.md)
  A notification that the window object minimized.
- [class let didMoveNotification: NSNotification.Name](../appkit/nswindow/didmovenotification.md)
  A notification that the window object moved.
- [class let didResignKeyNotification: NSNotification.Name](../appkit/nswindow/didresignkeynotification.md)
  A notification that the window object resigned its status as key window.
- [class let didResignMainNotification: NSNotification.Name](../appkit/nswindow/didresignmainnotification.md)
  A notification that the window object resigned its status as main window.
- [class let didResizeNotification: NSNotification.Name](../appkit/nswindow/didresizenotification.md)
  A notification that the window object size changed.
- [class let didUpdateNotification: NSNotification.Name](../appkit/nswindow/didupdatenotification.md)
  A notification that the window object received an update message.
- [class let willBeginSheetNotification: NSNotification.Name](../appkit/nswindow/willbeginsheetnotification.md)
  A notification that the window object is about to open a sheet.
- [class let willCloseNotification: NSNotification.Name](../appkit/nswindow/willclosenotification.md)
  A notification that the window object is about to close.
- [class let willEnterFullScreenNotification: NSNotification.Name](../appkit/nswindow/willenterfullscreennotification.md)
  A notification that the window will enter full-screen mode.
- [class let willEnterVersionBrowserNotification: NSNotification.Name](../appkit/nswindow/willenterversionbrowsernotification.md)
  A notification that the window object will enter version browser mode.
- [class let willExitFullScreenNotification: NSNotification.Name](../appkit/nswindow/willexitfullscreennotification.md)
  A notification that the window object will exit full-screen mode.
- [class let willExitVersionBrowserNotification: NSNotification.Name](../appkit/nswindow/willexitversionbrowsernotification.md)
  A notification that the window object will exit version browser mode.
- [class let willMiniaturizeNotification: NSNotification.Name](../appkit/nswindow/willminiaturizenotification.md)
  A notification that the window object is about to minimize.
- [class let willMoveNotification: NSNotification.Name](../appkit/nswindow/willmovenotification.md)
  A notification that the window object is about to move.
- [class let willStartLiveResizeNotification: NSNotification.Name](../appkit/nswindow/willstartliveresizenotification.md)
  A notification that the user is about to resize the window.
- [class let accessibilityDisplayOptionsDidChangeNotification: NSNotification.Name](../appkit/nsworkspace/accessibilitydisplayoptionsdidchangenotification.md)
  A notification that the workspace posts when any of the accessibility display options change.
- [class let activeSpaceDidChangeNotification: NSNotification.Name](../appkit/nsworkspace/activespacedidchangenotification.md)
  A notification that the workspace posts when a Spaces change occurs.
- [class let didActivateApplicationNotification: NSNotification.Name](../appkit/nsworkspace/didactivateapplicationnotification.md)
  A notification that the workspace posts when the Finder is about to activate an app.
- [class let didChangeFileLabelsNotification: NSNotification.Name](../appkit/nsworkspace/didchangefilelabelsnotification.md)
  A notification that the workspace posts when the Finder file labels or colors change.
- [class let didDeactivateApplicationNotification: NSNotification.Name](../appkit/nsworkspace/diddeactivateapplicationnotification.md)
  A notification that the workspace posts when the Finder deactivates an app.
- [class let didHideApplicationNotification: NSNotification.Name](../appkit/nsworkspace/didhideapplicationnotification.md)
  A notification that the workspace posts when the Finder hides an app.
- [class let didLaunchApplicationNotification: NSNotification.Name](../appkit/nsworkspace/didlaunchapplicationnotification.md)
  A notification that the workspace posts when a new app starts up.
- [class let didMountNotification: NSNotification.Name](../appkit/nsworkspace/didmountnotification.md)
  A notification that the workspace posts when a new device mounts.
- [class let didPerformFileOperationNotification: NSNotification.Name](../appkit/nsworkspace/didperformfileoperationnotification.md)
  Posted when a file operation has been performed in the receiving app.
- [class let didRenameVolumeNotification: NSNotification.Name](../appkit/nsworkspace/didrenamevolumenotification.md)
  A notification that the workspace posts when a volume changes its name or mount path.
- [class let didTerminateApplicationNotification: NSNotification.Name](../appkit/nsworkspace/didterminateapplicationnotification.md)
  A notification that the workspace posts when an app finishes executing.
- [class let didUnhideApplicationNotification: NSNotification.Name](../appkit/nsworkspace/didunhideapplicationnotification.md)
  A notification that the workspace posts when the Finder unhides an app.
- [class let didUnmountNotification: NSNotification.Name](../appkit/nsworkspace/didunmountnotification.md)
  A notification that the workspace posts when the Finder unmounts a device.
- [class let didWakeNotification: NSNotification.Name](../appkit/nsworkspace/didwakenotification.md)
  A notification that the workspace posts when the device wakes from sleep.
- [class let screensDidSleepNotification: NSNotification.Name](../appkit/nsworkspace/screensdidsleepnotification.md)
  A notification that the workspace posts when the device’s screen goes to sleep.
- [class let screensDidWakeNotification: NSNotification.Name](../appkit/nsworkspace/screensdidwakenotification.md)
  A notification that the workspace posts when the device’s screens wake.
- [class let sessionDidBecomeActiveNotification: NSNotification.Name](../appkit/nsworkspace/sessiondidbecomeactivenotification.md)
  A notification that the workspace posts after a user session switches in.
- [class let sessionDidResignActiveNotification: NSNotification.Name](../appkit/nsworkspace/sessiondidresignactivenotification.md)
  A notification that the workspace posts before a user session switches out.
- [class let willLaunchApplicationNotification: NSNotification.Name](../appkit/nsworkspace/willlaunchapplicationnotification.md)
  A notification that the workspace posts when the Finder is about to launch an app.
- [class let willPowerOffNotification: NSNotification.Name](../appkit/nsworkspace/willpoweroffnotification.md)
  A notification that the workspace posts when the user requests a logout or powers off the device.
- [class let willSleepNotification: NSNotification.Name](../appkit/nsworkspace/willsleepnotification.md)
  A notification that the workspace posts before the device goes to sleep.
- [class let willUnmountNotification: NSNotification.Name](../appkit/nsworkspace/willunmountnotification.md)
  A notification that the workspace posts when the Finder is about to unmount a device.
- [class let didChangeNotification: NSNotification.Name](../appkit/nscolorlist/didchangenotification.md)
  Posted whenever a color list changes.
- [class let didChangeNotification: NSNotification.Name](../appkit/nscolorlist/didchangenotification.md)
  Posted whenever a color list changes.
- [class let selectionDidChangeNotification: NSNotification.Name](../appkit/nscombobox/selectiondidchangenotification.md)
  Posted after the pop-up list selection of the `NSComboBox` changes.
- [class let selectionIsChangingNotification: NSNotification.Name](../appkit/nscombobox/selectionischangingnotification.md)
  Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [class let willDismissNotification: NSNotification.Name](../appkit/nscombobox/willdismissnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [class let willPopUpNotification: NSNotification.Name](../appkit/nscombobox/willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.
- [class let contextHelpModeDidActivateNotification: NSNotification.Name](../appkit/nshelpmanager/contexthelpmodedidactivatenotification.md)
  Posted when the application enters context-sensitive help mode. This typically happens when the user holds down the Help key.
- [class let contextHelpModeDidDeactivateNotification: NSNotification.Name](../appkit/nshelpmanager/contexthelpmodediddeactivatenotification.md)
  Posted when the application exits context-sensitive help mode. This happens when the user clicks the mouse button while the cursor is anywhere on the screen after displaying a context-sensitive help topic.
- [class let textDidBeginEditingNotification: NSNotification.Name](../appkit/nscontrol/textdidbegineditingnotification.md)
  Sent when a control with editable cells begins an edit session.
- [class let textDidChangeNotification: NSNotification.Name](../appkit/nscontrol/textdidchangenotification.md)
  Sent when the text in the receiving control changes.
- [class let textDidEndEditingNotification: NSNotification.Name](../appkit/nscontrol/textdidendeditingnotification.md)
  Sent when a control with editable cells ends an editing session.
- [class let currentControlTintDidChangeNotification: NSNotification.Name](../appkit/nscolor/currentcontroltintdidchangenotification.md)
  Sent after the user changes control tint preference.
- [class let didCloseNotification: NSNotification.Name](../appkit/nsdrawer/didclosenotification.md)
  Posted whenever the drawer is closed.
- [class let didOpenNotification: NSNotification.Name](../appkit/nsdrawer/didopennotification.md)
  Posted whenever the drawer is opened.
- [class let willCloseNotification: NSNotification.Name](../appkit/nsdrawer/willclosenotification.md)
  Posted whenever the drawer is about to close.
- [class let willOpenNotification: NSNotification.Name](../appkit/nsdrawer/willopennotification.md)
  Posted whenever the drawer is about to open.
- [class let didChangeNotification: NSNotification.Name](../appkit/nsfontcollection/didchangenotification.md)
  Posted whenever a font collection is changed.
- [class let fontSetChangedNotification: NSNotification.Name](../appkit/nsfont/fontsetchangednotification.md)
  Posted after the currently-set font changes.
- [class let registryDidChangeNotification: NSNotification.Name](../appkit/nsimagerep/registrydidchangenotification.md)
  Posted whenever the image representation class registry changes.
- [class let didAddItemNotification: NSNotification.Name](../appkit/nsmenu/didadditemnotification.md)
  Posted after a menu item is added to the menu.
- [class let didBeginTrackingNotification: NSNotification.Name](../appkit/nsmenu/didbegintrackingnotification.md)
  Posted when menu tracking begins.
- [class let didChangeItemNotification: NSNotification.Name](../appkit/nsmenu/didchangeitemnotification.md)
  Posted after a menu item in the menu changes appearance.
- [class let didEndTrackingNotification: NSNotification.Name](../appkit/nsmenu/didendtrackingnotification.md)
  Posted when menu tracking ends, even if no action is sent.
- [class let didRemoveItemNotification: NSNotification.Name](../appkit/nsmenu/didremoveitemnotification.md)
  Posted after a menu item is removed from the menu.
- [class let didSendActionNotification: NSNotification.Name](../appkit/nsmenu/didsendactionnotification.md)
  Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [class let willSendActionNotification: NSNotification.Name](../appkit/nsmenu/willsendactionnotification.md)
  Posted just before the application dispatches a menu item’s action method to the menu item’s target.
- [class let columnDidMoveNotification: NSNotification.Name](../appkit/nsoutlineview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [class let columnDidResizeNotification: NSNotification.Name](../appkit/nsoutlineview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSOutlineView` object.
- [class let itemDidCollapseNotification: NSNotification.Name](../appkit/nsoutlineview/itemdidcollapsenotification.md)
  Posted whenever an item is collapsed in an `NSOutlineView` object.
- [class let itemDidExpandNotification: NSNotification.Name](../appkit/nsoutlineview/itemdidexpandnotification.md)
  Posted whenever an item is expanded in an `NSOutlineView` object.
- [class let itemWillCollapseNotification: NSNotification.Name](../appkit/nsoutlineview/itemwillcollapsenotification.md)
  Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [class let itemWillExpandNotification: NSNotification.Name](../appkit/nsoutlineview/itemwillexpandnotification.md)
  Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [class let selectionDidChangeNotification: NSNotification.Name](../appkit/nsoutlineview/selectiondidchangenotification.md)
  Posted after the outline view’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](../appkit/nsoutlineview/selectionischangingnotification.md)
  Posted as the outline view’s selection changes (while the mouse button is still down).
- [class let willPopUpNotification: NSNotification.Name](../appkit/nspopupbuttoncell/willpopupnotification.md)
  This notification is posted just before a pop-up menu is attached to its window frame.
- [class let willPopUpNotification: NSNotification.Name](../appkit/nspopupbutton/willpopupnotification.md)
  Posted when an `NSPopUpButton` object receives a mouse-down event—that is, when the user is about to select an item from the menu.
- [class let didCloseNotification: NSNotification.Name](../appkit/nspopover/didclosenotification.md)
  Sent after the popover has finished animating offscreen.
- [class let didShowNotification: NSNotification.Name](../appkit/nspopover/didshownotification.md)
  Sent after the popover has finished animating onscreen.
- [class let willCloseNotification: NSNotification.Name](../appkit/nspopover/willclosenotification.md)
  Sent before the popover is closed.
- [class let willShowNotification: NSNotification.Name](../appkit/nspopover/willshownotification.md)
  Sent before the popover is shown.
- [class let preferredScrollerStyleDidChangeNotification: NSNotification.Name](../appkit/nsscroller/preferredscrollerstyledidchangenotification.md)
  Posted if the preferred scroller style changes.
- [class let rowsDidChangeNotification: NSNotification.Name](../appkit/nsruleeditor/rowsdidchangenotification.md)
  This notification is posted to the default notification center whenever the view’s rows change.
- [class let colorSpaceDidChangeNotification: NSNotification.Name](../appkit/nsscreen/colorspacedidchangenotification.md)
  Posted when the color space of the screen has changed.
- [class let didEndLiveMagnifyNotification: NSNotification.Name](../appkit/nsscrollview/didendlivemagnifynotification.md)
  Posted at the end of a magnify gesture.
- [class let didEndLiveScrollNotification: NSNotification.Name](../appkit/nsscrollview/didendlivescrollnotification.md)
  Posted on the main thread at the end of live scroll tracking.
- [class let didLiveScrollNotification: NSNotification.Name](../appkit/nsscrollview/didlivescrollnotification.md)
  Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.
- [class let willStartLiveMagnifyNotification: NSNotification.Name](../appkit/nsscrollview/willstartlivemagnifynotification.md)
  Posted at the beginning of a magnify gesture.
- [class let willStartLiveScrollNotification: NSNotification.Name](../appkit/nsscrollview/willstartlivescrollnotification.md)
  Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [class let didChangeAutomaticCapitalizationNotification: NSNotification.Name](../appkit/nsspellchecker/didchangeautomaticcapitalizationnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticCapitalizationMessage`](https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomaticcapitalizationmessage).
- [class let didChangeAutomaticDashSubstitutionNotification: NSNotification.Name](../appkit/nsspellchecker/didchangeautomaticdashsubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticDashSubstitutionMessage`](https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomaticdashsubstitutionmessage).
- [class let didChangeAutomaticPeriodSubstitutionNotification: NSNotification.Name](../appkit/nsspellchecker/didchangeautomaticperiodsubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticPeriodSubstitutionMessage`](https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomaticperiodsubstitutionmessage).
- [class let didChangeAutomaticQuoteSubstitutionNotification: NSNotification.Name](../appkit/nsspellchecker/didchangeautomaticquotesubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticQuoteSubstitutionMessage`](https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomaticquotesubstitutionmessage).
- [class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name](../appkit/nsspellchecker/didchangeautomaticspellingcorrectionnotification.md)
  This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.
- [class let didChangeAutomaticTextReplacementNotification: NSNotification.Name](../appkit/nsspellchecker/didchangeautomatictextreplacementnotification.md)
  Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.
- [class let didResizeSubviewsNotification: NSNotification.Name](../appkit/nssplitview/didresizesubviewsnotification.md)
  A notification that posts after a change to the size of some or all subviews of a split view.
- [class let willResizeSubviewsNotification: NSNotification.Name](../appkit/nssplitview/willresizesubviewsnotification.md)
  A notification that posts before a change to the size of some or all subviews of a split view.
- [class let systemColorsDidChangeNotification: NSNotification.Name](../appkit/nscolor/systemcolorsdidchangenotification.md)
  Sent when the system colors have changed, such as through a system control panel interface.
- [class let columnDidMoveNotification: NSNotification.Name](../appkit/nstableview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSTableView` object.
- [class let columnDidResizeNotification: NSNotification.Name](../appkit/nstableview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSTableView` object.
- [class let selectionDidChangeNotification: NSNotification.Name](../appkit/nstableview/selectiondidchangenotification.md)
  Posted after an `NSTableView` object’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](../appkit/nstableview/selectionischangingnotification.md)
  Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).
- [class let selectedAlternativeStringNotification: NSNotification.Name](../appkit/nstextalternatives/selectedalternativestringnotification.md)
  Posted when the user selects an alternate string.
- [class let didBeginEditingNotification: NSNotification.Name](../appkit/nstext/didbegineditingnotification.md)
  Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [class let didChangeNotification: NSNotification.Name](../appkit/nstext/didchangenotification.md)
  Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [class let didEndEditingNotification: NSNotification.Name](../appkit/nstext/didendeditingnotification.md)
  Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.
- [class let keyboardSelectionDidChangeNotification: NSNotification.Name](../appkit/nstextinputcontext/keyboardselectiondidchangenotification.md)
  Posted after the selected text input source changes.
- [class let didChangeAutomaticTextCompletionNotification: NSNotification.Name](../appkit/nsspellchecker/didchangeautomatictextcompletionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticTextCompletionMessage`](https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomatictextcompletionmessage).
- [class let didBecomeActiveNotification: NSNotification.Name](../appkit/nsapplication/didbecomeactivenotification.md)
  Posted immediately after the app becomes active.
- [class let didChangeOcclusionStateNotification: NSNotification.Name](../appkit/nsapplication/didchangeocclusionstatenotification.md)
  Posted when the app’s occlusion state changes.
- [class let didChangeScreenParametersNotification: NSNotification.Name](../appkit/nsapplication/didchangescreenparametersnotification.md)
  Posted when the configuration of the displays attached to the computer is changed.
- [class let didFinishLaunchingNotification: NSNotification.Name](../appkit/nsapplication/didfinishlaunchingnotification.md)
  Posted at the end of the [`finishLaunching()`](https://developer.apple.com/documentation/appkit/nsapplication/finishlaunching()) method to indicate that the app has completed launching and is ready to run.
- [class let didFinishRestoringWindowsNotification: NSNotification.Name](../appkit/nsapplication/didfinishrestoringwindowsnotification.md)
  Posted when the app has finished restoring windows.
- [class let didHideNotification: NSNotification.Name](../appkit/nsapplication/didhidenotification.md)
  Posted at the end of the [`hide(_:)`](https://developer.apple.com/documentation/appkit/nsapplication/hide(_:)) method to indicate that the app is now hidden.
- [class let didResignActiveNotification: NSNotification.Name](../appkit/nsapplication/didresignactivenotification.md)
  Posted immediately after the app gives up its active status to another app.
- [class let didUnhideNotification: NSNotification.Name](../appkit/nsapplication/didunhidenotification.md)
  Posted at the end of the [`unhideWithoutActivation()`](https://developer.apple.com/documentation/appkit/nsapplication/unhidewithoutactivation()) method to indicate that the app is now visible.
- [class let didUpdateNotification: NSNotification.Name](../appkit/nsapplication/didupdatenotification.md)
  Posted at the end of the [`updateWindows()`](https://developer.apple.com/documentation/appkit/nsapplication/updatewindows()) method to indicate that the app has finished updating its windows.
- [class let willBecomeActiveNotification: NSNotification.Name](../appkit/nsapplication/willbecomeactivenotification.md)
  Posted immediately before the app becomes active.
- [class let willFinishLaunchingNotification: NSNotification.Name](../appkit/nsapplication/willfinishlaunchingnotification.md)
  Posted at the start of the [`finishLaunching()`](https://developer.apple.com/documentation/appkit/nsapplication/finishlaunching()) method to indicate that the app has completed its initialization process and is about to finish launching.
- [class let willHideNotification: NSNotification.Name](../appkit/nsapplication/willhidenotification.md)
  Posted at the start of the [`hide(_:)`](https://developer.apple.com/documentation/appkit/nsapplication/hide(_:)) method to indicate that the app is about to be hidden.
- [class let willResignActiveNotification: NSNotification.Name](../appkit/nsapplication/willresignactivenotification.md)
  Posted immediately before the app gives up its active status to another app.
- [class let willTerminateNotification: NSNotification.Name](../appkit/nsapplication/willterminatenotification.md)
  Sends a notification to terminate the app.
- [class let willUnhideNotification: NSNotification.Name](../appkit/nsapplication/willunhidenotification.md)
  Posted at the start of the [`unhideWithoutActivation()`](https://developer.apple.com/documentation/appkit/nsapplication/unhidewithoutactivation()) method to indicate that the app is about to become visible.
- [class let willUpdateNotification: NSNotification.Name](../appkit/nsapplication/willupdatenotification.md)
  Posted at the start of the [`updateWindows()`](https://developer.apple.com/documentation/appkit/nsapplication/updatewindows()) method to indicate that the app is about to update its windows.
- [class let columnConfigurationDidChangeNotification: NSNotification.Name](../appkit/nsbrowser/columnconfigurationdidchangenotification.md)
  Notifies the delegate when the width of a browser column has changed.
- [static let NSClassDescriptionNeededForClass: NSNotification.Name](nsnotification/name-swift.struct/nsclassdescriptionneededforclass.md)
  Posted by [`init(for:)`](nsclassdescription/init(for:).md) when a class description cannot be found for a class.
- [static let NSApplicationProtectedDataDidBecomeAvailable: NSNotification.Name](nsnotification/name-swift.struct/nsapplicationprotecteddatadidbecomeavailable.md)
- [static let NSApplicationProtectedDataWillBecomeUnavailable: NSNotification.Name](nsnotification/name-swift.struct/nsapplicationprotecteddatawillbecomeunavailable.md)
- [static let announcementRequested: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/announcementrequested.md)
  This notification posts when an app needs to make an announcement to the user. If VoiceOver is enabled, it’s presented via speech and/or braille. Otherwise, it does nothing.
- [static let applicationActivated: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/applicationactivated.md)
  This notification is posted after the app has been activated. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let applicationDeactivated: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/applicationdeactivated.md)
  This notification is posted after the app has been deactivated.  Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let applicationHidden: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/applicationhidden.md)
  This notification is posted after the app is hidden. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let applicationShown: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/applicationshown.md)
  This notification is posted after the app is shown. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let created: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/created.md)
  This notification is posted after an accessibility element is created. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let drawerCreated: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/drawercreated.md)
  This notification is posted after a drawer appears. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let focusedUIElementChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/focuseduielementchanged.md)
  This notification is posted after an accessibility element gains focus. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let focusedWindowChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/focusedwindowchanged.md)
  This notification is posted after the key window changes. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let helpTagCreated: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/helptagcreated.md)
  This notification is posted after a help tag appears. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let layoutChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/layoutchanged.md)
  This notification is posted after the UI changes in a way that requires the attention of an accessibility client. This notification should be accompanied by a `userInfo` dictionary with the key [`uiElements`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notificationuserinfokey/uielements) and an array containing the UI elements that have been added or changed. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let mainWindowChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/mainwindowchanged.md)
  This notification is posted after the main window changes. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let moved: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/moved.md)
  This notification is posted after an accessibility element moves. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let resized: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/resized.md)
  This notification is posted after an accessibility element’s size changes. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let rowCollapsed: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/rowcollapsed.md)
  This notification is posted after a row collapses. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let rowCountChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/rowcountchanged.md)
  This notification is posted after a row is added or deleted. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let rowExpanded: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/rowexpanded.md)
  This notification is posted after a row expands. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let selectedCellsChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/selectedcellschanged.md)
  This notification is posted after one or more cells in a cell-based table are selected or deselected. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let selectedChildrenChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/selectedchildrenchanged.md)
  This notification is posted after one or more child elements are selected or deselected. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let selectedChildrenMoved: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/selectedchildrenmoved.md)
  This notification is posted after the selected items in a layout area move. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let selectedColumnsChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/selectedcolumnschanged.md)
  This notification is posted after one or more columns are selected or deselected. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let selectedRowsChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/selectedrowschanged.md)
  This notification is posted after one or more rows are selected or deselected. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let selectedTextChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/selectedtextchanged.md)
  This notification is posted after text is selected or deselected.  Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let sheetCreated: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/sheetcreated.md)
  This notification is posted after a sheet appears.  Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let titleChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/titlechanged.md)
  This notification is posted after an accessibility element’s title changes. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let uiElementDestroyed: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/uielementdestroyed.md)
  This notification is posted after an accessibility element is destroyed. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let unitsChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/unitschanged.md)
  This notification is posted after the units in a layout area change. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let valueChanged: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/valuechanged.md)
  This notification is posted after an accessibility element’s value changes. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let windowCreated: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/windowcreated.md)
  This notification is posted after a new window appears. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let windowDeminiaturized: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/windowdeminiaturized.md)
  This notification is posted after a window is restored to full size from the Dock.  Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let windowMiniaturized: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/windowminiaturized.md)
  This notification is posted after a window is put in the Dock. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let windowMoved: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/windowmoved.md)
  This notification is posted after a window moves.  Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [static let windowResized: NSAccessibility.Notification](../appkit/nsaccessibility-swift.struct/notification/windowresized.md)
  This notification is posted after a window’s size changes. Post this notification using the [`post(element:notification:)`](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [class let progressMarkNotification: NSNotification.Name](../appkit/nsanimation/progressmarknotification.md)
  Posted when the current progress of a running animation reaches one of its progress marks.
- [class let antialiasThresholdChangedNotification: NSNotification.Name](../appkit/nsfont/antialiasthresholdchangednotification.md)
  Posted after the threshold for antialiasing changes.
- [class let globalFrameDidChangeNotification: NSNotification.Name](../appkit/nsview/globalframedidchangenotification.md)
  Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated.
### AVFAudio
- [static let AVAudioEngineConfigurationChange: NSNotification.Name](nsnotification/name-swift.struct/avaudioengineconfigurationchange.md)
  A notification the framework posts when the audio engine configuration changes.
- [static let AVAudioUnitComponentTagsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avaudiounitcomponenttagsdidchange.md)
  A notification that indicates when component tags change.
- [class let interruptionNotification: NSNotification.Name](../avfaudio/avaudiosession/interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.
- [class let mediaServicesWereLostNotification: NSNotification.Name](../avfaudio/avaudiosession/mediaserviceswerelostnotification.md)
  A notification the system posts when it terminates the media server.
- [class let mediaServicesWereResetNotification: NSNotification.Name](../avfaudio/avaudiosession/mediaserviceswereresetnotification.md)
  A notification the system posts when the media server restarts.
- [class let routeChangeNotification: NSNotification.Name](../avfaudio/avaudiosession/routechangenotification.md)
  A notification the system posts when its audio route changes.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](../avfaudio/avaudiosession/silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
### AVFoundation
- [static let AVAssetChapterMetadataGroupsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassetchaptermetadatagroupsdidchange.md)
  A notification the system posts when an asset’s chapter metadata groups change.
- [static let AVAssetContainsFragmentsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassetcontainsfragmentsdidchange.md)
  A notification the system posts when an asset’s fragments change.
- [static let AVAssetDurationDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassetdurationdidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
- [static let AVAssetMediaSelectionGroupsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassetmediaselectiongroupsdidchange.md)
  A notification the system posts when an asset’s media selection groups change.
- [static let AVAssetTrackSegmentsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassettracksegmentsdidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s segments.
- [static let AVAssetTrackTimeRangeDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassettracktimerangedidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s time range.
- [static let AVAssetTrackTrackAssociationsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassettracktrackassociationsdidchange.md)
  A notification the system posts when the track associations for an asset track change.
- [static let AVAssetWasDefragmented: NSNotification.Name](nsnotification/name-swift.struct/avassetwasdefragmented.md)
  A notification the system posts when a fragmented asset minder observes that the system defragments the asset on disk.
- [class let subjectAreaDidChangeNotification: NSNotification.Name](../avfoundation/avcapturedevice/subjectareadidchangenotification.md)
  A notification the system posts when a capture device detects a substantial change to the video subject area.
- [class let wasConnectedNotification: NSNotification.Name](../avfoundation/avcapturedevice/wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class let wasDisconnectedNotification: NSNotification.Name](../avfoundation/avcapturedevice/wasdisconnectednotification.md)
  A notification the system posts when an existing device becomes unavailable.
- [class let formatDescriptionDidChangeNotification: NSNotification.Name](../avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification.md)
  A notification the system posts when the capture input port’s format description changes.
- [class let didStartRunningNotification: NSNotification.Name](../avfoundation/avcapturesession/didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](../avfoundation/avcapturesession/didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let interruptionEndedNotification: NSNotification.Name](../avfoundation/avcapturesession/interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.
- [class let runtimeErrorNotification: NSNotification.Name](../avfoundation/avcapturesession/runtimeerrornotification.md)
  A notification the system posts when an error occurs during a capture session.
- [class let wasInterruptedNotification: NSNotification.Name](../avfoundation/avcapturesession/wasinterruptednotification.md)
  A notification the system posts when it interrupts a capture session.
- [static let AVFragmentedMovieContainsMovieFragmentsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avfragmentedmoviecontainsmoviefragmentsdidchange.md)
  A notification the system posts when a fragmented movie minder observes a change to a movie’s fragments.
- [static let AVFragmentedMovieDurationDidChange: NSNotification.Name](nsnotification/name-swift.struct/avfragmentedmoviedurationdidchange.md)
  A notification the system posts when a fragmented movie minder observes a change to a movie’s duration.
- [static let AVFragmentedMovieTrackSegmentsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avfragmentedmovietracksegmentsdidchange.md)
  A notification the system posts when a fragmented movie minder observes a change to a fragmented movie track’s segments.
- [static let AVFragmentedMovieTrackTimeRangeDidChange: NSNotification.Name](nsnotification/name-swift.struct/avfragmentedmovietracktimerangedidchange.md)
  A notification the system posts when a fragmented movie minder observes a change to a movie track’s time range.
- [static let AVFragmentedMovieWasDefragmented: NSNotification.Name](nsnotification/name-swift.struct/avfragmentedmoviewasdefragmented.md)
  A notification the system posts when a fragmented movie minder observes that the system defragments the asset on disk.
- [static let AVPlayerAvailableHDRModesDidChange: NSNotification.Name](nsnotification/name-swift.struct/avplayeravailablehdrmodesdidchange.md)
  A notification the system posts when a player’s available HDR modes change.
- [class let assetListResponseStatusDidChangeNotification: NSNotification.Name](../avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification.md)
  A notification the system posts when the status of an interstitial event’s asset list response changes.
- [class let didPlayToEndTimeNotification: NSNotification.Name](../avfoundation/avplayeritem/didplaytoendtimenotification.md)
  A notification the system posts when a player item plays to its end time.
- [class let failedToPlayToEndTimeNotification: NSNotification.Name](../avfoundation/avplayeritem/failedtoplaytoendtimenotification.md)
  A notification that the system posts when a player item fails to play to its end time.
- [class let newAccessLogEntryNotification: NSNotification.Name](../avfoundation/avplayeritem/newaccesslogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its access log.
- [class let newErrorLogEntryNotification: NSNotification.Name](../avfoundation/avplayeritem/newerrorlogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its error log.
- [class let playbackStalledNotification: NSNotification.Name](../avfoundation/avplayeritem/playbackstallednotification.md)
  A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](nsnotification/name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md)
  A notification the system posts when changes occur to its detected routes.
- [static let AVSampleBufferAudioRendererOutputConfigurationDidChange: NSNotification.Name](nsnotification/name-swift.struct/avsamplebufferaudiorendereroutputconfigurationdidchange.md)
  A notification the system posts to indicate that the hardware configuration doesn’t match the enqueued data format.
- [static let AVSampleBufferAudioRendererWasFlushedAutomatically: NSNotification.Name](nsnotification/name-swift.struct/avsamplebufferaudiorendererwasflushedautomatically.md)
  A notification the system posts when a renderer flushes its enqueued media data without an explicit request to do so.
- [static let AVSampleBufferDisplayLayerFailedToDecode: NSNotification.Name](nsnotification/name-swift.struct/avsamplebufferdisplaylayerfailedtodecode.md)
  A notification the system posts when a sample buffer display layer fails to decode.
- [static let AVSampleBufferDisplayLayerOutputObscuredDueToInsufficientExternalProtectionDidChange: NSNotification.Name](nsnotification/name-swift.struct/avsamplebufferdisplaylayeroutputobscuredduetoinsufficientexternalprotectiondidchange.md)
  A notification the system posts when the current device configuration doesn’t support the external content protection mechanism.
- [static let AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChange: NSNotification.Name](nsnotification/name-swift.struct/avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchange.md)
  A notification the system posts when a sample buffer display layer changes its decoding requirements.
- [class let timeJumpedNotification: NSNotification.Name](../avfoundation/avplayeritem/timejumpednotification.md)
  A notification the system posts when a player item’s time changes discontinuously.
- [static let AVFragmentedMovieTrackTotalSampleDataLengthDidChange: NSNotification.Name](nsnotification/name-swift.struct/avfragmentedmovietracktotalsampledatalengthdidchange.md)
  A notification the system posts when the sample data length of a fragmented movie track changes.
- [static var AVPlayerItemTimeJumped: NSNotification.Name](nsnotification/name-swift.struct/avplayeritemtimejumped.md)
  A notification the system posts to indicate a jump in a player item’s current time.
- [class let timeJumpedNotification: NSNotification.Name](../avfoundation/avplayeritem/timejumpednotification.md)
  A notification the system posts when a player item’s time changes discontinuously.
### AVKit
- [static let AVDisplayManagerModeSwitchSettingsChanged: NSNotification.Name](nsnotification/name-swift.struct/avdisplaymanagermodeswitchsettingschanged.md)
  A notification the display manager posts when a user changes their Match Content settings in the tvOS Settings app.
- [static let AVDisplayManagerModeSwitchStart: NSNotification.Name](nsnotification/name-swift.struct/avdisplaymanagermodeswitchstart.md)
  A notification the display manager posts when a display begins a mode switch.
- [static let AVDisplayManagerModeSwitchEnd: NSNotification.Name](nsnotification/name-swift.struct/avdisplaymanagermodeswitchend.md)
  A notification the display manager posts when a display ends a mode switch.
### ClockKit
- [static let CLKComplicationServerActiveComplicationsDidChange: NSNotification.Name](nsnotification/name-swift.struct/clkcomplicationserveractivecomplicationsdidchange.md)
  Posted when the set of active complications changes.
### CloudKit
- [static let CKAccountChanged: NSNotification.Name](nsnotification/name-swift.struct/ckaccountchanged.md)
  A notification that a container posts when the status of an iCloud account changes.
### Contacts
- [static let CNContactStoreDidChange: NSNotification.Name](nsnotification/name-swift.struct/cncontactstoredidchange.md)
  Posted when changes occur to the contact store.
### Core Data
- [static let NSManagedObjectContextDidSave: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave.md)
  A notification that posts before a context writes unsaved changes.
- [static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange.md)
  A notification that the coordinator posts after its registered stores change.
- [static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstorecoordinatorstoreswillchange.md)
  A notification that posts before a coordinator changes its registered stores.
- [static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstorecoordinatorwillremovestore.md)
  A notification that posts before a coordinator removes a store.
- [static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate: NSNotification.Name](nsnotification/name-swift.struct/nscoredatacorespotlightdelegateindexdidupdate.md)
  A notification that posts after Spotlight completes an index update.
- [static let NSManagedObjectContextDidMergeChangesObjectIDs: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidmergechangesobjectids.md)
  A notification that posts after a context merges changes from a different notification.
- [static let NSManagedObjectContextDidSaveObjectIDs: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidsaveobjectids.md)
  A notification that posts after a context finishes writing changes.
- [static let NSPersistentStoreRemoteChange: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstoreremotechange.md)
  A notification that posts after another process writes to a persistent store.
- [static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges.md)
  Posted after records are imported from the ubiquitous content store.
### Core Telephony
- [static let CTServiceRadioAccessTechnologyDidChange: NSNotification.Name](nsnotification/name-swift.struct/ctserviceradioaccesstechnologydidchange.md)
  A notification that posts when radio access technology changes.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](nsnotification/name-swift.struct/ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.
### Core WLAN
- [static let CWBSSIDDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwbssiddidchange.md)
- [static let CWCountryCodeDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwcountrycodedidchange.md)
- [static let CWLinkDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwlinkdidchange.md)
- [static let CWLinkQualityDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwlinkqualitydidchange.md)
- [static let CWModeDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwmodedidchange.md)
- [static let CWPowerDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwpowerdidchange.md)
- [static let CWSSIDDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwssiddidchange.md)
- [static let CWScanCacheDidUpdate: NSNotification.Name](nsnotification/name-swift.struct/cwscancachedidupdate.md)
### EventKit
- [static let EKEventStoreChanged: NSNotification.Name](nsnotification/name-swift.struct/ekeventstorechanged.md)
  A notification posted when changes are made to the Calendar database.
### External Accessory
- [static let EAAccessoryDidConnect: NSNotification.Name](nsnotification/name-swift.struct/eaaccessorydidconnect.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.
- [static let EAAccessoryDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/eaaccessorydiddisconnect.md)
  A notification that is posted when an accessory is disconnected and no longer available for your application to use.
### File Provider
- [static let fileProviderDomainDidChange: NSNotification.Name](nsnotification/name-swift.struct/fileproviderdomaindidchange.md)
- [static let fileProviderMaterializedSetDidChange: NSNotification.Name](nsnotification/name-swift.struct/fileprovidermaterializedsetdidchange.md)
- [static let fileProviderPendingSetDidChange: NSNotification.Name](nsnotification/name-swift.struct/fileproviderpendingsetdidchange.md)
### Foundation
- [static let NSUbiquityIdentityDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsubiquityidentitydidchange.md)
  Sent after the iCloud (“ubiquity”) identity has changed.
- [static let NSAppleEventManagerWillProcessFirstEvent: NSNotification.Name](nsnotification/name-swift.struct/nsappleeventmanagerwillprocessfirstevent.md)
  Posted by `NSAppleEventManager` before it first dispatches an Apple event. Your application can use this notification to avoid registering any Apple event handlers until the first time at which they may be needed.
- [static let NSUndoManagerCheckpoint: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagercheckpoint.md)
  Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [static let NSUndoManagerDidCloseUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.md)
  Posted after an undo manager closes an undo group.
- [static let NSUndoManagerDidOpenUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.md)
  Posted whenever an undo manager opens an undo group.
- [static let NSUndoManagerDidRedoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidredochange.md)
  Posted just after an undo manager performs a redo operation.
- [static let NSUndoManagerDidUndoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidundochange.md)
  Posted just after an undo manager performs an undo operation.
- [static let NSUndoManagerWillCloseUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md)
  Posted before an undo manager closes an undo group.
- [static let NSUndoManagerWillRedoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillredochange.md)
  Posted just before an undo manager performs a redo operation.
- [static let NSUndoManagerWillUndoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillundochange.md)
  Posted just before an undo manager performs an undo operation.
- [static let NSWillBecomeMultiThreaded: NSNotification.Name](nsnotification/name-swift.struct/nswillbecomemultithreaded.md)
  Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [`detachNewThreadSelector(_:toTarget:with:)`](thread/detachnewthreadselector(_:totarget:with:).md) or the [`start()`](thread/start().md) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing.
- [static let NSBundleResourceRequestLowDiskSpace: NSNotification.Name](nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace.md)
  Posted after the system detects that the amount of available disk space is getting low. The notification is posted to the default notification center.
- [static let NSCalendarDayChanged: NSNotification.Name](nsnotification/name-swift.struct/nscalendardaychanged.md)
  A notification that is posted whenever the calendar day of the system changes, as determined by the system calendar, locale, and time zone.
- [static let NSDidBecomeSingleThreaded: NSNotification.Name](nsnotification/name-swift.struct/nsdidbecomesinglethreaded.md)
  Not implemented.
- [static let NSExtensionHostDidBecomeActive: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostdidbecomeactive.md)
  Posted when the extension’s host app moves from the inactive to the active state.
- [static let NSExtensionHostDidEnterBackground: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostdidenterbackground.md)
  Posted when the extension’s host app begins running in the background.
- [static let NSExtensionHostWillEnterForeground: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostwillenterforeground.md)
  Posted when the extension’s host app begins running in the foreground.
- [static let NSExtensionHostWillResignActive: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostwillresignactive.md)
  Posted when the extension’s host app moves from the active to the inactive state.
- [static let NSFileHandleConnectionAccepted: NSNotification.Name](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md)
  Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.
- [static let NSFileHandleDataAvailable: NSNotification.Name](nsnotification/name-swift.struct/nsfilehandledataavailable.md)
  Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [static let NSFileHandleReadToEndOfFileCompletion: NSNotification.Name](nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion.md)
  Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.
- [static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name](nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged.md)
  A notification posted when the acceptance policy of the cookie storage has changed.
- [static let NSHTTPCookieManagerCookiesChanged: NSNotification.Name](nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged.md)
  A notification posted when the cookies stored in the cookie storage have changed.
- [static let NSMetadataQueryDidFinishGathering: NSNotification.Name](nsnotification/name-swift.struct/nsmetadataquerydidfinishgathering.md)
  Posted when the receiver has finished with the initial result-gathering phase of the query.
- [static let NSMetadataQueryDidStartGathering: NSNotification.Name](nsnotification/name-swift.struct/nsmetadataquerydidstartgathering.md)
  Posted when the receiver begins with the initial result-gathering phase of the query.
- [static let NSMetadataQueryDidUpdate: NSNotification.Name](nsnotification/name-swift.struct/nsmetadataquerydidupdate.md)
  Posted when the receiver’s results have changed during the live-update phase of the query.
- [static let NSMetadataQueryGatheringProgress: NSNotification.Name](nsnotification/name-swift.struct/nsmetadataquerygatheringprogress.md)
  Posted as the receiver is collecting results during the initial result-gathering phase of the query.
- [static let NSProcessInfoPowerStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md)
  Posts when the power state of a device changes.
- [static let NSSystemClockDidChange: NSNotification.Name](nsnotification/name-swift.struct/nssystemclockdidchange.md)
  A notification posted whenever the system clock is changed.
- [static let NSSystemTimeZoneDidChange: NSNotification.Name](nsnotification/name-swift.struct/nssystemtimezonedidchange.md)
  A notification posted when the time zone changes.
- [static let NSThreadWillExit: NSNotification.Name](nsnotification/name-swift.struct/nsthreadwillexit.md)
  An `NSThread` object posts this notification when it receives the [`exit()`](thread/exit().md) message, before the thread exits. Observer methods invoked to receive this notification execute in the exiting thread, before it exits.
- [static let NSURLCredentialStorageChanged: NSNotification.Name](nsnotification/name-swift.struct/nsurlcredentialstoragechanged.md)
  A notification posted when the set of stored credentials changes.
### Game Controller
- [static let GCControllerDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerdidconnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerdiddisconnect.md)
  A notification that posts after a controller disconnects from the device.
- [static let GCControllerDidBecomeCurrent: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerdidbecomecurrent.md)
  A notification that posts when a controller becomes the current controller.
- [static let GCControllerDidStopBeingCurrent: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerdidstopbeingcurrent.md)
  A notification that posts when a controller stops being the current controller.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerusercustomizationsdidchange.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.
- [static let GCKeyboardDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gckeyboarddidconnect.md)
  A notification that posts after a keyboard connects to the device.
- [static let GCKeyboardDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gckeyboarddiddisconnect.md)
  A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.
- [static let GCMouseDidBecomeCurrent: NSNotification.Name](nsnotification/name-swift.struct/gcmousedidbecomecurrent.md)
  A notification that posts when a mouse becomes the most recent mouse that the user connects.
- [static let GCMouseDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gcmousedidconnect.md)
  A notification that posts after a mouse connects to the device.
- [static let GCMouseDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gcmousediddisconnect.md)
  A notification that posts after a mouse disconnects from the device.
- [static let GCMouseDidStopBeingCurrent: NSNotification.Name](nsnotification/name-swift.struct/gcmousedidstopbeingcurrent.md)
  A notification that posts when a mouse stops being the most recent mouse that the user connects.
- [static let GCRacingWheelDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gcracingwheeldidconnect.md)
  A notification that posts after a racing wheel controller connects to the device.
- [static let GCRacingWheelDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gcracingwheeldiddisconnect.md)
  A notification that posts after a racing wheel controller disconnects from the device.
### GameKit
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](nsnotification/name-swift.struct/gkplayerauthenticationdidchangenotificationname.md)
  A notification that posts after GameKit authenticates the local player.
- [static let GKPlayerDidChangeNotificationName: NSNotification.Name](nsnotification/name-swift.struct/gkplayerdidchangenotificationname.md)
  A notification that posts when a player object’s data changes.
### HealthKit
- [static let HKUserPreferencesDidChange: NSNotification.Name](nsnotification/name-swift.struct/hkuserpreferencesdidchange.md)
  Notifies observers whenever the user changes his or her preferred units.
### HomeKit
- [let HMCharacteristicPropertySupportsEventNotification: String](../homekit/hmcharacteristicpropertysupportseventnotification-2f0ml.md)
  The characteristic supports event notifications.
### IOBluetooth
- [static let IOBluetoothHostControllerPoweredOff: NSNotification.Name](nsnotification/name-swift.struct/iobluetoothhostcontrollerpoweredoff.md)
- [static let IOBluetoothHostControllerPoweredOn: NSNotification.Name](nsnotification/name-swift.struct/iobluetoothhostcontrollerpoweredon.md)
- [static let IOBluetoothL2CAPChannelPublished: NSNotification.Name](nsnotification/name-swift.struct/iobluetoothl2capchannelpublished.md)
- [static let IOBluetoothL2CAPChannelTerminated: NSNotification.Name](nsnotification/name-swift.struct/iobluetoothl2capchannelterminated.md)
### iTunes Library
- [static let ITLibraryDidChange: NSNotification.Name](nsnotification/name-swift.struct/itlibrarydidchange.md)
  A notification the system posts when a library change occurs.
### MapKit
- [static let MKAnnotationCalloutInfoDidChange: NSNotification.Name](nsnotification/name-swift.struct/mkannotationcalloutinfodidchange.md)
  A property to observe to determine when the title or subtitle information of an annotation object changes.
### MediaPlayer
- [static let MPMusicPlayerControllerQueueDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmusicplayercontrollerqueuedidchange.md)
  Indicates the music player’s queue changed.
- [static let MPMediaLibraryDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmedialibrarydidchange.md)
  Indicates the media library has changed.
- [static let MPMediaPlaybackIsPreparedToPlayDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmediaplaybackispreparedtoplaydidchange.md)
  Indicates that the prepared to play status of the media player has changed.
- [static let MPMusicPlayerControllerNowPlayingItemDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmusicplayercontrollernowplayingitemdidchange.md)
  Posted when the currently playing media item has changed.
- [static let MPMusicPlayerControllerPlaybackStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmusicplayercontrollerplaybackstatedidchange.md)
  Posted when the playback state changes programmatically or by user action.
- [static let MPMusicPlayerControllerVolumeDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmusicplayercontrollervolumedidchange.md)
  Posted when the audio playback volume for the music player has changed.
- [static let MPMovieDurationAvailable: NSNotification.Name](nsnotification/name-swift.struct/mpmoviedurationavailable.md)
  Posted when the duration of a movie has been determined. There is no `userInfo` dictionary.
- [static let MPMovieMediaTypesAvailable: NSNotification.Name](nsnotification/name-swift.struct/mpmoviemediatypesavailable.md)
  Posted when the available media types in a movie are determined. There is no `userInfo` dictionary.
- [static let MPMovieNaturalSizeAvailable: NSNotification.Name](nsnotification/name-swift.struct/mpmovienaturalsizeavailable.md)
  Posted when the natural frame size of a movie is first determined or subsequently changes. There is no `userInfo` dictionary.
- [static let MPMoviePlayerDidEnterFullscreen: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerdidenterfullscreen.md)
  Posted when a movie player has entered full-screen mode. There is no `userInfo` dictionary.
- [static let MPMoviePlayerDidExitFullscreen: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerdidexitfullscreen.md)
  Posted when a movie player has exited full-screen mode. There is no `userInfo` dictionary.
- [static let MPMoviePlayerIsAirPlayVideoActiveDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerisairplayvideoactivedidchange.md)
  Posted when a movie player has started or ended playing a movie via AirPlay. There is no `userInfo` dictionary.
- [static let MPMoviePlayerLoadStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerloadstatedidchange.md)
  Posted when a movie player’s network buffering state has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerNowPlayingMovieDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayernowplayingmoviedidchange.md)
  Posted when the currently playing movie has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerPlaybackDidFinish: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerplaybackdidfinish.md)
  Posted when a movie has finished playing.
- [static let MPMoviePlayerPlaybackStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerplaybackstatedidchange.md)
  Posted when a movie player’s playback state has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerReadyForDisplayDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerreadyfordisplaydidchange.md)
  Posted when the ready for display state changes.
- [static let MPMoviePlayerScalingModeDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerscalingmodedidchange.md)
  Posted when the scaling mode of a movie player has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerThumbnailImageRequestDidFinish: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerthumbnailimagerequestdidfinish.md)
  Posted when a request to capture a thumbnail from a movie has finished whether the request succeeded or failed. Upon successful capture of a thumbnail, the `userInfo` dictionary contains values for the following keys:
- [static let MPMoviePlayerTimedMetadataUpdated: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayertimedmetadataupdated.md)
  Posted when new timed metadata arrives.
- [static let MPMoviePlayerWillEnterFullscreen: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerwillenterfullscreen.md)
  Posted when a movie player is about to enter full-screen mode.
- [static let MPMoviePlayerWillExitFullscreen: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerwillexitfullscreen.md)
  Posted when a movie player is about to exit full-screen mode.
- [static let MPMovieSourceTypeAvailable: NSNotification.Name](nsnotification/name-swift.struct/mpmoviesourcetypeavailable.md)
  Posted when the source type of a movie was previously unknown and is newly available. There is no `userInfo` dictionary.
- [static let MPVolumeViewWirelessRouteActiveDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpvolumeviewwirelessrouteactivedidchange.md)
  Indicates the active wireless route changed.
- [static let MPVolumeViewWirelessRoutesAvailableDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpvolumeviewwirelessroutesavailabledidchange.md)
  Indicates the available wireless routes changed.
### MessageUI
- [static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name](nsnotification/name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.md)
  Posted when the current device’s ability to send text messages changes.
- [static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name](nsnotification/name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.md)
  Posted when the current device’s ability to send text messages changes.
### NetworkExtension
- [static let NEFilterConfigurationDidChange: NSNotification.Name](nsnotification/name-swift.struct/nefilterconfigurationdidchange.md)
  Posted after the filter configuration stored in the Network Extension preferences changes.
- [static let NEVPNConfigurationChange: NSNotification.Name](nsnotification/name-swift.struct/nevpnconfigurationchange.md)
  Posted after the VPN configuration stored in the Network Extension preferences changes.
- [static let NEVPNStatusDidChange: NSNotification.Name](nsnotification/name-swift.struct/nevpnstatusdidchange.md)
  Posted when the status of the VPN connection changes.
- [static let NEDNSProxyConfigurationDidChange: NSNotification.Name](nsnotification/name-swift.struct/nednsproxyconfigurationdidchange.md)
  A notification that is posted when the DNS proxy configuration changes.
- [static let NEDNSSettingsConfigurationDidChange: NSNotification.Name](nsnotification/name-swift.struct/nednssettingsconfigurationdidchange.md)
### PassKit
- [static let PKPassLibraryDidChange: PKPassLibraryNotificationName](../passkit/pkpasslibrarynotificationname/pkpasslibrarydidchange.md)
  A notification that PassKit posts when the pass library changes.
- [static let PKPassLibraryRemotePaymentPassesDidChange: PKPassLibraryNotificationName](../passkit/pkpasslibrarynotificationname/pkpasslibraryremotepaymentpassesdidchange.md)
  A notification that PassKit posts when it adds or removes a pass on a paired remote device.
### PDFKit
- [static let PDFDocumentDidBeginFind: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidbeginfind.md)
  A notification that the document began a find operation.
- [static let PDFDocumentDidBeginPageFind: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidbeginpagefind.md)
  A notification that a find operation begins working on a new page of a document.
- [static let PDFDocumentDidBeginPageWrite: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidbeginpagewrite.md)
  A notification that a write operation begins working on a page in a document.
- [static let PDFDocumentDidBeginWrite: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidbeginwrite.md)
  A notification that a write operation begins working on a document.
- [static let PDFDocumentDidEndFind: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidendfind.md)
  A notification that the document finished a find operation.
- [static let PDFDocumentDidEndPageFind: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidendpagefind.md)
  A notification that a find operation finishes working on a page in a document.
- [static let PDFDocumentDidEndPageWrite: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidendpagewrite.md)
  A notification that a write operation finishes working on a page in a document.
- [static let PDFDocumentDidEndWrite: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidendwrite.md)
  A notification that a write operation finishes working on a document.
- [static let PDFDocumentDidFindMatch: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidfindmatch.md)
  A notification that a string match is found in a document.
- [static let PDFDocumentDidUnlock: NSNotification.Name](nsnotification/name-swift.struct/pdfdocumentdidunlock.md)
  A notification that a document unlocked.
- [static let PDFThumbnailViewDocumentEdited: NSNotification.Name](nsnotification/name-swift.struct/pdfthumbnailviewdocumentedited.md)
- [static let PDFViewAnnotationHit: NSNotification.Name](nsnotification/name-swift.struct/pdfviewannotationhit.md)
  A notification posted when the user clicks on an annotation.
- [static let PDFViewAnnotationWillHit: NSNotification.Name](nsnotification/name-swift.struct/pdfviewannotationwillhit.md)
  A notification posted before the user clicks an annotation.
- [static let PDFViewChangedHistory: NSNotification.Name](nsnotification/name-swift.struct/pdfviewchangedhistory.md)
  A notification posted when the page history changes.
- [static let PDFViewCopyPermission: NSNotification.Name](nsnotification/name-swift.struct/pdfviewcopypermission.md)
  A notification posted when the user attempts to copy to the pasteboard without the appropriate permissions.
- [static let PDFViewDisplayBoxChanged: NSNotification.Name](nsnotification/name-swift.struct/pdfviewdisplayboxchanged.md)
  A notification posted when the display box has changed.
- [static let PDFViewDisplayModeChanged: NSNotification.Name](nsnotification/name-swift.struct/pdfviewdisplaymodechanged.md)
  A notification posted when the display mode has changed.
- [static let PDFViewDocumentChanged: NSNotification.Name](nsnotification/name-swift.struct/pdfviewdocumentchanged.md)
  A notification posted when a new document is associated with the view.
- [static let PDFViewPageChanged: NSNotification.Name](nsnotification/name-swift.struct/pdfviewpagechanged.md)
  A notification posted when a new page becomes the current page.
- [static let PDFViewPrintPermission: NSNotification.Name](nsnotification/name-swift.struct/pdfviewprintpermission.md)
  A notification posted when the user attempts to print without the appropriate permissions.
- [static let PDFViewScaleChanged: NSNotification.Name](nsnotification/name-swift.struct/pdfviewscalechanged.md)
  A notification posted when the scale factor changes.
- [static let PDFViewSelectionChanged: NSNotification.Name](nsnotification/name-swift.struct/pdfviewselectionchanged.md)
  A notification posted when the current selection has changed.
- [static let PDFViewVisiblePagesChanged: NSNotification.Name](nsnotification/name-swift.struct/pdfviewvisiblepageschanged.md)
  A notification posted when the visible pages have changed.
### PreferencePanes
- [static let NSPreferencePaneCancelUnselect: NSNotification.Name](nsnotification/name-swift.struct/nspreferencepanecancelunselect.md)
  Notifies observers that the preference pane should not be deselected.
- [static let NSPreferencePaneDoUnselect: NSNotification.Name](nsnotification/name-swift.struct/nspreferencepanedounselect.md)
  Notifies observers that the preference pane may be deselected.
- [static let NSPreferencePaneSwitchToPane: NSNotification.Name](nsnotification/name-swift.struct/nspreferencepaneswitchtopane.md)
  Notifies observers that the user selected a new preference pane.
- [static let NSPreferencePaneUpdateHelpMenu: NSNotification.Name](nsnotification/name-swift.struct/nspreferencepaneupdatehelpmenu.md)
  Notifies observers that your help menu content changed.
- [static let NSPreferencePrefPaneIsAvailable: NSNotification.Name](nsnotification/name-swift.struct/nspreferenceprefpaneisavailable.md)
  Notifies observers that the system preferences app is available to display your preferences.
### Quartz
- [static let IKFilterBrowserFilterDoubleClick: NSNotification.Name](nsnotification/name-swift.struct/ikfilterbrowserfilterdoubleclick.md)
  Posted when the user double-clicks a filter in the filter browser.
- [static let IKFilterBrowserFilterSelected: NSNotification.Name](nsnotification/name-swift.struct/ikfilterbrowserfilterselected.md)
  Posted when the user clicks a filter name in the filter browser.
- [static let IKFilterBrowserWillPreviewFilter: NSNotification.Name](nsnotification/name-swift.struct/ikfilterbrowserwillpreviewfilter.md)
  Posted before showing a filter preview, allowing an application to set the parameters of a filter.
- [static let quartzFilterManagerDidAddFilter: NSNotification.Name](nsnotification/name-swift.struct/quartzfiltermanagerdidaddfilter.md)
- [static let quartzFilterManagerDidModifyFilter: NSNotification.Name](nsnotification/name-swift.struct/quartzfiltermanagerdidmodifyfilter.md)
- [static let quartzFilterManagerDidRemoveFilter: NSNotification.Name](nsnotification/name-swift.struct/quartzfiltermanagerdidremovefilter.md)
- [static let quartzFilterManagerDidSelectFilter: NSNotification.Name](nsnotification/name-swift.struct/quartzfiltermanagerdidselectfilter.md)
- [static let QCCompositionPickerPanelDidSelectComposition: NSNotification.Name](nsnotification/name-swift.struct/qccompositionpickerpaneldidselectcomposition.md)
  Posted when the user chooses a composition.
- [static let QCCompositionPickerViewDidSelectComposition: NSNotification.Name](nsnotification/name-swift.struct/qccompositionpickerviewdidselectcomposition.md)
  Posted when the user selects a composition in the picker view.
- [static let QCCompositionRepositoryDidUpdate: NSNotification.Name](nsnotification/name-swift.struct/qccompositionrepositorydidupdate.md)
  Posted whenever the list of compositions in the composition repository is updated.
- [static let QCViewDidStartRendering: NSNotification.Name](nsnotification/name-swift.struct/qcviewdidstartrendering.md)
  Posted when the view starts rendering.
- [static let QCViewDidStopRendering: NSNotification.Name](nsnotification/name-swift.struct/qcviewdidstoprendering.md)
  Posted when the view stops rendering.
### StoreKit
- [static let SKCloudServiceCapabilitiesDidChange: NSNotification.Name](nsnotification/name-swift.struct/skcloudservicecapabilitiesdidchange.md)
  A notification name for indicating a change in the capabilities associated with the Music library on the device.
- [static let SKStorefrontIdentifierDidChange: NSNotification.Name](nsnotification/name-swift.struct/skstorefrontidentifierdidchange.md)
  A notification name for indicating a change in the storefront identifier associated with the device.
- [static let SKStorefrontCountryCodeDidChange: NSNotification.Name](nsnotification/name-swift.struct/skstorefrontcountrycodedidchange.md)
  A notification name for indicating a change in the storefront country or region code associated with the device.
### TV Services
- [static let TVTopShelfItemsDidChange: NSNotification.Name](nsnotification/name-swift.struct/tvtopshelfitemsdidchange.md)
  A notification to post when your app’s Top Shelf content has changed.
### UIKit
- [static let announcementDidFinishNotification: NSNotification.Name](../uikit/uiaccessibility/announcementdidfinishnotification.md)
  A notification that UIKit posts when the system finishes reading an announcement.
- [static let elementFocusedNotification: NSNotification.Name](../uikit/uiaccessibility/elementfocusednotification.md)
  A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [static let assistiveTouchStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/assistivetouchstatusdidchangenotification.md)
  A notification that indicates a change in the status of AssistiveTouch.
- [static let boldTextStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/boldtextstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Bold Text setting changes.
- [static let closedCaptioningStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/closedcaptioningstatusdidchangenotification.md)
  A notification that UIKit posts when the setting for Closed Captions + SDH changes.
- [static let darkerSystemColorsStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/darkersystemcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [static let grayscaleStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/grayscalestatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Grayscale setting changes.
- [static let guidedAccessStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/guidedaccessstatusdidchangenotification.md)
  A notification that indicates when a Guided Access session starts or ends.
- [static let hearingDevicePairedEarDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/hearingdevicepairedeardidchangenotification.md)
  A notification that UIKit posts when there’s a change to the currently paired hearing devices.
- [static let invertColorsStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/invertcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the settings for inverted colors change.
- [static let monoAudioStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/monoaudiostatusdidchangenotification.md)
  A notification that UIKit posts when system audio changes from stereo to mono.
- [static let reduceMotionStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/reducemotionstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Motion setting changes.
- [static let reduceTransparencyStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/reducetransparencystatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [static let shakeToUndoDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/shaketoundodidchangenotification.md)
  A notification that UIKit posts when the system’s Shake to Undo setting changes.
- [static let speakScreenStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/speakscreenstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Screen setting changes.
- [static let speakSelectionStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/speakselectionstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Selection setting changes.
- [static let switchControlStatusDidChangeNotification: NSNotification.Name](../uikit/uiaccessibility/switchcontrolstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Switch Control setting changes.
- [class let didBecomeActiveNotification: NSNotification.Name](../uikit/uiapplication/didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](../uikit/uiapplication/didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let didFinishLaunchingNotification: NSNotification.Name](../uikit/uiapplication/didfinishlaunchingnotification.md)
  A notification that posts immediately after the app finishes launching.
- [class let didReceiveMemoryWarningNotification: NSNotification.Name](../uikit/uiapplication/didreceivememorywarningnotification.md)
  A notification that posts when the app receives a warning from the operating system about low memory availability.
- [class let significantTimeChangeNotification: NSNotification.Name](../uikit/uiapplication/significanttimechangenotification.md)
  A notification that posts when there’s a significant change in time.
- [class let userDidTakeScreenshotNotification: NSNotification.Name](../uikit/uiapplication/userdidtakescreenshotnotification.md)
  A notification that posts when a person takes a screenshot on the device.
- [class let willEnterForegroundNotification: NSNotification.Name](../uikit/uiapplication/willenterforegroundnotification.md)
  A notification that posts shortly before your app’s UI transitions to the foreground.
- [class let willResignActiveNotification: NSNotification.Name](../uikit/uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](../uikit/uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.
- [static let didChangeNotification: NSNotification.Name](../uikit/uicontentsizecategory/didchangenotification.md)
  A notification that posts when the user changes the preferred content size setting.
- [class let proximityStateDidChangeNotification: NSNotification.Name](../uikit/uidevice/proximitystatedidchangenotification.md)
  A notification that posts when the state of the proximity sensor changes.
- [class let brightnessDidChangeNotification: NSNotification.Name](../uikit/uiscreen/brightnessdidchangenotification.md)
  A notification that posts when a screen’s brightness changes.
- [class let didConnectNotification: NSNotification.Name](../uikit/uiscreen/didconnectnotification.md)
  A notification the system posts when a new screen connects to the device.
- [class let didDisconnectNotification: NSNotification.Name](../uikit/uiscreen/diddisconnectnotification.md)
  A notification the system posts when a screen disconnects from the device.
- [class let modeDidChangeNotification: NSNotification.Name](../uikit/uiscreen/modedidchangenotification.md)
  A notification that posts when a screen’s mode changes.
- [class let selectionDidChangeNotification: NSNotification.Name](../uikit/uitableview/selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.
- [class let textDidBeginEditingNotification: NSNotification.Name](../uikit/uitextfield/textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text field.
- [class let textDidChangeNotification: NSNotification.Name](../uikit/uitextfield/textdidchangenotification.md)
  A notification that alerts observers when the text in a text field changes.
- [class let textDidEndEditingNotification: NSNotification.Name](../uikit/uitextfield/textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text field.
- [class let currentInputModeDidChangeNotification: NSNotification.Name](../uikit/uitextinputmode/currentinputmodedidchangenotification.md)
  A notification that posts when the current input mode changes.
- [class let textDidBeginEditingNotification: NSNotification.Name](../uikit/uitextview/textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text view.
- [class let textDidChangeNotification: NSNotification.Name](../uikit/uitextview/textdidchangenotification.md)
  A notification that alerts observers when the text in a text view changes.
- [class let textDidEndEditingNotification: NSNotification.Name](../uikit/uitextview/textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text view.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](../uikit/uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.
- [class let didBecomeHiddenNotification: NSNotification.Name](../uikit/uiwindow/didbecomehiddennotification.md)
  A notification that posts when a window becomes hidden.
- [class let didBecomeKeyNotification: NSNotification.Name](../uikit/uiwindow/didbecomekeynotification.md)
  A notification that posts whenever a window becomes the key window.
- [class let didBecomeVisibleNotification: NSNotification.Name](../uikit/uiwindow/didbecomevisiblenotification.md)
  A notification that posts when a window becomes visible.
- [class let didResignKeyNotification: NSNotification.Name](../uikit/uiwindow/didresignkeynotification.md)
  A notification that posts whenever a window resigns its status as main window.
- [class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name](../uikit/uiapplication/backgroundrefreshstatusdidchangenotification.md)
  A notification that posts when the app’s status for downloading content in the background changes.
- [class let didChangeStatusBarFrameNotification: NSNotification.Name](../uikit/uiapplication/didchangestatusbarframenotification.md)
  Posted when the frame of the status bar changes.
- [class let didChangeStatusBarOrientationNotification: NSNotification.Name](../uikit/uiapplication/didchangestatusbarorientationnotification.md)
  Posted when the orientation of the app’s user interface changes.
- [class let willChangeStatusBarFrameNotification: NSNotification.Name](../uikit/uiapplication/willchangestatusbarframenotification.md)
  Posted when the app is about to change the frame of the status bar.
- [class let willChangeStatusBarOrientationNotification: NSNotification.Name](../uikit/uiapplication/willchangestatusbarorientationnotification.md)
  Posted when the app is about to change the orientation of its interface.
- [class let batteryLevelDidChangeNotification: NSNotification.Name](../uikit/uidevice/batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let batteryStateDidChangeNotification: NSNotification.Name](../uikit/uidevice/batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
- [class let orientationDidChangeNotification: NSNotification.Name](../uikit/uidevice/orientationdidchangenotification.md)
  A notification that posts when the orientation of the device changes.
- [class let stateChangedNotification: NSNotification.Name](../uikit/uidocument/statechangednotification.md)
  A notification the document object posts when there’s a change in the state of the document.
- [class let keyboardDidChangeFrameNotification: NSNotification.Name](../uikit/uiresponder/keyboarddidchangeframenotification.md)
  A notification that posts immediately after a change in the keyboard’s frame.
- [class let keyboardDidHideNotification: NSNotification.Name](../uikit/uiresponder/keyboarddidhidenotification.md)
  A notification that posts immediately after dismissing the keyboard.
- [class let keyboardDidShowNotification: NSNotification.Name](../uikit/uiresponder/keyboarddidshownotification.md)
  A notification that posts immediately after displaying the keyboard.
- [class let keyboardWillChangeFrameNotification: NSNotification.Name](../uikit/uiresponder/keyboardwillchangeframenotification.md)
  A notification that posts immediately prior to a change in the keyboard’s frame.
- [class let keyboardWillHideNotification: NSNotification.Name](../uikit/uiresponder/keyboardwillhidenotification.md)
  A notification that posts immediately prior to dismissing the keyboard.
- [class let keyboardWillShowNotification: NSNotification.Name](../uikit/uiresponder/keyboardwillshownotification.md)
  A notification that posts immediately prior to displaying the keyboard.
- [class let didHideMenuNotification: NSNotification.Name](../uikit/uimenucontroller/didhidemenunotification.md)
  Posted by the menu controller just after it hides the menu.
- [class let didShowMenuNotification: NSNotification.Name](../uikit/uimenucontroller/didshowmenunotification.md)
  Posted by the menu controller just after it shows the menu.
- [class let menuFrameDidChangeNotification: NSNotification.Name](../uikit/uimenucontroller/menuframedidchangenotification.md)
  Posted when the frame of a visible menu changes.
- [class let willHideMenuNotification: NSNotification.Name](../uikit/uimenucontroller/willhidemenunotification.md)
  Posted by the menu controller just before it hides the menu.
- [class let willShowMenuNotification: NSNotification.Name](../uikit/uimenucontroller/willshowmenunotification.md)
  Posted by the menu controller just before it shows the menu.
- [class let changedNotification: NSNotification.Name](../uikit/uipasteboard/changednotification.md)
  A notification that a pasteboard object posts when its contents change.
- [class let removedNotification: NSNotification.Name](../uikit/uipasteboard/removednotification.md)
  A notification that a pasteboard object posts just before an app removes it.
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](../uikit/uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](../uikit/uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.
### WatchKit
- [static let WKAccessibilityReduceMotionStatusDidChange: NSNotification.Name](nsnotification/name-swift.struct/wkaccessibilityreducemotionstatusdidchange.md)
  Tells the interface controller that the reduce motion status has changed.
- [static let WKAudioFilePlayerItemDidPlayToEndTime: NSNotification.Name](nsnotification/name-swift.struct/wkaudiofileplayeritemdidplaytoendtime.md)
  A notification that the item has played successfully to its end.
- [static let WKAudioFilePlayerItemFailedToPlayToEndTime: NSNotification.Name](nsnotification/name-swift.struct/wkaudiofileplayeritemfailedtoplaytoendtime.md)
  A notification that the item failed to play to its end.
- [static let WKAudioFilePlayerItemTimeJumped: NSNotification.Name](nsnotification/name-swift.struct/wkaudiofileplayeritemtimejumped.md)
  A notification that the item’s current time has changed discontinuously.
### WebKit
- [static let WebHistoryAllItemsRemoved: NSNotification.Name](nsnotification/name-swift.struct/webhistoryallitemsremoved.md)
  Posted when all history items have been removed from the web history.
- [static let WebHistoryItemChanged: NSNotification.Name](nsnotification/name-swift.struct/webhistoryitemchanged.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [static let WebHistoryItemsAdded: NSNotification.Name](nsnotification/name-swift.struct/webhistoryitemsadded.md)
  Posted when history items have been added to a web history.
- [static let WebHistoryItemsRemoved: NSNotification.Name](nsnotification/name-swift.struct/webhistoryitemsremoved.md)
  Posted when items have been removed from the web history.
- [static let WebHistoryLoaded: NSNotification.Name](nsnotification/name-swift.struct/webhistoryloaded.md)
  Posted when web history items have been loaded from a URL.
- [static let WebHistorySaved: NSNotification.Name](nsnotification/name-swift.struct/webhistorysaved.md)
  Posted when web history items have been saved to a URL.
- [static let WebPreferencesChanged: NSNotification.Name](nsnotification/name-swift.struct/webpreferenceschanged.md)
  Posted when the web preference settings are changed.
- [static let WebViewDidBeginEditing: NSNotification.Name](nsnotification/name-swift.struct/webviewdidbeginediting.md)
  Posted when a web view begins any operation that changes its contents in response to user editing.
- [static let WebViewDidChange: NSNotification.Name](nsnotification/name-swift.struct/webviewdidchange.md)
  Posted when a web view performs any operation that changes its contents in response to user editing.
- [static let WebViewDidChangeSelection: NSNotification.Name](nsnotification/name-swift.struct/webviewdidchangeselection.md)
  Posted when a web view changes its typing selection.
- [static let WebViewDidChangeTypingStyle: NSNotification.Name](nsnotification/name-swift.struct/webviewdidchangetypingstyle.md)
  Posted when a web view changes its typing style.
- [static let WebViewDidEndEditing: NSNotification.Name](nsnotification/name-swift.struct/webviewdidendediting.md)
  Posted when a web view ends any operation that changes its contents in response to user editing.
- [static let WebViewProgressEstimateChanged: NSNotification.Name](nsnotification/name-swift.struct/webviewprogressestimatechanged.md)
  Posted by a WebView object when the estimated progress value of a load changes.
- [static let WebViewProgressFinished: NSNotification.Name](nsnotification/name-swift.struct/webviewprogressfinished.md)
  Posted by a WebView object when the load has finished.
- [static let WebViewProgressStarted: NSNotification.Name](nsnotification/name-swift.struct/webviewprogressstarted.md)
  Posted by a WebView object when a load begins, including a load that is initiated in a subframe.
### Accounts
- [static let ACAccountStoreDidChange: NSNotification.Name](nsnotification/name-swift.struct/acaccountstoredidchange.md)
  Posted when the accounts managed by this account store changed in the database.
### Initializers
- [init(String)](nsnotification/name-swift.struct/init(_:).md)
- [init(rawValue: String)](nsnotification/name-swift.struct/init(rawvalue:).md)
### Type Properties
- [static var AVCaptureDeviceSubjectAreaDidChange: NSNotification.Name](nsnotification/name-swift.struct/avcapturedevicesubjectareadidchange.md)
- [static var AVCaptureDeviceWasConnected: NSNotification.Name](nsnotification/name-swift.struct/avcapturedevicewasconnected.md)
- [static var AVCaptureDeviceWasDisconnected: NSNotification.Name](nsnotification/name-swift.struct/avcapturedevicewasdisconnected.md)
- [static var AVCaptureInputPortFormatDescriptionDidChange: NSNotification.Name](nsnotification/name-swift.struct/avcaptureinputportformatdescriptiondidchange.md)
- [static var AVCaptureSessionDidStartRunning: NSNotification.Name](nsnotification/name-swift.struct/avcapturesessiondidstartrunning.md)
- [static var AVCaptureSessionDidStopRunning: NSNotification.Name](nsnotification/name-swift.struct/avcapturesessiondidstoprunning.md)
- [static var AVCaptureSessionInterruptionEnded: NSNotification.Name](nsnotification/name-swift.struct/avcapturesessioninterruptionended.md)
- [static var AVCaptureSessionRuntimeError: NSNotification.Name](nsnotification/name-swift.struct/avcapturesessionruntimeerror.md)
- [static var AVCaptureSessionWasInterrupted: NSNotification.Name](nsnotification/name-swift.struct/avcapturesessionwasinterrupted.md)
- [static var AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChange: NSNotification.Name](nsnotification/name-swift.struct/avplayerinterstitialeventmonitorassetlistresponsestatusdidchange.md)
- [static let AVPlayerInterstitialEventMonitorScheduleRequestCompleted: NSNotification.Name](nsnotification/name-swift.struct/avplayerinterstitialeventmonitorschedulerequestcompleted.md)
- [static var AVPlayerItemDidPlayToEndTime: NSNotification.Name](nsnotification/name-swift.struct/avplayeritemdidplaytoendtime.md)
- [static var AVPlayerItemFailedToPlayToEndTime: NSNotification.Name](nsnotification/name-swift.struct/avplayeritemfailedtoplaytoendtime.md)
- [static var AVPlayerItemNewAccessLogEntry: NSNotification.Name](nsnotification/name-swift.struct/avplayeritemnewaccesslogentry.md)
- [static var AVPlayerItemNewErrorLogEntry: NSNotification.Name](nsnotification/name-swift.struct/avplayeritemnewerrorlogentry.md)
- [static var AVPlayerItemPlaybackStalled: NSNotification.Name](nsnotification/name-swift.struct/avplayeritemplaybackstalled.md)
- [static let AVSampleBufferDisplayLayerReadyForDisplayDidChange: NSNotification.Name](nsnotification/name-swift.struct/avsamplebufferdisplaylayerreadyfordisplaydidchange.md)
- [static var AXAnimatedImagesEnabledDidChange: NSNotification.Name](nsnotification/name-swift.struct/axanimatedimagesenableddidchange.md)
- [static var AXPrefersHeadAnchorAlternativeDidChange: NSNotification.Name](nsnotification/name-swift.struct/axprefersheadanchoralternativedidchange.md)
- [static var AXPrefersHorizontalTextLayoutDidChange: NSNotification.Name](nsnotification/name-swift.struct/axprefershorizontaltextlayoutdidchange.md)
- [static let DRBurnProgressPanelDidFinish: NSNotification.Name](nsnotification/name-swift.struct/drburnprogresspaneldidfinish.md)
- [static let DRBurnProgressPanelWillBegin: NSNotification.Name](nsnotification/name-swift.struct/drburnprogresspanelwillbegin.md)
- [static let DRBurnStatusChanged: NSNotification.Name](nsnotification/name-swift.struct/drburnstatuschanged.md)
- [static let DRDeviceAppeared: NSNotification.Name](nsnotification/name-swift.struct/drdeviceappeared.md)
- [static let DRDeviceDisappeared: NSNotification.Name](nsnotification/name-swift.struct/drdevicedisappeared.md)
- [static let DRDeviceStatusChanged: NSNotification.Name](nsnotification/name-swift.struct/drdevicestatuschanged.md)
- [static let DREraseProgressPanelDidFinish: NSNotification.Name](nsnotification/name-swift.struct/dreraseprogresspaneldidfinish.md)
- [static let DREraseProgressPanelWillBegin: NSNotification.Name](nsnotification/name-swift.struct/dreraseprogresspanelwillbegin.md)
- [static let DREraseStatusChanged: NSNotification.Name](nsnotification/name-swift.struct/drerasestatuschanged.md)
- [static let DRSetupPanelDeviceSelectionChanged: NSNotification.Name](nsnotification/name-swift.struct/drsetuppaneldeviceselectionchanged.md)
- [static let GCSpatialAccessoryDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gcspatialaccessorydidconnect.md)
- [static let GCSpatialAccessoryDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gcspatialaccessorydiddisconnect.md)
- [static let GCStylusDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gcstylusdidconnect.md)
- [static let GCStylusDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gcstylusdiddisconnect.md)
- [static let HMCharacteristicPropertySupportsEvent: NSNotification.Name](nsnotification/name-swift.struct/hmcharacteristicpropertysupportsevent.md)
- [static let MEVideoDecoderReadyForMoreMediaDataDidChange: NSNotification.Name](nsnotification/name-swift.struct/mevideodecoderreadyformoremediadatadidchange.md)
- [static let NERelayConfigurationDidChange: NSNotification.Name](nsnotification/name-swift.struct/nerelayconfigurationdidchange.md)
- [static let NEURLFilterConfigurationDidChange: Notification.Name](nsnotification/name-swift.struct/neurlfilterconfigurationdidchange.md)
  Name of the NSNotification that is posted when the URL filter configuration changes.
- [static let NEURLFilterStatusDidChange: Notification.Name](nsnotification/name-swift.struct/neurlfilterstatusdidchange.md)
  Name of the NSNotification that is posted when the URL filter status changes.
- [static let NSApplicationShouldBeginSuppressingHighDynamicRangeContent: NSNotification.Name](nsnotification/name-swift.struct/nsapplicationshouldbeginsuppressinghighdynamicrangecontent.md)
- [static let NSApplicationShouldEndSuppressingHighDynamicRangeContent: NSNotification.Name](nsnotification/name-swift.struct/nsapplicationshouldendsuppressinghighdynamicrangecontent.md)
- [static let NSProcessInfoPerformanceProfileDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsprocessinfoperformanceprofiledidchange.md)
- [static let NSSpellCheckerDidChangeAutomaticInlinePrediction: NSNotification.Name](nsnotification/name-swift.struct/nsspellcheckerdidchangeautomaticinlineprediction.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init?(coder: NSCoder)](nsnotification/init(coder:).md)
  Initializes a notification with the data from an unarchiver.
- [convenience init(name: NSNotification.Name, object: Any?)](nsnotification/init(name:object:).md)
  Returns a new notification object with a specified name and object.
- [init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](nsnotification/init(name:object:userinfo:).md)
  Initializes a notification with a specified name, object, and user information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct)*