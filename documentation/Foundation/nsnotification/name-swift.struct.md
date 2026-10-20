# NSNotification.Name

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * NSNotificationName;
```

## Topics

### AddressBook
- [static let abDatabaseChanged: NSNotification.Name](./name-swift.struct/abdatabasechanged.md)
  Posted when this process has changed the Address Book database.
- [static let abDatabaseChangedExternally: NSNotification.Name](./name-swift.struct/abdatabasechangedexternally.md)
  Posted when a process other than the current one has changed the Address Book database.
- [static let ABPeoplePickerDisplayedPropertyDidChange: NSNotification.Name](./name-swift.struct/abpeoplepickerdisplayedpropertydidchange.md)
  Posted when the displayed property in the record list is changed.
- [static let ABPeoplePickerGroupSelectionDidChange: NSNotification.Name](./name-swift.struct/abpeoplepickergroupselectiondidchange.md)
  Posted when the selection in the group list is changed.
- [static let ABPeoplePickerNameSelectionDidChange: NSNotification.Name](./name-swift.struct/abpeoplepickernameselectiondidchange.md)
  Posted when the selection in the name list is changed.
- [static let ABPeoplePickerValueSelectionDidChange: NSNotification.Name](./name-swift.struct/abpeoplepickervalueselectiondidchange.md)
  Posted when the selection in a multivalue property is changed.
### AppKit
- [static let unsupportedAttributeAddedNotification: NSNotification.Name](./name-swift.struct/unsupportedattributeaddednotification.md)
- [class let didProcessEditingNotification: NSNotification.Name](../../AppKit/nstextstorage/didprocesseditingnotification.md)
  A notification that posts after a text storage finishes processing edits.
- [class let willProcessEditingNotification: NSNotification.Name](../../AppKit/nstextstorage/willprocesseditingnotification.md)
  A notification that posts before a text storage begins processing edits.
- [class let didChangeSelectionNotification: NSNotification.Name](../../AppKit/nstextview/didchangeselectionnotification.md)
  Posted when the selected range of characters changes.
- [class let didChangeTypingAttributesNotification: NSNotification.Name](../../AppKit/nstextview/didchangetypingattributesnotification.md)
  Posted when there is a change in the typing attributes within a text view.
- [class let willChangeNotifyingTextViewNotification: NSNotification.Name](../../AppKit/nstextview/willchangenotifyingtextviewnotification.md)
  Posted when a new text view is established as the text view that sends notifications.
- [class let didRemoveItemNotification: NSNotification.Name](../../AppKit/nstoolbar/didremoveitemnotification.md)
  Posted after an item is removed from a toolbar.
- [class let willAddItemNotification: NSNotification.Name](../../AppKit/nstoolbar/willadditemnotification.md)
  Posts before the toolbar adds a new item.
- [class let boundsDidChangeNotification: NSNotification.Name](../../AppKit/nsview/boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](../../AppKit/nsview/didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.
- [class let frameDidChangeNotification: NSNotification.Name](../../AppKit/nsview/framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [class let didBecomeKeyNotification: NSNotification.Name](../../AppKit/nswindow/didbecomekeynotification.md)
  A notification that the window object became the key window.
- [class let didBecomeMainNotification: NSNotification.Name](../../AppKit/nswindow/didbecomemainnotification.md)
  A notification that the window object became the main window.
- [class let didChangeBackingPropertiesNotification: NSNotification.Name](../../AppKit/nswindow/didchangebackingpropertiesnotification.md)
  A notification that the window object backing properties changed.
- [class let didChangeOcclusionStateNotification: NSNotification.Name](../../AppKit/nswindow/didchangeocclusionstatenotification.md)
  A notification that the window object’s occlusion state changed.
- [class let didChangeScreenNotification: NSNotification.Name](../../AppKit/nswindow/didchangescreennotification.md)
  A notification that a portion of the window object’s frame moved onto or off of a screen.
- [class let didChangeScreenProfileNotification: NSNotification.Name](../../AppKit/nswindow/didchangescreenprofilenotification.md)
  A notification that the screen containing the window changed.
- [class let didDeminiaturizeNotification: NSNotification.Name](../../AppKit/nswindow/diddeminiaturizenotification.md)
  A notification that the window is no longer minimized.
- [class let didEndLiveResizeNotification: NSNotification.Name](../../AppKit/nswindow/didendliveresizenotification.md)
  A notification that the user resized the window object.
- [class let didEndSheetNotification: NSNotification.Name](../../AppKit/nswindow/didendsheetnotification.md)
  A notification that the window object closed an attached sheet.
- [class let didEnterFullScreenNotification: NSNotification.Name](../../AppKit/nswindow/didenterfullscreennotification.md)
  A notification that the window entered full-screen mode.
- [class let didEnterVersionBrowserNotification: NSNotification.Name](../../AppKit/nswindow/didenterversionbrowsernotification.md)
  A notification that the window object entered version browser mode.
- [class let didExitFullScreenNotification: NSNotification.Name](../../AppKit/nswindow/didexitfullscreennotification.md)
  A notification that the window object exited full-screen mode.
- [class let didExitVersionBrowserNotification: NSNotification.Name](../../AppKit/nswindow/didexitversionbrowsernotification.md)
  A notification that the window object exited version browser mode.
- [class let didExposeNotification: NSNotification.Name](../../AppKit/nswindow/didexposenotification.md)
  A notification that a window exposed a portion of its nonretained content.
- [class let didMiniaturizeNotification: NSNotification.Name](../../AppKit/nswindow/didminiaturizenotification.md)
  A notification that the window object minimized.
- [class let didMoveNotification: NSNotification.Name](../../AppKit/nswindow/didmovenotification.md)
  A notification that the window object moved.
- [class let didResignKeyNotification: NSNotification.Name](../../AppKit/nswindow/didresignkeynotification.md)
  A notification that the window object resigned its status as key window.
- [class let didResignMainNotification: NSNotification.Name](../../AppKit/nswindow/didresignmainnotification.md)
  A notification that the window object resigned its status as main window.
- [class let didResizeNotification: NSNotification.Name](../../AppKit/nswindow/didresizenotification.md)
  A notification that the window object size changed.
- [class let didUpdateNotification: NSNotification.Name](../../AppKit/nswindow/didupdatenotification.md)
  A notification that the window object received an update message.
- [class let willBeginSheetNotification: NSNotification.Name](../../AppKit/nswindow/willbeginsheetnotification.md)
  A notification that the window object is about to open a sheet.
- [class let willCloseNotification: NSNotification.Name](../../AppKit/nswindow/willclosenotification.md)
  A notification that the window object is about to close.
- [class let willEnterFullScreenNotification: NSNotification.Name](../../AppKit/nswindow/willenterfullscreennotification.md)
  A notification that the window will enter full-screen mode.
- [class let willEnterVersionBrowserNotification: NSNotification.Name](../../AppKit/nswindow/willenterversionbrowsernotification.md)
  A notification that the window object will enter version browser mode.
- [class let willExitFullScreenNotification: NSNotification.Name](../../AppKit/nswindow/willexitfullscreennotification.md)
  A notification that the window object will exit full-screen mode.
- [class let willExitVersionBrowserNotification: NSNotification.Name](../../AppKit/nswindow/willexitversionbrowsernotification.md)
  A notification that the window object will exit version browser mode.
- [class let willMiniaturizeNotification: NSNotification.Name](../../AppKit/nswindow/willminiaturizenotification.md)
  A notification that the window object is about to minimize.
- [class let willMoveNotification: NSNotification.Name](../../AppKit/nswindow/willmovenotification.md)
  A notification that the window object is about to move.
- [class let willStartLiveResizeNotification: NSNotification.Name](../../AppKit/nswindow/willstartliveresizenotification.md)
  A notification that the user is about to resize the window.
- [class let accessibilityDisplayOptionsDidChangeNotification: NSNotification.Name](../../AppKit/nsworkspace/accessibilitydisplayoptionsdidchangenotification.md)
  A notification that the workspace posts when any of the accessibility display options change.
- [class let activeSpaceDidChangeNotification: NSNotification.Name](../../AppKit/nsworkspace/activespacedidchangenotification.md)
  A notification that the workspace posts when a Spaces change occurs.
- [class let didActivateApplicationNotification: NSNotification.Name](../../AppKit/nsworkspace/didactivateapplicationnotification.md)
  A notification that the workspace posts when the Finder is about to activate an app.
- [class let didChangeFileLabelsNotification: NSNotification.Name](../../AppKit/nsworkspace/didchangefilelabelsnotification.md)
  A notification that the workspace posts when the Finder file labels or colors change.
- [class let didDeactivateApplicationNotification: NSNotification.Name](../../AppKit/nsworkspace/diddeactivateapplicationnotification.md)
  A notification that the workspace posts when the Finder deactivates an app.
- [class let didHideApplicationNotification: NSNotification.Name](../../AppKit/nsworkspace/didhideapplicationnotification.md)
  A notification that the workspace posts when the Finder hides an app.
- [class let didLaunchApplicationNotification: NSNotification.Name](../../AppKit/nsworkspace/didlaunchapplicationnotification.md)
  A notification that the workspace posts when a new app starts up.
- [class let didMountNotification: NSNotification.Name](../../AppKit/nsworkspace/didmountnotification.md)
  A notification that the workspace posts when a new device mounts.
- [class let didPerformFileOperationNotification: NSNotification.Name](../../AppKit/nsworkspace/didperformfileoperationnotification.md)
  Posted when a file operation has been performed in the receiving app.
- [class let didRenameVolumeNotification: NSNotification.Name](../../AppKit/nsworkspace/didrenamevolumenotification.md)
  A notification that the workspace posts when a volume changes its name or mount path.
- [class let didTerminateApplicationNotification: NSNotification.Name](../../AppKit/nsworkspace/didterminateapplicationnotification.md)
  A notification that the workspace posts when an app finishes executing.
- [class let didUnhideApplicationNotification: NSNotification.Name](../../AppKit/nsworkspace/didunhideapplicationnotification.md)
  A notification that the workspace posts when the Finder unhides an app.
- [class let didUnmountNotification: NSNotification.Name](../../AppKit/nsworkspace/didunmountnotification.md)
  A notification that the workspace posts when the Finder unmounts a device.
- [class let didWakeNotification: NSNotification.Name](../../AppKit/nsworkspace/didwakenotification.md)
  A notification that the workspace posts when the device wakes from sleep.
- [class let screensDidSleepNotification: NSNotification.Name](../../AppKit/nsworkspace/screensdidsleepnotification.md)
  A notification that the workspace posts when the device’s screen goes to sleep.
- [class let screensDidWakeNotification: NSNotification.Name](../../AppKit/nsworkspace/screensdidwakenotification.md)
  A notification that the workspace posts when the device’s screens wake.
- [class let sessionDidBecomeActiveNotification: NSNotification.Name](../../AppKit/nsworkspace/sessiondidbecomeactivenotification.md)
  A notification that the workspace posts after a user session switches in.
- [class let sessionDidResignActiveNotification: NSNotification.Name](../../AppKit/nsworkspace/sessiondidresignactivenotification.md)
  A notification that the workspace posts before a user session switches out.
- [class let willLaunchApplicationNotification: NSNotification.Name](../../AppKit/nsworkspace/willlaunchapplicationnotification.md)
  A notification that the workspace posts when the Finder is about to launch an app.
- [class let willPowerOffNotification: NSNotification.Name](../../AppKit/nsworkspace/willpoweroffnotification.md)
  A notification that the workspace posts when the user requests a logout or powers off the device.
- [class let willSleepNotification: NSNotification.Name](../../AppKit/nsworkspace/willsleepnotification.md)
  A notification that the workspace posts before the device goes to sleep.
- [class let willUnmountNotification: NSNotification.Name](../../AppKit/nsworkspace/willunmountnotification.md)
  A notification that the workspace posts when the Finder is about to unmount a device.
- [class let didChangeNotification: NSNotification.Name](../../AppKit/nscolorlist/didchangenotification.md)
  Posted whenever a color list changes.
- [class let didChangeNotification: NSNotification.Name](../../AppKit/nscolorlist/didchangenotification.md)
  Posted whenever a color list changes.
- [class let selectionDidChangeNotification: NSNotification.Name](../../AppKit/nscombobox/selectiondidchangenotification.md)
  Posted after the pop-up list selection of the `NSComboBox` changes.
- [class let selectionIsChangingNotification: NSNotification.Name](../../AppKit/nscombobox/selectionischangingnotification.md)
  Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [class let willDismissNotification: NSNotification.Name](../../AppKit/nscombobox/willdismissnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [class let willPopUpNotification: NSNotification.Name](../../AppKit/nscombobox/willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.
- [class let contextHelpModeDidActivateNotification: NSNotification.Name](../../AppKit/nshelpmanager/contexthelpmodedidactivatenotification.md)
  Posted when the application enters context-sensitive help mode. This typically happens when the user holds down the Help key.
- [class let contextHelpModeDidDeactivateNotification: NSNotification.Name](../../AppKit/nshelpmanager/contexthelpmodediddeactivatenotification.md)
  Posted when the application exits context-sensitive help mode. This happens when the user clicks the mouse button while the cursor is anywhere on the screen after displaying a context-sensitive help topic.
- [class let textDidBeginEditingNotification: NSNotification.Name](../../AppKit/nscontrol/textdidbegineditingnotification.md)
  Sent when a control with editable cells begins an edit session.
- [class let textDidChangeNotification: NSNotification.Name](../../AppKit/nscontrol/textdidchangenotification.md)
  Sent when the text in the receiving control changes.
- [class let textDidEndEditingNotification: NSNotification.Name](../../AppKit/nscontrol/textdidendeditingnotification.md)
  Sent when a control with editable cells ends an editing session.
- [class let currentControlTintDidChangeNotification: NSNotification.Name](../../AppKit/nscolor/currentcontroltintdidchangenotification.md)
  Sent after the user changes control tint preference.
- [class let didCloseNotification: NSNotification.Name](../../AppKit/nsdrawer/didclosenotification.md)
  Posted whenever the drawer is closed.
- [class let didOpenNotification: NSNotification.Name](../../AppKit/nsdrawer/didopennotification.md)
  Posted whenever the drawer is opened.
- [class let willCloseNotification: NSNotification.Name](../../AppKit/nsdrawer/willclosenotification.md)
  Posted whenever the drawer is about to close.
- [class let willOpenNotification: NSNotification.Name](../../AppKit/nsdrawer/willopennotification.md)
  Posted whenever the drawer is about to open.
- [class let didChangeNotification: NSNotification.Name](../../AppKit/nsfontcollection/didchangenotification.md)
  Posted whenever a font collection is changed.
- [class let fontSetChangedNotification: NSNotification.Name](../../AppKit/nsfont/fontsetchangednotification.md)
  Posted after the currently-set font changes.
- [class let registryDidChangeNotification: NSNotification.Name](../../AppKit/nsimagerep/registrydidchangenotification.md)
  Posted whenever the image representation class registry changes.
- [class let didAddItemNotification: NSNotification.Name](../../AppKit/nsmenu/didadditemnotification.md)
  Posted after a menu item is added to the menu.
- [class let didBeginTrackingNotification: NSNotification.Name](../../AppKit/nsmenu/didbegintrackingnotification.md)
  Posted when menu tracking begins.
- [class let didChangeItemNotification: NSNotification.Name](../../AppKit/nsmenu/didchangeitemnotification.md)
  Posted after a menu item in the menu changes appearance.
- [class let didEndTrackingNotification: NSNotification.Name](../../AppKit/nsmenu/didendtrackingnotification.md)
  Posted when menu tracking ends, even if no action is sent.
- [class let didRemoveItemNotification: NSNotification.Name](../../AppKit/nsmenu/didremoveitemnotification.md)
  Posted after a menu item is removed from the menu.
- [class let didSendActionNotification: NSNotification.Name](../../AppKit/nsmenu/didsendactionnotification.md)
  Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [class let willSendActionNotification: NSNotification.Name](../../AppKit/nsmenu/willsendactionnotification.md)
  Posted just before the application dispatches a menu item’s action method to the menu item’s target.
- [class let columnDidMoveNotification: NSNotification.Name](../../AppKit/nsoutlineview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [class let columnDidResizeNotification: NSNotification.Name](../../AppKit/nsoutlineview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSOutlineView` object.
- [class let itemDidCollapseNotification: NSNotification.Name](../../AppKit/nsoutlineview/itemdidcollapsenotification.md)
  Posted whenever an item is collapsed in an `NSOutlineView` object.
- [class let itemDidExpandNotification: NSNotification.Name](../../AppKit/nsoutlineview/itemdidexpandnotification.md)
  Posted whenever an item is expanded in an `NSOutlineView` object.
- [class let itemWillCollapseNotification: NSNotification.Name](../../AppKit/nsoutlineview/itemwillcollapsenotification.md)
  Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [class let itemWillExpandNotification: NSNotification.Name](../../AppKit/nsoutlineview/itemwillexpandnotification.md)
  Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [class let selectionDidChangeNotification: NSNotification.Name](../../AppKit/nsoutlineview/selectiondidchangenotification.md)
  Posted after the outline view’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](../../AppKit/nsoutlineview/selectionischangingnotification.md)
  Posted as the outline view’s selection changes (while the mouse button is still down).
- [class let willPopUpNotification: NSNotification.Name](../../AppKit/nspopupbuttoncell/willpopupnotification.md)
  This notification is posted just before a pop-up menu is attached to its window frame.
- [class let willPopUpNotification: NSNotification.Name](../../AppKit/nspopupbutton/willpopupnotification.md)
  Posted when an `NSPopUpButton` object receives a mouse-down event—that is, when the user is about to select an item from the menu.
- [class let didCloseNotification: NSNotification.Name](../../AppKit/nspopover/didclosenotification.md)
  Sent after the popover has finished animating offscreen.
- [class let didShowNotification: NSNotification.Name](../../AppKit/nspopover/didshownotification.md)
  Sent after the popover has finished animating onscreen.
- [class let willCloseNotification: NSNotification.Name](../../AppKit/nspopover/willclosenotification.md)
  Sent before the popover is closed.
- [class let willShowNotification: NSNotification.Name](../../AppKit/nspopover/willshownotification.md)
  Sent before the popover is shown.
- [class let preferredScrollerStyleDidChangeNotification: NSNotification.Name](../../AppKit/nsscroller/preferredscrollerstyledidchangenotification.md)
  Posted if the preferred scroller style changes.
- [class let rowsDidChangeNotification: NSNotification.Name](../../AppKit/nsruleeditor/rowsdidchangenotification.md)
  This notification is posted to the default notification center whenever the view’s rows change.
- [class let colorSpaceDidChangeNotification: NSNotification.Name](../../AppKit/nsscreen/colorspacedidchangenotification.md)
  Posted when the color space of the screen has changed.
- [class let didEndLiveMagnifyNotification: NSNotification.Name](../../AppKit/nsscrollview/didendlivemagnifynotification.md)
  Posted at the end of a magnify gesture.
- [class let didEndLiveScrollNotification: NSNotification.Name](../../AppKit/nsscrollview/didendlivescrollnotification.md)
  Posted on the main thread at the end of live scroll tracking.
- [class let didLiveScrollNotification: NSNotification.Name](../../AppKit/nsscrollview/didlivescrollnotification.md)
  Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.
- [class let willStartLiveMagnifyNotification: NSNotification.Name](../../AppKit/nsscrollview/willstartlivemagnifynotification.md)
  Posted at the beginning of a magnify gesture.
- [class let willStartLiveScrollNotification: NSNotification.Name](../../AppKit/nsscrollview/willstartlivescrollnotification.md)
  Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [class let didChangeAutomaticCapitalizationNotification: NSNotification.Name](../../AppKit/nsspellchecker/didchangeautomaticcapitalizationnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticCapitalizationMessage`](../../AppKit/nsspellchecker/didchangeautomaticcapitalizationmessage.md).
- [class let didChangeAutomaticDashSubstitutionNotification: NSNotification.Name](../../AppKit/nsspellchecker/didchangeautomaticdashsubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticDashSubstitutionMessage`](../../AppKit/nsspellchecker/didchangeautomaticdashsubstitutionmessage.md).
- [class let didChangeAutomaticPeriodSubstitutionNotification: NSNotification.Name](../../AppKit/nsspellchecker/didchangeautomaticperiodsubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticPeriodSubstitutionMessage`](../../AppKit/nsspellchecker/didchangeautomaticperiodsubstitutionmessage.md).
- [class let didChangeAutomaticQuoteSubstitutionNotification: NSNotification.Name](../../AppKit/nsspellchecker/didchangeautomaticquotesubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticQuoteSubstitutionMessage`](../../AppKit/nsspellchecker/didchangeautomaticquotesubstitutionmessage.md).
- [class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name](../../AppKit/nsspellchecker/didchangeautomaticspellingcorrectionnotification.md)
  This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.
- [class let didChangeAutomaticTextReplacementNotification: NSNotification.Name](../../AppKit/nsspellchecker/didchangeautomatictextreplacementnotification.md)
  Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.
- [class let didResizeSubviewsNotification: NSNotification.Name](../../AppKit/nssplitview/didresizesubviewsnotification.md)
  A notification that posts after a change to the size of some or all subviews of a split view.
- [class let willResizeSubviewsNotification: NSNotification.Name](../../AppKit/nssplitview/willresizesubviewsnotification.md)
  A notification that posts before a change to the size of some or all subviews of a split view.
- [class let systemColorsDidChangeNotification: NSNotification.Name](../../AppKit/nscolor/systemcolorsdidchangenotification.md)
  Sent when the system colors have changed, such as through a system control panel interface.
- [class let columnDidMoveNotification: NSNotification.Name](../../AppKit/nstableview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSTableView` object.
- [class let columnDidResizeNotification: NSNotification.Name](../../AppKit/nstableview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSTableView` object.
- [class let selectionDidChangeNotification: NSNotification.Name](../../AppKit/nstableview/selectiondidchangenotification.md)
  Posted after an `NSTableView` object’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](../../AppKit/nstableview/selectionischangingnotification.md)
  Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).
- [class let selectedAlternativeStringNotification: NSNotification.Name](../../AppKit/nstextalternatives/selectedalternativestringnotification.md)
  Posted when the user selects an alternate string.
- [class let didBeginEditingNotification: NSNotification.Name](../../AppKit/nstext/didbegineditingnotification.md)
  Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [class let didChangeNotification: NSNotification.Name](../../AppKit/nstext/didchangenotification.md)
  Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [class let didEndEditingNotification: NSNotification.Name](../../AppKit/nstext/didendeditingnotification.md)
  Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.
- [class let keyboardSelectionDidChangeNotification: NSNotification.Name](../../AppKit/nstextinputcontext/keyboardselectiondidchangenotification.md)
  Posted after the selected text input source changes.
- [class let didChangeAutomaticTextCompletionNotification: NSNotification.Name](../../AppKit/nsspellchecker/didchangeautomatictextcompletionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticTextCompletionMessage`](../../AppKit/nsspellchecker/didchangeautomatictextcompletionmessage.md).
- [class let didBecomeActiveNotification: NSNotification.Name](../../AppKit/nsapplication/didbecomeactivenotification.md)
  Posted immediately after the app becomes active.
- [class let didChangeOcclusionStateNotification: NSNotification.Name](../../AppKit/nsapplication/didchangeocclusionstatenotification.md)
  Posted when the app’s occlusion state changes.
- [class let didChangeScreenParametersNotification: NSNotification.Name](../../AppKit/nsapplication/didchangescreenparametersnotification.md)
  Posted when the configuration of the displays attached to the computer is changed.
- [class let didFinishLaunchingNotification: NSNotification.Name](../../AppKit/nsapplication/didfinishlaunchingnotification.md)
  Posted at the end of the [`finishLaunching()`](../../AppKit/nsapplication/finishlaunching%28%29.md) method to indicate that the app has completed launching and is ready to run.
- [class let didFinishRestoringWindowsNotification: NSNotification.Name](../../AppKit/nsapplication/didfinishrestoringwindowsnotification.md)
  Posted when the app has finished restoring windows.
- [class let didHideNotification: NSNotification.Name](../../AppKit/nsapplication/didhidenotification.md)
  Posted at the end of the [`hide(_:)`](../../AppKit/nsapplication/hide%28_%29.md) method to indicate that the app is now hidden.
- [class let didResignActiveNotification: NSNotification.Name](../../AppKit/nsapplication/didresignactivenotification.md)
  Posted immediately after the app gives up its active status to another app.
- [class let didUnhideNotification: NSNotification.Name](../../AppKit/nsapplication/didunhidenotification.md)
  Posted at the end of the [`unhideWithoutActivation()`](../../AppKit/nsapplication/unhidewithoutactivation%28%29.md) method to indicate that the app is now visible.
- [class let didUpdateNotification: NSNotification.Name](../../AppKit/nsapplication/didupdatenotification.md)
  Posted at the end of the [`updateWindows()`](../../AppKit/nsapplication/updatewindows%28%29.md) method to indicate that the app has finished updating its windows.
- [class let willBecomeActiveNotification: NSNotification.Name](../../AppKit/nsapplication/willbecomeactivenotification.md)
  Posted immediately before the app becomes active.
- [class let willFinishLaunchingNotification: NSNotification.Name](../../AppKit/nsapplication/willfinishlaunchingnotification.md)
  Posted at the start of the [`finishLaunching()`](../../AppKit/nsapplication/finishlaunching%28%29.md) method to indicate that the app has completed its initialization process and is about to finish launching.
- [class let willHideNotification: NSNotification.Name](../../AppKit/nsapplication/willhidenotification.md)
  Posted at the start of the [`hide(_:)`](../../AppKit/nsapplication/hide%28_%29.md) method to indicate that the app is about to be hidden.
- [class let willResignActiveNotification: NSNotification.Name](../../AppKit/nsapplication/willresignactivenotification.md)
  Posted immediately before the app gives up its active status to another app.
- [class let willTerminateNotification: NSNotification.Name](../../AppKit/nsapplication/willterminatenotification.md)
  Sends a notification to terminate the app.
- [class let willUnhideNotification: NSNotification.Name](../../AppKit/nsapplication/willunhidenotification.md)
  Posted at the start of the [`unhideWithoutActivation()`](../../AppKit/nsapplication/unhidewithoutactivation%28%29.md) method to indicate that the app is about to become visible.
- [class let willUpdateNotification: NSNotification.Name](../../AppKit/nsapplication/willupdatenotification.md)
  Posted at the start of the [`updateWindows()`](../../AppKit/nsapplication/updatewindows%28%29.md) method to indicate that the app is about to update its windows.
- [class let columnConfigurationDidChangeNotification: NSNotification.Name](../../AppKit/nsbrowser/columnconfigurationdidchangenotification.md)
  Notifies the delegate when the width of a browser column has changed.
- [static let NSClassDescriptionNeededForClass: NSNotification.Name](./name-swift.struct/nsclassdescriptionneededforclass.md)
  Posted by [`init(for:)`](../nsclassdescription/init%28for%29.md) when a class description cannot be found for a class.
- [static let NSApplicationProtectedDataDidBecomeAvailable: NSNotification.Name](./name-swift.struct/nsapplicationprotecteddatadidbecomeavailable.md)
- [static let NSApplicationProtectedDataWillBecomeUnavailable: NSNotification.Name](./name-swift.struct/nsapplicationprotecteddatawillbecomeunavailable.md)
- [static let announcementRequested: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/announcementrequested.md)
  This notification posts when an app needs to make an announcement to the user. If VoiceOver is enabled, it’s presented via speech and/or braille. Otherwise, it does nothing.
- [static let applicationActivated: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/applicationactivated.md)
  This notification is posted after the app has been activated. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationDeactivated: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/applicationdeactivated.md)
  This notification is posted after the app has been deactivated.  Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationHidden: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/applicationhidden.md)
  This notification is posted after the app is hidden. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationShown: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/applicationshown.md)
  This notification is posted after the app is shown. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let created: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/created.md)
  This notification is posted after an accessibility element is created. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let drawerCreated: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/drawercreated.md)
  This notification is posted after a drawer appears. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let focusedUIElementChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/focuseduielementchanged.md)
  This notification is posted after an accessibility element gains focus. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let focusedWindowChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/focusedwindowchanged.md)
  This notification is posted after the key window changes. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let helpTagCreated: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/helptagcreated.md)
  This notification is posted after a help tag appears. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let layoutChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/layoutchanged.md)
  This notification is posted after the UI changes in a way that requires the attention of an accessibility client. This notification should be accompanied by a `userInfo` dictionary with the key [`uiElements`](../../AppKit/nsaccessibility-swift.struct/notificationuserinfokey/uielements.md) and an array containing the UI elements that have been added or changed. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let mainWindowChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/mainwindowchanged.md)
  This notification is posted after the main window changes. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let moved: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/moved.md)
  This notification is posted after an accessibility element moves. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let resized: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/resized.md)
  This notification is posted after an accessibility element’s size changes. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let rowCollapsed: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/rowcollapsed.md)
  This notification is posted after a row collapses. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let rowCountChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/rowcountchanged.md)
  This notification is posted after a row is added or deleted. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let rowExpanded: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/rowexpanded.md)
  This notification is posted after a row expands. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedCellsChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/selectedcellschanged.md)
  This notification is posted after one or more cells in a cell-based table are selected or deselected. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedChildrenChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/selectedchildrenchanged.md)
  This notification is posted after one or more child elements are selected or deselected. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedChildrenMoved: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/selectedchildrenmoved.md)
  This notification is posted after the selected items in a layout area move. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedColumnsChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/selectedcolumnschanged.md)
  This notification is posted after one or more columns are selected or deselected. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedRowsChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/selectedrowschanged.md)
  This notification is posted after one or more rows are selected or deselected. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedTextChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/selectedtextchanged.md)
  This notification is posted after text is selected or deselected.  Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let sheetCreated: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/sheetcreated.md)
  This notification is posted after a sheet appears.  Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let titleChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/titlechanged.md)
  This notification is posted after an accessibility element’s title changes. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let uiElementDestroyed: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/uielementdestroyed.md)
  This notification is posted after an accessibility element is destroyed. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let unitsChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/unitschanged.md)
  This notification is posted after the units in a layout area change. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let valueChanged: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/valuechanged.md)
  This notification is posted after an accessibility element’s value changes. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowCreated: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/windowcreated.md)
  This notification is posted after a new window appears. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowDeminiaturized: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/windowdeminiaturized.md)
  This notification is posted after a window is restored to full size from the Dock.  Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowMiniaturized: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/windowminiaturized.md)
  This notification is posted after a window is put in the Dock. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowMoved: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/windowmoved.md)
  This notification is posted after a window moves.  Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowResized: NSAccessibility.Notification](../../AppKit/nsaccessibility-swift.struct/notification/windowresized.md)
  This notification is posted after a window’s size changes. Post this notification using the [`post(element:notification:)`](../../AppKit/nsaccessibility-swift.struct/post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [class let progressMarkNotification: NSNotification.Name](../../AppKit/nsanimation/progressmarknotification.md)
  Posted when the current progress of a running animation reaches one of its progress marks.
- [class let antialiasThresholdChangedNotification: NSNotification.Name](../../AppKit/nsfont/antialiasthresholdchangednotification.md)
  Posted after the threshold for antialiasing changes.
- [class let globalFrameDidChangeNotification: NSNotification.Name](../../AppKit/nsview/globalframedidchangenotification.md)
  Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated.
### AVFAudio
- [static let AVAudioEngineConfigurationChange: NSNotification.Name](./name-swift.struct/avaudioengineconfigurationchange.md)
  A notification the framework posts when the audio engine configuration changes.
- [static let AVAudioUnitComponentTagsDidChange: NSNotification.Name](./name-swift.struct/avaudiounitcomponenttagsdidchange.md)
  A notification that indicates when component tags change.
- [class let interruptionNotification: NSNotification.Name](../../AVFAudio/avaudiosession/interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.
- [class let mediaServicesWereLostNotification: NSNotification.Name](../../AVFAudio/avaudiosession/mediaserviceswerelostnotification.md)
  A notification the system posts when it terminates the media server.
- [class let mediaServicesWereResetNotification: NSNotification.Name](../../AVFAudio/avaudiosession/mediaserviceswereresetnotification.md)
  A notification the system posts when the media server restarts.
- [class let routeChangeNotification: NSNotification.Name](../../AVFAudio/avaudiosession/routechangenotification.md)
  A notification the system posts when its audio route changes.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](../../AVFAudio/avaudiosession/silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
### AVFoundation
- [static let AVAssetChapterMetadataGroupsDidChange: NSNotification.Name](./name-swift.struct/avassetchaptermetadatagroupsdidchange.md)
  A notification the system posts when an asset’s chapter metadata groups change.
- [static let AVAssetContainsFragmentsDidChange: NSNotification.Name](./name-swift.struct/avassetcontainsfragmentsdidchange.md)
  A notification the system posts when an asset’s fragments change.
- [static let AVAssetDurationDidChange: NSNotification.Name](./name-swift.struct/avassetdurationdidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
- [static let AVAssetMediaSelectionGroupsDidChange: NSNotification.Name](./name-swift.struct/avassetmediaselectiongroupsdidchange.md)
  A notification the system posts when an asset’s media selection groups change.
- [static let AVAssetTrackSegmentsDidChange: NSNotification.Name](./name-swift.struct/avassettracksegmentsdidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s segments.
- [static let AVAssetTrackTimeRangeDidChange: NSNotification.Name](./name-swift.struct/avassettracktimerangedidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s time range.
- [static let AVAssetTrackTrackAssociationsDidChange: NSNotification.Name](./name-swift.struct/avassettracktrackassociationsdidchange.md)
  A notification the system posts when the track associations for an asset track change.
- [static let AVAssetWasDefragmented: NSNotification.Name](./name-swift.struct/avassetwasdefragmented.md)
  A notification the system posts when a fragmented asset minder observes that the system defragments the asset on disk.
- [class let subjectAreaDidChangeNotification: NSNotification.Name](../../AVFoundation/avcapturedevice/subjectareadidchangenotification.md)
  A notification the system posts when a capture device detects a substantial change to the video subject area.
- [class let wasConnectedNotification: NSNotification.Name](../../AVFoundation/avcapturedevice/wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class let wasDisconnectedNotification: NSNotification.Name](../../AVFoundation/avcapturedevice/wasdisconnectednotification.md)
  A notification the system posts when an existing device becomes unavailable.
- [class let formatDescriptionDidChangeNotification: NSNotification.Name](../../AVFoundation/avcaptureinput/port/formatdescriptiondidchangenotification.md)
  A notification the system posts when the capture input port’s format description changes.
- [class let didStartRunningNotification: NSNotification.Name](../../AVFoundation/avcapturesession/didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](../../AVFoundation/avcapturesession/didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let interruptionEndedNotification: NSNotification.Name](../../AVFoundation/avcapturesession/interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.
- [class let runtimeErrorNotification: NSNotification.Name](../../AVFoundation/avcapturesession/runtimeerrornotification.md)
  A notification the system posts when an error occurs during a capture session.
- [class let wasInterruptedNotification: NSNotification.Name](../../AVFoundation/avcapturesession/wasinterruptednotification.md)
  A notification the system posts when it interrupts a capture session.
- [static let AVFragmentedMovieContainsMovieFragmentsDidChange: NSNotification.Name](./name-swift.struct/avfragmentedmoviecontainsmoviefragmentsdidchange.md)
  A notification the system posts when a fragmented movie minder observes a change to a movie’s fragments.
- [static let AVFragmentedMovieDurationDidChange: NSNotification.Name](./name-swift.struct/avfragmentedmoviedurationdidchange.md)
  A notification the system posts when a fragmented movie minder observes a change to a movie’s duration.
- [static let AVFragmentedMovieTrackSegmentsDidChange: NSNotification.Name](./name-swift.struct/avfragmentedmovietracksegmentsdidchange.md)
  A notification the system posts when a fragmented movie minder observes a change to a fragmented movie track’s segments.
- [static let AVFragmentedMovieTrackTimeRangeDidChange: NSNotification.Name](./name-swift.struct/avfragmentedmovietracktimerangedidchange.md)
  A notification the system posts when a fragmented movie minder observes a change to a movie track’s time range.
- [static let AVFragmentedMovieWasDefragmented: NSNotification.Name](./name-swift.struct/avfragmentedmoviewasdefragmented.md)
  A notification the system posts when a fragmented movie minder observes that the system defragments the asset on disk.
- [static let AVPlayerAvailableHDRModesDidChange: NSNotification.Name](./name-swift.struct/avplayeravailablehdrmodesdidchange.md)
  A notification the system posts when a player’s available HDR modes change.
- [class let assetListResponseStatusDidChangeNotification: NSNotification.Name](../../AVFoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification.md)
  A notification the system posts when the status of an interstitial event’s asset list response changes.
- [class let didPlayToEndTimeNotification: NSNotification.Name](../../AVFoundation/avplayeritem/didplaytoendtimenotification.md)
  A notification the system posts when a player item plays to its end time.
- [class let failedToPlayToEndTimeNotification: NSNotification.Name](../../AVFoundation/avplayeritem/failedtoplaytoendtimenotification.md)
  A notification that the system posts when a player item fails to play to its end time.
- [class let newAccessLogEntryNotification: NSNotification.Name](../../AVFoundation/avplayeritem/newaccesslogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its access log.
- [class let newErrorLogEntryNotification: NSNotification.Name](../../AVFoundation/avplayeritem/newerrorlogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its error log.
- [class let playbackStalledNotification: NSNotification.Name](../../AVFoundation/avplayeritem/playbackstallednotification.md)
  A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](./name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md)
  A notification the system posts when changes occur to its detected routes.
- [static let AVSampleBufferAudioRendererOutputConfigurationDidChange: NSNotification.Name](./name-swift.struct/avsamplebufferaudiorendereroutputconfigurationdidchange.md)
  A notification the system posts to indicate that the hardware configuration doesn’t match the enqueued data format.
- [static let AVSampleBufferAudioRendererWasFlushedAutomatically: NSNotification.Name](./name-swift.struct/avsamplebufferaudiorendererwasflushedautomatically.md)
  A notification the system posts when a renderer flushes its enqueued media data without an explicit request to do so.
- [static let AVSampleBufferDisplayLayerFailedToDecode: NSNotification.Name](./name-swift.struct/avsamplebufferdisplaylayerfailedtodecode.md)
  A notification the system posts when a sample buffer display layer fails to decode.
- [static let AVSampleBufferDisplayLayerOutputObscuredDueToInsufficientExternalProtectionDidChange: NSNotification.Name](./name-swift.struct/avsamplebufferdisplaylayeroutputobscuredduetoinsufficientexternalprotectiondidchange.md)
  A notification the system posts when the current device configuration doesn’t support the external content protection mechanism.
- [static let AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChange: NSNotification.Name](./name-swift.struct/avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchange.md)
  A notification the system posts when a sample buffer display layer changes its decoding requirements.
- [class let timeJumpedNotification: NSNotification.Name](../../AVFoundation/avplayeritem/timejumpednotification.md)
  A notification the system posts when a player item’s time changes discontinuously.
- [static let AVFragmentedMovieTrackTotalSampleDataLengthDidChange: NSNotification.Name](./name-swift.struct/avfragmentedmovietracktotalsampledatalengthdidchange.md)
  A notification the system posts when the sample data length of a fragmented movie track changes.
- [static var AVPlayerItemTimeJumped: NSNotification.Name](./name-swift.struct/avplayeritemtimejumped.md)
  A notification the system posts to indicate a jump in a player item’s current time.
- [class let timeJumpedNotification: NSNotification.Name](../../AVFoundation/avplayeritem/timejumpednotification.md)
  A notification the system posts when a player item’s time changes discontinuously.
### AVKit
- [static let AVDisplayManagerModeSwitchSettingsChanged: NSNotification.Name](./name-swift.struct/avdisplaymanagermodeswitchsettingschanged.md)
  A notification the display manager posts when a user changes their Match Content settings in the tvOS Settings app.
- [static let AVDisplayManagerModeSwitchStart: NSNotification.Name](./name-swift.struct/avdisplaymanagermodeswitchstart.md)
  A notification the display manager posts when a display begins a mode switch.
- [static let AVDisplayManagerModeSwitchEnd: NSNotification.Name](./name-swift.struct/avdisplaymanagermodeswitchend.md)
  A notification the display manager posts when a display ends a mode switch.
### ClockKit
- [static let CLKComplicationServerActiveComplicationsDidChange: NSNotification.Name](./name-swift.struct/clkcomplicationserveractivecomplicationsdidchange.md)
  Posted when the set of active complications changes.
### CloudKit
- [static let CKAccountChanged: NSNotification.Name](./name-swift.struct/ckaccountchanged.md)
  A notification that a container posts when the status of an iCloud account changes.
### Contacts
- [static let CNContactStoreDidChange: NSNotification.Name](./name-swift.struct/cncontactstoredidchange.md)
  Posted when changes occur to the contact store.
### Core Data
- [static let NSManagedObjectContextDidSave: NSNotification.Name](./name-swift.struct/nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](./name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](./name-swift.struct/nsmanagedobjectcontextwillsave.md)
  A notification that posts before a context writes unsaved changes.
- [static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name](./name-swift.struct/nspersistentstorecoordinatorstoresdidchange.md)
  A notification that the coordinator posts after its registered stores change.
- [static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name](./name-swift.struct/nspersistentstorecoordinatorstoreswillchange.md)
  A notification that posts before a coordinator changes its registered stores.
- [static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name](./name-swift.struct/nspersistentstorecoordinatorwillremovestore.md)
  A notification that posts before a coordinator removes a store.
- [static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate: NSNotification.Name](./name-swift.struct/nscoredatacorespotlightdelegateindexdidupdate.md)
  A notification that posts after Spotlight completes an index update.
- [static let NSManagedObjectContextDidMergeChangesObjectIDs: NSNotification.Name](./name-swift.struct/nsmanagedobjectcontextdidmergechangesobjectids.md)
  A notification that posts after a context merges changes from a different notification.
- [static let NSManagedObjectContextDidSaveObjectIDs: NSNotification.Name](./name-swift.struct/nsmanagedobjectcontextdidsaveobjectids.md)
  A notification that posts after a context finishes writing changes.
- [static let NSPersistentStoreRemoteChange: NSNotification.Name](./name-swift.struct/nspersistentstoreremotechange.md)
  A notification that posts after another process writes to a persistent store.
- [static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name](./name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges.md)
  Posted after records are imported from the ubiquitous content store.
### Core Telephony
- [static let CTServiceRadioAccessTechnologyDidChange: NSNotification.Name](./name-swift.struct/ctserviceradioaccesstechnologydidchange.md)
  A notification that posts when radio access technology changes.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](./name-swift.struct/ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.
### Core WLAN
- [static let CWBSSIDDidChange: NSNotification.Name](./name-swift.struct/cwbssiddidchange.md)
- [static let CWCountryCodeDidChange: NSNotification.Name](./name-swift.struct/cwcountrycodedidchange.md)
- [static let CWLinkDidChange: NSNotification.Name](./name-swift.struct/cwlinkdidchange.md)
- [static let CWLinkQualityDidChange: NSNotification.Name](./name-swift.struct/cwlinkqualitydidchange.md)
- [static let CWModeDidChange: NSNotification.Name](./name-swift.struct/cwmodedidchange.md)
- [static let CWPowerDidChange: NSNotification.Name](./name-swift.struct/cwpowerdidchange.md)
- [static let CWSSIDDidChange: NSNotification.Name](./name-swift.struct/cwssiddidchange.md)
- [static let CWScanCacheDidUpdate: NSNotification.Name](./name-swift.struct/cwscancachedidupdate.md)
### EventKit
- [static let EKEventStoreChanged: NSNotification.Name](./name-swift.struct/ekeventstorechanged.md)
  A notification posted when changes are made to the Calendar database.
### External Accessory
- [static let EAAccessoryDidConnect: NSNotification.Name](./name-swift.struct/eaaccessorydidconnect.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.
- [static let EAAccessoryDidDisconnect: NSNotification.Name](./name-swift.struct/eaaccessorydiddisconnect.md)
  A notification that is posted when an accessory is disconnected and no longer available for your application to use.
### File Provider
- [static let fileProviderDomainDidChange: NSNotification.Name](./name-swift.struct/fileproviderdomaindidchange.md)
- [static let fileProviderMaterializedSetDidChange: NSNotification.Name](./name-swift.struct/fileprovidermaterializedsetdidchange.md)
- [static let fileProviderPendingSetDidChange: NSNotification.Name](./name-swift.struct/fileproviderpendingsetdidchange.md)
### Foundation
- [static let NSUbiquityIdentityDidChange: NSNotification.Name](./name-swift.struct/nsubiquityidentitydidchange.md)
  Sent after the iCloud (“ubiquity”) identity has changed.
- [static let NSAppleEventManagerWillProcessFirstEvent: NSNotification.Name](./name-swift.struct/nsappleeventmanagerwillprocessfirstevent.md)
  Posted by `NSAppleEventManager` before it first dispatches an Apple event. Your application can use this notification to avoid registering any Apple event handlers until the first time at which they may be needed.
- [static let NSUndoManagerCheckpoint: NSNotification.Name](./name-swift.struct/nsundomanagercheckpoint.md)
  Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [static let NSUndoManagerDidCloseUndoGroup: NSNotification.Name](./name-swift.struct/nsundomanagerdidcloseundogroup.md)
  Posted after an undo manager closes an undo group.
- [static let NSUndoManagerDidOpenUndoGroup: NSNotification.Name](./name-swift.struct/nsundomanagerdidopenundogroup.md)
  Posted whenever an undo manager opens an undo group.
- [static let NSUndoManagerDidRedoChange: NSNotification.Name](./name-swift.struct/nsundomanagerdidredochange.md)
  Posted just after an undo manager performs a redo operation.
- [static let NSUndoManagerDidUndoChange: NSNotification.Name](./name-swift.struct/nsundomanagerdidundochange.md)
  Posted just after an undo manager performs an undo operation.
- [static let NSUndoManagerWillCloseUndoGroup: NSNotification.Name](./name-swift.struct/nsundomanagerwillcloseundogroup.md)
  Posted before an undo manager closes an undo group.
- [static let NSUndoManagerWillRedoChange: NSNotification.Name](./name-swift.struct/nsundomanagerwillredochange.md)
  Posted just before an undo manager performs a redo operation.
- [static let NSUndoManagerWillUndoChange: NSNotification.Name](./name-swift.struct/nsundomanagerwillundochange.md)
  Posted just before an undo manager performs an undo operation.
- [static let NSWillBecomeMultiThreaded: NSNotification.Name](./name-swift.struct/nswillbecomemultithreaded.md)
  Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [`detachNewThreadSelector(_:toTarget:with:)`](../thread/detachnewthreadselector%28_,totarget,with%29.md) or the [`start()`](../thread/start%28%29.md) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing.
- [static let NSBundleResourceRequestLowDiskSpace: NSNotification.Name](./name-swift.struct/nsbundleresourcerequestlowdiskspace.md)
  Posted after the system detects that the amount of available disk space is getting low. The notification is posted to the default notification center.
- [static let NSCalendarDayChanged: NSNotification.Name](./name-swift.struct/nscalendardaychanged.md)
  A notification that is posted whenever the calendar day of the system changes, as determined by the system calendar, locale, and time zone.
- [static let NSDidBecomeSingleThreaded: NSNotification.Name](./name-swift.struct/nsdidbecomesinglethreaded.md)
  Not implemented.
- [static let NSExtensionHostDidBecomeActive: NSNotification.Name](./name-swift.struct/nsextensionhostdidbecomeactive.md)
  Posted when the extension’s host app moves from the inactive to the active state.
- [static let NSExtensionHostDidEnterBackground: NSNotification.Name](./name-swift.struct/nsextensionhostdidenterbackground.md)
  Posted when the extension’s host app begins running in the background.
- [static let NSExtensionHostWillEnterForeground: NSNotification.Name](./name-swift.struct/nsextensionhostwillenterforeground.md)
  Posted when the extension’s host app begins running in the foreground.
- [static let NSExtensionHostWillResignActive: NSNotification.Name](./name-swift.struct/nsextensionhostwillresignactive.md)
  Posted when the extension’s host app moves from the active to the inactive state.
- [static let NSFileHandleConnectionAccepted: NSNotification.Name](./name-swift.struct/nsfilehandleconnectionaccepted.md)
  Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.
- [static let NSFileHandleDataAvailable: NSNotification.Name](./name-swift.struct/nsfilehandledataavailable.md)
  Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [static let NSFileHandleReadToEndOfFileCompletion: NSNotification.Name](./name-swift.struct/nsfilehandlereadtoendoffilecompletion.md)
  Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.
- [static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name](./name-swift.struct/nshttpcookiemanageracceptpolicychanged.md)
  A notification posted when the acceptance policy of the cookie storage has changed.
- [static let NSHTTPCookieManagerCookiesChanged: NSNotification.Name](./name-swift.struct/nshttpcookiemanagercookieschanged.md)
  A notification posted when the cookies stored in the cookie storage have changed.
- [static let NSMetadataQueryDidFinishGathering: NSNotification.Name](./name-swift.struct/nsmetadataquerydidfinishgathering.md)
  Posted when the receiver has finished with the initial result-gathering phase of the query.
- [static let NSMetadataQueryDidStartGathering: NSNotification.Name](./name-swift.struct/nsmetadataquerydidstartgathering.md)
  Posted when the receiver begins with the initial result-gathering phase of the query.
- [static let NSMetadataQueryDidUpdate: NSNotification.Name](./name-swift.struct/nsmetadataquerydidupdate.md)
  Posted when the receiver’s results have changed during the live-update phase of the query.
- [static let NSMetadataQueryGatheringProgress: NSNotification.Name](./name-swift.struct/nsmetadataquerygatheringprogress.md)
  Posted as the receiver is collecting results during the initial result-gathering phase of the query.
- [static let NSProcessInfoPowerStateDidChange: NSNotification.Name](./name-swift.struct/nsprocessinfopowerstatedidchange.md)
  Posts when the power state of a device changes.
- [static let NSSystemClockDidChange: NSNotification.Name](./name-swift.struct/nssystemclockdidchange.md)
  A notification posted whenever the system clock is changed.
- [static let NSSystemTimeZoneDidChange: NSNotification.Name](./name-swift.struct/nssystemtimezonedidchange.md)
  A notification posted when the time zone changes.
- [static let NSThreadWillExit: NSNotification.Name](./name-swift.struct/nsthreadwillexit.md)
  An `NSThread` object posts this notification when it receives the [`exit()`](../thread/exit%28%29.md) message, before the thread exits. Observer methods invoked to receive this notification execute in the exiting thread, before it exits.
- [static let NSURLCredentialStorageChanged: NSNotification.Name](./name-swift.struct/nsurlcredentialstoragechanged.md)
  A notification posted when the set of stored credentials changes.
### Game Controller
- [static let GCControllerDidConnect: NSNotification.Name](./name-swift.struct/gccontrollerdidconnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](./name-swift.struct/gccontrollerdiddisconnect.md)
  A notification that posts after a controller disconnects from the device.
- [static let GCControllerDidBecomeCurrent: NSNotification.Name](./name-swift.struct/gccontrollerdidbecomecurrent.md)
  A notification that posts when a controller becomes the current controller.
- [static let GCControllerDidStopBeingCurrent: NSNotification.Name](./name-swift.struct/gccontrollerdidstopbeingcurrent.md)
  A notification that posts when a controller stops being the current controller.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](./name-swift.struct/gccontrollerusercustomizationsdidchange.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.
- [static let GCKeyboardDidConnect: NSNotification.Name](./name-swift.struct/gckeyboarddidconnect.md)
  A notification that posts after a keyboard connects to the device.
- [static let GCKeyboardDidDisconnect: NSNotification.Name](./name-swift.struct/gckeyboarddiddisconnect.md)
  A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.
- [static let GCMouseDidBecomeCurrent: NSNotification.Name](./name-swift.struct/gcmousedidbecomecurrent.md)
  A notification that posts when a mouse becomes the most recent mouse that the user connects.
- [static let GCMouseDidConnect: NSNotification.Name](./name-swift.struct/gcmousedidconnect.md)
  A notification that posts after a mouse connects to the device.
- [static let GCMouseDidDisconnect: NSNotification.Name](./name-swift.struct/gcmousediddisconnect.md)
  A notification that posts after a mouse disconnects from the device.
- [static let GCMouseDidStopBeingCurrent: NSNotification.Name](./name-swift.struct/gcmousedidstopbeingcurrent.md)
  A notification that posts when a mouse stops being the most recent mouse that the user connects.
- [static let GCRacingWheelDidConnect: NSNotification.Name](./name-swift.struct/gcracingwheeldidconnect.md)
  A notification that posts after a racing wheel controller connects to the device.
- [static let GCRacingWheelDidDisconnect: NSNotification.Name](./name-swift.struct/gcracingwheeldiddisconnect.md)
  A notification that posts after a racing wheel controller disconnects from the device.
### GameKit
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](./name-swift.struct/gkplayerauthenticationdidchangenotificationname.md)
  A notification that posts after GameKit authenticates the local player.
- [static let GKPlayerDidChangeNotificationName: NSNotification.Name](./name-swift.struct/gkplayerdidchangenotificationname.md)
  A notification that posts when a player object’s data changes.
### HealthKit
- [static let HKUserPreferencesDidChange: NSNotification.Name](./name-swift.struct/hkuserpreferencesdidchange.md)
  Notifies observers whenever the user changes his or her preferred units.
### HomeKit
- [let HMCharacteristicPropertySupportsEventNotification: String](../../HomeKit/hmcharacteristicpropertysupportseventnotification-2f0ml.md)
  The characteristic supports event notifications.
### IOBluetooth
- [static let IOBluetoothHostControllerPoweredOff: NSNotification.Name](./name-swift.struct/iobluetoothhostcontrollerpoweredoff.md)
- [static let IOBluetoothHostControllerPoweredOn: NSNotification.Name](./name-swift.struct/iobluetoothhostcontrollerpoweredon.md)
- [static let IOBluetoothL2CAPChannelPublished: NSNotification.Name](./name-swift.struct/iobluetoothl2capchannelpublished.md)
- [static let IOBluetoothL2CAPChannelTerminated: NSNotification.Name](./name-swift.struct/iobluetoothl2capchannelterminated.md)
### iTunes Library
- [static let ITLibraryDidChange: NSNotification.Name](./name-swift.struct/itlibrarydidchange.md)
  A notification the system posts when a library change occurs.
### MapKit
- [static let MKAnnotationCalloutInfoDidChange: NSNotification.Name](./name-swift.struct/mkannotationcalloutinfodidchange.md)
  A property to observe to determine when the title or subtitle information of an annotation object changes.
### MediaPlayer
- [static let MPMusicPlayerControllerQueueDidChange: NSNotification.Name](./name-swift.struct/mpmusicplayercontrollerqueuedidchange.md)
  Indicates the music player’s queue changed.
- [static let MPMediaLibraryDidChange: NSNotification.Name](./name-swift.struct/mpmedialibrarydidchange.md)
  Indicates the media library has changed.
- [static let MPMediaPlaybackIsPreparedToPlayDidChange: NSNotification.Name](./name-swift.struct/mpmediaplaybackispreparedtoplaydidchange.md)
  Indicates that the prepared to play status of the media player has changed.
- [static let MPMusicPlayerControllerNowPlayingItemDidChange: NSNotification.Name](./name-swift.struct/mpmusicplayercontrollernowplayingitemdidchange.md)
  Posted when the currently playing media item has changed.
- [static let MPMusicPlayerControllerPlaybackStateDidChange: NSNotification.Name](./name-swift.struct/mpmusicplayercontrollerplaybackstatedidchange.md)
  Posted when the playback state changes programmatically or by user action.
- [static let MPMusicPlayerControllerVolumeDidChange: NSNotification.Name](./name-swift.struct/mpmusicplayercontrollervolumedidchange.md)
  Posted when the audio playback volume for the music player has changed.
- [static let MPMovieDurationAvailable: NSNotification.Name](./name-swift.struct/mpmoviedurationavailable.md)
  Posted when the duration of a movie has been determined. There is no `userInfo` dictionary.
- [static let MPMovieMediaTypesAvailable: NSNotification.Name](./name-swift.struct/mpmoviemediatypesavailable.md)
  Posted when the available media types in a movie are determined. There is no `userInfo` dictionary.
- [static let MPMovieNaturalSizeAvailable: NSNotification.Name](./name-swift.struct/mpmovienaturalsizeavailable.md)
  Posted when the natural frame size of a movie is first determined or subsequently changes. There is no `userInfo` dictionary.
- [static let MPMoviePlayerDidEnterFullscreen: NSNotification.Name](./name-swift.struct/mpmovieplayerdidenterfullscreen.md)
  Posted when a movie player has entered full-screen mode. There is no `userInfo` dictionary.
- [static let MPMoviePlayerDidExitFullscreen: NSNotification.Name](./name-swift.struct/mpmovieplayerdidexitfullscreen.md)
  Posted when a movie player has exited full-screen mode. There is no `userInfo` dictionary.
- [static let MPMoviePlayerIsAirPlayVideoActiveDidChange: NSNotification.Name](./name-swift.struct/mpmovieplayerisairplayvideoactivedidchange.md)
  Posted when a movie player has started or ended playing a movie via AirPlay. There is no `userInfo` dictionary.
- [static let MPMoviePlayerLoadStateDidChange: NSNotification.Name](./name-swift.struct/mpmovieplayerloadstatedidchange.md)
  Posted when a movie player’s network buffering state has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerNowPlayingMovieDidChange: NSNotification.Name](./name-swift.struct/mpmovieplayernowplayingmoviedidchange.md)
  Posted when the currently playing movie has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerPlaybackDidFinish: NSNotification.Name](./name-swift.struct/mpmovieplayerplaybackdidfinish.md)
  Posted when a movie has finished playing.
- [static let MPMoviePlayerPlaybackStateDidChange: NSNotification.Name](./name-swift.struct/mpmovieplayerplaybackstatedidchange.md)
  Posted when a movie player’s playback state has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerReadyForDisplayDidChange: NSNotification.Name](./name-swift.struct/mpmovieplayerreadyfordisplaydidchange.md)
  Posted when the ready for display state changes.
- [static let MPMoviePlayerScalingModeDidChange: NSNotification.Name](./name-swift.struct/mpmovieplayerscalingmodedidchange.md)
  Posted when the scaling mode of a movie player has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerThumbnailImageRequestDidFinish: NSNotification.Name](./name-swift.struct/mpmovieplayerthumbnailimagerequestdidfinish.md)
  Posted when a request to capture a thumbnail from a movie has finished whether the request succeeded or failed. Upon successful capture of a thumbnail, the `userInfo` dictionary contains values for the following keys:
- [static let MPMoviePlayerTimedMetadataUpdated: NSNotification.Name](./name-swift.struct/mpmovieplayertimedmetadataupdated.md)
  Posted when new timed metadata arrives.
- [static let MPMoviePlayerWillEnterFullscreen: NSNotification.Name](./name-swift.struct/mpmovieplayerwillenterfullscreen.md)
  Posted when a movie player is about to enter full-screen mode.
- [static let MPMoviePlayerWillExitFullscreen: NSNotification.Name](./name-swift.struct/mpmovieplayerwillexitfullscreen.md)
  Posted when a movie player is about to exit full-screen mode.
- [static let MPMovieSourceTypeAvailable: NSNotification.Name](./name-swift.struct/mpmoviesourcetypeavailable.md)
  Posted when the source type of a movie was previously unknown and is newly available. There is no `userInfo` dictionary.
- [static let MPVolumeViewWirelessRouteActiveDidChange: NSNotification.Name](./name-swift.struct/mpvolumeviewwirelessrouteactivedidchange.md)
  Indicates the active wireless route changed.
- [static let MPVolumeViewWirelessRoutesAvailableDidChange: NSNotification.Name](./name-swift.struct/mpvolumeviewwirelessroutesavailabledidchange.md)
  Indicates the available wireless routes changed.
### MessageUI
- [static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name](./name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.md)
  Posted when the current device’s ability to send text messages changes.
- [static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name](./name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.md)
  Posted when the current device’s ability to send text messages changes.
### NetworkExtension
- [static let NEFilterConfigurationDidChange: NSNotification.Name](./name-swift.struct/nefilterconfigurationdidchange.md)
  Posted after the filter configuration stored in the Network Extension preferences changes.
- [static let NEVPNConfigurationChange: NSNotification.Name](./name-swift.struct/nevpnconfigurationchange.md)
  Posted after the VPN configuration stored in the Network Extension preferences changes.
- [static let NEVPNStatusDidChange: NSNotification.Name](./name-swift.struct/nevpnstatusdidchange.md)
  Posted when the status of the VPN connection changes.
- [static let NEDNSProxyConfigurationDidChange: NSNotification.Name](./name-swift.struct/nednsproxyconfigurationdidchange.md)
  A notification that is posted when the DNS proxy configuration changes.
- [static let NEDNSSettingsConfigurationDidChange: NSNotification.Name](./name-swift.struct/nednssettingsconfigurationdidchange.md)
### PassKit
- [static let PKPassLibraryDidChange: PKPassLibraryNotificationName](../../PassKit/pkpasslibrarynotificationname/pkpasslibrarydidchange.md)
  A notification that PassKit posts when the pass library changes.
- [static let PKPassLibraryRemotePaymentPassesDidChange: PKPassLibraryNotificationName](../../PassKit/pkpasslibrarynotificationname/pkpasslibraryremotepaymentpassesdidchange.md)
  A notification that PassKit posts when it adds or removes a pass on a paired remote device.
### PDFKit
- [static let PDFDocumentDidBeginFind: NSNotification.Name](./name-swift.struct/pdfdocumentdidbeginfind.md)
  A notification that the document began a find operation.
- [static let PDFDocumentDidBeginPageFind: NSNotification.Name](./name-swift.struct/pdfdocumentdidbeginpagefind.md)
  A notification that a find operation begins working on a new page of a document.
- [static let PDFDocumentDidBeginPageWrite: NSNotification.Name](./name-swift.struct/pdfdocumentdidbeginpagewrite.md)
  A notification that a write operation begins working on a page in a document.
- [static let PDFDocumentDidBeginWrite: NSNotification.Name](./name-swift.struct/pdfdocumentdidbeginwrite.md)
  A notification that a write operation begins working on a document.
- [static let PDFDocumentDidEndFind: NSNotification.Name](./name-swift.struct/pdfdocumentdidendfind.md)
  A notification that the document finished a find operation.
- [static let PDFDocumentDidEndPageFind: NSNotification.Name](./name-swift.struct/pdfdocumentdidendpagefind.md)
  A notification that a find operation finishes working on a page in a document.
- [static let PDFDocumentDidEndPageWrite: NSNotification.Name](./name-swift.struct/pdfdocumentdidendpagewrite.md)
  A notification that a write operation finishes working on a page in a document.
- [static let PDFDocumentDidEndWrite: NSNotification.Name](./name-swift.struct/pdfdocumentdidendwrite.md)
  A notification that a write operation finishes working on a document.
- [static let PDFDocumentDidFindMatch: NSNotification.Name](./name-swift.struct/pdfdocumentdidfindmatch.md)
  A notification that a string match is found in a document.
- [static let PDFDocumentDidUnlock: NSNotification.Name](./name-swift.struct/pdfdocumentdidunlock.md)
  A notification that a document unlocked.
- [static let PDFThumbnailViewDocumentEdited: NSNotification.Name](./name-swift.struct/pdfthumbnailviewdocumentedited.md)
- [static let PDFViewAnnotationHit: NSNotification.Name](./name-swift.struct/pdfviewannotationhit.md)
  A notification posted when the user clicks on an annotation.
- [static let PDFViewAnnotationWillHit: NSNotification.Name](./name-swift.struct/pdfviewannotationwillhit.md)
  A notification posted before the user clicks an annotation.
- [static let PDFViewChangedHistory: NSNotification.Name](./name-swift.struct/pdfviewchangedhistory.md)
  A notification posted when the page history changes.
- [static let PDFViewCopyPermission: NSNotification.Name](./name-swift.struct/pdfviewcopypermission.md)
  A notification posted when the user attempts to copy to the pasteboard without the appropriate permissions.
- [static let PDFViewDisplayBoxChanged: NSNotification.Name](./name-swift.struct/pdfviewdisplayboxchanged.md)
  A notification posted when the display box has changed.
- [static let PDFViewDisplayModeChanged: NSNotification.Name](./name-swift.struct/pdfviewdisplaymodechanged.md)
  A notification posted when the display mode has changed.
- [static let PDFViewDocumentChanged: NSNotification.Name](./name-swift.struct/pdfviewdocumentchanged.md)
  A notification posted when a new document is associated with the view.
- [static let PDFViewPageChanged: NSNotification.Name](./name-swift.struct/pdfviewpagechanged.md)
  A notification posted when a new page becomes the current page.
- [static let PDFViewPrintPermission: NSNotification.Name](./name-swift.struct/pdfviewprintpermission.md)
  A notification posted when the user attempts to print without the appropriate permissions.
- [static let PDFViewScaleChanged: NSNotification.Name](./name-swift.struct/pdfviewscalechanged.md)
  A notification posted when the scale factor changes.
- [static let PDFViewSelectionChanged: NSNotification.Name](./name-swift.struct/pdfviewselectionchanged.md)
  A notification posted when the current selection has changed.
- [static let PDFViewVisiblePagesChanged: NSNotification.Name](./name-swift.struct/pdfviewvisiblepageschanged.md)
  A notification posted when the visible pages have changed.
### PreferencePanes
- [static let NSPreferencePaneCancelUnselect: NSNotification.Name](./name-swift.struct/nspreferencepanecancelunselect.md)
  Notifies observers that the preference pane should not be deselected.
- [static let NSPreferencePaneDoUnselect: NSNotification.Name](./name-swift.struct/nspreferencepanedounselect.md)
  Notifies observers that the preference pane may be deselected.
- [static let NSPreferencePaneSwitchToPane: NSNotification.Name](./name-swift.struct/nspreferencepaneswitchtopane.md)
  Notifies observers that the user selected a new preference pane.
- [static let NSPreferencePaneUpdateHelpMenu: NSNotification.Name](./name-swift.struct/nspreferencepaneupdatehelpmenu.md)
  Notifies observers that your help menu content changed.
- [static let NSPreferencePrefPaneIsAvailable: NSNotification.Name](./name-swift.struct/nspreferenceprefpaneisavailable.md)
  Notifies observers that the system preferences app is available to display your preferences.
### Quartz
- [static let IKFilterBrowserFilterDoubleClick: NSNotification.Name](./name-swift.struct/ikfilterbrowserfilterdoubleclick.md)
  Posted when the user double-clicks a filter in the filter browser.
- [static let IKFilterBrowserFilterSelected: NSNotification.Name](./name-swift.struct/ikfilterbrowserfilterselected.md)
  Posted when the user clicks a filter name in the filter browser.
- [static let IKFilterBrowserWillPreviewFilter: NSNotification.Name](./name-swift.struct/ikfilterbrowserwillpreviewfilter.md)
  Posted before showing a filter preview, allowing an application to set the parameters of a filter.
- [static let quartzFilterManagerDidAddFilter: NSNotification.Name](./name-swift.struct/quartzfiltermanagerdidaddfilter.md)
- [static let quartzFilterManagerDidModifyFilter: NSNotification.Name](./name-swift.struct/quartzfiltermanagerdidmodifyfilter.md)
- [static let quartzFilterManagerDidRemoveFilter: NSNotification.Name](./name-swift.struct/quartzfiltermanagerdidremovefilter.md)
- [static let quartzFilterManagerDidSelectFilter: NSNotification.Name](./name-swift.struct/quartzfiltermanagerdidselectfilter.md)
- [static let QCCompositionPickerPanelDidSelectComposition: NSNotification.Name](./name-swift.struct/qccompositionpickerpaneldidselectcomposition.md)
  Posted when the user chooses a composition.
- [static let QCCompositionPickerViewDidSelectComposition: NSNotification.Name](./name-swift.struct/qccompositionpickerviewdidselectcomposition.md)
  Posted when the user selects a composition in the picker view.
- [static let QCCompositionRepositoryDidUpdate: NSNotification.Name](./name-swift.struct/qccompositionrepositorydidupdate.md)
  Posted whenever the list of compositions in the composition repository is updated.
- [static let QCViewDidStartRendering: NSNotification.Name](./name-swift.struct/qcviewdidstartrendering.md)
  Posted when the view starts rendering.
- [static let QCViewDidStopRendering: NSNotification.Name](./name-swift.struct/qcviewdidstoprendering.md)
  Posted when the view stops rendering.
### StoreKit
- [static let SKCloudServiceCapabilitiesDidChange: NSNotification.Name](./name-swift.struct/skcloudservicecapabilitiesdidchange.md)
  A notification name for indicating a change in the capabilities associated with the Music library on the device.
- [static let SKStorefrontIdentifierDidChange: NSNotification.Name](./name-swift.struct/skstorefrontidentifierdidchange.md)
  A notification name for indicating a change in the storefront identifier associated with the device.
- [static let SKStorefrontCountryCodeDidChange: NSNotification.Name](./name-swift.struct/skstorefrontcountrycodedidchange.md)
  A notification name for indicating a change in the storefront country or region code associated with the device.
### TV Services
- [static let TVTopShelfItemsDidChange: NSNotification.Name](./name-swift.struct/tvtopshelfitemsdidchange.md)
  A notification to post when your app’s Top Shelf content has changed.
### UIKit
- [static let announcementDidFinishNotification: NSNotification.Name](../../UIKit/uiaccessibility/announcementdidfinishnotification.md)
  A notification that UIKit posts when the system finishes reading an announcement.
- [static let elementFocusedNotification: NSNotification.Name](../../UIKit/uiaccessibility/elementfocusednotification.md)
  A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [static let assistiveTouchStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/assistivetouchstatusdidchangenotification.md)
  A notification that indicates a change in the status of AssistiveTouch.
- [static let boldTextStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/boldtextstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Bold Text setting changes.
- [static let closedCaptioningStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/closedcaptioningstatusdidchangenotification.md)
  A notification that UIKit posts when the setting for Closed Captions + SDH changes.
- [static let darkerSystemColorsStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/darkersystemcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [static let grayscaleStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/grayscalestatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Grayscale setting changes.
- [static let guidedAccessStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/guidedaccessstatusdidchangenotification.md)
  A notification that indicates when a Guided Access session starts or ends.
- [static let hearingDevicePairedEarDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/hearingdevicepairedeardidchangenotification.md)
  A notification that UIKit posts when there’s a change to the currently paired hearing devices.
- [static let invertColorsStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/invertcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the settings for inverted colors change.
- [static let monoAudioStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/monoaudiostatusdidchangenotification.md)
  A notification that UIKit posts when system audio changes from stereo to mono.
- [static let reduceMotionStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/reducemotionstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Motion setting changes.
- [static let reduceTransparencyStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/reducetransparencystatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [static let shakeToUndoDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/shaketoundodidchangenotification.md)
  A notification that UIKit posts when the system’s Shake to Undo setting changes.
- [static let speakScreenStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/speakscreenstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Screen setting changes.
- [static let speakSelectionStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/speakselectionstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Selection setting changes.
- [static let switchControlStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiaccessibility/switchcontrolstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Switch Control setting changes.
- [class let didBecomeActiveNotification: NSNotification.Name](../../UIKit/uiapplication/didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](../../UIKit/uiapplication/didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let didFinishLaunchingNotification: NSNotification.Name](../../UIKit/uiapplication/didfinishlaunchingnotification.md)
  A notification that posts immediately after the app finishes launching.
- [class let didReceiveMemoryWarningNotification: NSNotification.Name](../../UIKit/uiapplication/didreceivememorywarningnotification.md)
  A notification that posts when the app receives a warning from the operating system about low memory availability.
- [class let significantTimeChangeNotification: NSNotification.Name](../../UIKit/uiapplication/significanttimechangenotification.md)
  A notification that posts when there’s a significant change in time.
- [class let userDidTakeScreenshotNotification: NSNotification.Name](../../UIKit/uiapplication/userdidtakescreenshotnotification.md)
  A notification that posts when a person takes a screenshot on the device.
- [class let willEnterForegroundNotification: NSNotification.Name](../../UIKit/uiapplication/willenterforegroundnotification.md)
  A notification that posts shortly before your app’s UI transitions to the foreground.
- [class let willResignActiveNotification: NSNotification.Name](../../UIKit/uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](../../UIKit/uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.
- [static let didChangeNotification: NSNotification.Name](../../UIKit/uicontentsizecategory/didchangenotification.md)
  A notification that posts when the user changes the preferred content size setting.
- [class let proximityStateDidChangeNotification: NSNotification.Name](../../UIKit/uidevice/proximitystatedidchangenotification.md)
  A notification that posts when the state of the proximity sensor changes.
- [class let brightnessDidChangeNotification: NSNotification.Name](../../UIKit/uiscreen/brightnessdidchangenotification.md)
  A notification that posts when a screen’s brightness changes.
- [class let didConnectNotification: NSNotification.Name](../../UIKit/uiscreen/didconnectnotification.md)
  A notification the system posts when a new screen connects to the device.
- [class let didDisconnectNotification: NSNotification.Name](../../UIKit/uiscreen/diddisconnectnotification.md)
  A notification the system posts when a screen disconnects from the device.
- [class let modeDidChangeNotification: NSNotification.Name](../../UIKit/uiscreen/modedidchangenotification.md)
  A notification that posts when a screen’s mode changes.
- [class let selectionDidChangeNotification: NSNotification.Name](../../UIKit/uitableview/selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.
- [class let textDidBeginEditingNotification: NSNotification.Name](../../UIKit/uitextfield/textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text field.
- [class let textDidChangeNotification: NSNotification.Name](../../UIKit/uitextfield/textdidchangenotification.md)
  A notification that alerts observers when the text in a text field changes.
- [class let textDidEndEditingNotification: NSNotification.Name](../../UIKit/uitextfield/textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text field.
- [class let currentInputModeDidChangeNotification: NSNotification.Name](../../UIKit/uitextinputmode/currentinputmodedidchangenotification.md)
  A notification that posts when the current input mode changes.
- [class let textDidBeginEditingNotification: NSNotification.Name](../../UIKit/uitextview/textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text view.
- [class let textDidChangeNotification: NSNotification.Name](../../UIKit/uitextview/textdidchangenotification.md)
  A notification that alerts observers when the text in a text view changes.
- [class let textDidEndEditingNotification: NSNotification.Name](../../UIKit/uitextview/textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text view.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](../../UIKit/uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.
- [class let didBecomeHiddenNotification: NSNotification.Name](../../UIKit/uiwindow/didbecomehiddennotification.md)
  A notification that posts when a window becomes hidden.
- [class let didBecomeKeyNotification: NSNotification.Name](../../UIKit/uiwindow/didbecomekeynotification.md)
  A notification that posts whenever a window becomes the key window.
- [class let didBecomeVisibleNotification: NSNotification.Name](../../UIKit/uiwindow/didbecomevisiblenotification.md)
  A notification that posts when a window becomes visible.
- [class let didResignKeyNotification: NSNotification.Name](../../UIKit/uiwindow/didresignkeynotification.md)
  A notification that posts whenever a window resigns its status as main window.
- [class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name](../../UIKit/uiapplication/backgroundrefreshstatusdidchangenotification.md)
  A notification that posts when the app’s status for downloading content in the background changes.
- [class let didChangeStatusBarFrameNotification: NSNotification.Name](../../UIKit/uiapplication/didchangestatusbarframenotification.md)
  Posted when the frame of the status bar changes.
- [class let didChangeStatusBarOrientationNotification: NSNotification.Name](../../UIKit/uiapplication/didchangestatusbarorientationnotification.md)
  Posted when the orientation of the app’s user interface changes.
- [class let willChangeStatusBarFrameNotification: NSNotification.Name](../../UIKit/uiapplication/willchangestatusbarframenotification.md)
  Posted when the app is about to change the frame of the status bar.
- [class let willChangeStatusBarOrientationNotification: NSNotification.Name](../../UIKit/uiapplication/willchangestatusbarorientationnotification.md)
  Posted when the app is about to change the orientation of its interface.
- [class let batteryLevelDidChangeNotification: NSNotification.Name](../../UIKit/uidevice/batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let batteryStateDidChangeNotification: NSNotification.Name](../../UIKit/uidevice/batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
- [class let orientationDidChangeNotification: NSNotification.Name](../../UIKit/uidevice/orientationdidchangenotification.md)
  A notification that posts when the orientation of the device changes.
- [class let stateChangedNotification: NSNotification.Name](../../UIKit/uidocument/statechangednotification.md)
  A notification the document object posts when there’s a change in the state of the document.
- [class let keyboardDidChangeFrameNotification: NSNotification.Name](../../UIKit/uiresponder/keyboarddidchangeframenotification.md)
  A notification that posts immediately after a change in the keyboard’s frame.
- [class let keyboardDidHideNotification: NSNotification.Name](../../UIKit/uiresponder/keyboarddidhidenotification.md)
  A notification that posts immediately after dismissing the keyboard.
- [class let keyboardDidShowNotification: NSNotification.Name](../../UIKit/uiresponder/keyboarddidshownotification.md)
  A notification that posts immediately after displaying the keyboard.
- [class let keyboardWillChangeFrameNotification: NSNotification.Name](../../UIKit/uiresponder/keyboardwillchangeframenotification.md)
  A notification that posts immediately prior to a change in the keyboard’s frame.
- [class let keyboardWillHideNotification: NSNotification.Name](../../UIKit/uiresponder/keyboardwillhidenotification.md)
  A notification that posts immediately prior to dismissing the keyboard.
- [class let keyboardWillShowNotification: NSNotification.Name](../../UIKit/uiresponder/keyboardwillshownotification.md)
  A notification that posts immediately prior to displaying the keyboard.
- [class let didHideMenuNotification: NSNotification.Name](../../UIKit/uimenucontroller/didhidemenunotification.md)
  Posted by the menu controller just after it hides the menu.
- [class let didShowMenuNotification: NSNotification.Name](../../UIKit/uimenucontroller/didshowmenunotification.md)
  Posted by the menu controller just after it shows the menu.
- [class let menuFrameDidChangeNotification: NSNotification.Name](../../UIKit/uimenucontroller/menuframedidchangenotification.md)
  Posted when the frame of a visible menu changes.
- [class let willHideMenuNotification: NSNotification.Name](../../UIKit/uimenucontroller/willhidemenunotification.md)
  Posted by the menu controller just before it hides the menu.
- [class let willShowMenuNotification: NSNotification.Name](../../UIKit/uimenucontroller/willshowmenunotification.md)
  Posted by the menu controller just before it shows the menu.
- [class let changedNotification: NSNotification.Name](../../UIKit/uipasteboard/changednotification.md)
  A notification that a pasteboard object posts when its contents change.
- [class let removedNotification: NSNotification.Name](../../UIKit/uipasteboard/removednotification.md)
  A notification that a pasteboard object posts just before an app removes it.
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](../../UIKit/uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](../../UIKit/uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.
### WatchKit
- [static let WKAccessibilityReduceMotionStatusDidChange: NSNotification.Name](./name-swift.struct/wkaccessibilityreducemotionstatusdidchange.md)
  Tells the interface controller that the reduce motion status has changed.
- [static let WKAudioFilePlayerItemDidPlayToEndTime: NSNotification.Name](./name-swift.struct/wkaudiofileplayeritemdidplaytoendtime.md)
  A notification that the item has played successfully to its end.
- [static let WKAudioFilePlayerItemFailedToPlayToEndTime: NSNotification.Name](./name-swift.struct/wkaudiofileplayeritemfailedtoplaytoendtime.md)
  A notification that the item failed to play to its end.
- [static let WKAudioFilePlayerItemTimeJumped: NSNotification.Name](./name-swift.struct/wkaudiofileplayeritemtimejumped.md)
  A notification that the item’s current time has changed discontinuously.
### WebKit
- [static let WebHistoryAllItemsRemoved: NSNotification.Name](./name-swift.struct/webhistoryallitemsremoved.md)
  Posted when all history items have been removed from the web history.
- [static let WebHistoryItemChanged: NSNotification.Name](./name-swift.struct/webhistoryitemchanged.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [static let WebHistoryItemsAdded: NSNotification.Name](./name-swift.struct/webhistoryitemsadded.md)
  Posted when history items have been added to a web history.
- [static let WebHistoryItemsRemoved: NSNotification.Name](./name-swift.struct/webhistoryitemsremoved.md)
  Posted when items have been removed from the web history.
- [static let WebHistoryLoaded: NSNotification.Name](./name-swift.struct/webhistoryloaded.md)
  Posted when web history items have been loaded from a URL.
- [static let WebHistorySaved: NSNotification.Name](./name-swift.struct/webhistorysaved.md)
  Posted when web history items have been saved to a URL.
- [static let WebPreferencesChanged: NSNotification.Name](./name-swift.struct/webpreferenceschanged.md)
  Posted when the web preference settings are changed.
- [static let WebViewDidBeginEditing: NSNotification.Name](./name-swift.struct/webviewdidbeginediting.md)
  Posted when a web view begins any operation that changes its contents in response to user editing.
- [static let WebViewDidChange: NSNotification.Name](./name-swift.struct/webviewdidchange.md)
  Posted when a web view performs any operation that changes its contents in response to user editing.
- [static let WebViewDidChangeSelection: NSNotification.Name](./name-swift.struct/webviewdidchangeselection.md)
  Posted when a web view changes its typing selection.
- [static let WebViewDidChangeTypingStyle: NSNotification.Name](./name-swift.struct/webviewdidchangetypingstyle.md)
  Posted when a web view changes its typing style.
- [static let WebViewDidEndEditing: NSNotification.Name](./name-swift.struct/webviewdidendediting.md)
  Posted when a web view ends any operation that changes its contents in response to user editing.
- [static let WebViewProgressEstimateChanged: NSNotification.Name](./name-swift.struct/webviewprogressestimatechanged.md)
  Posted by a WebView object when the estimated progress value of a load changes.
- [static let WebViewProgressFinished: NSNotification.Name](./name-swift.struct/webviewprogressfinished.md)
  Posted by a WebView object when the load has finished.
- [static let WebViewProgressStarted: NSNotification.Name](./name-swift.struct/webviewprogressstarted.md)
  Posted by a WebView object when a load begins, including a load that is initiated in a subframe.
### Accounts
- [static let ACAccountStoreDidChange: NSNotification.Name](./name-swift.struct/acaccountstoredidchange.md)
  Posted when the accounts managed by this account store changed in the database.
### Initializers
- [init(String)](./name-swift.struct/init%28_%29.md)
- [init(rawValue: String)](./name-swift.struct/init%28rawvalue%29.md)
### Type Properties
- [static var AVCaptureDeviceSubjectAreaDidChange: NSNotification.Name](./name-swift.struct/avcapturedevicesubjectareadidchange.md)
- [static var AVCaptureDeviceWasConnected: NSNotification.Name](./name-swift.struct/avcapturedevicewasconnected.md)
- [static var AVCaptureDeviceWasDisconnected: NSNotification.Name](./name-swift.struct/avcapturedevicewasdisconnected.md)
- [static var AVCaptureInputPortFormatDescriptionDidChange: NSNotification.Name](./name-swift.struct/avcaptureinputportformatdescriptiondidchange.md)
- [static var AVCaptureSessionDidStartRunning: NSNotification.Name](./name-swift.struct/avcapturesessiondidstartrunning.md)
- [static var AVCaptureSessionDidStopRunning: NSNotification.Name](./name-swift.struct/avcapturesessiondidstoprunning.md)
- [static var AVCaptureSessionInterruptionEnded: NSNotification.Name](./name-swift.struct/avcapturesessioninterruptionended.md)
- [static var AVCaptureSessionRuntimeError: NSNotification.Name](./name-swift.struct/avcapturesessionruntimeerror.md)
- [static var AVCaptureSessionWasInterrupted: NSNotification.Name](./name-swift.struct/avcapturesessionwasinterrupted.md)
- [static var AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChange: NSNotification.Name](./name-swift.struct/avplayerinterstitialeventmonitorassetlistresponsestatusdidchange.md)
- [static let AVPlayerInterstitialEventMonitorScheduleRequestCompleted: NSNotification.Name](./name-swift.struct/avplayerinterstitialeventmonitorschedulerequestcompleted.md)
- [static var AVPlayerItemDidPlayToEndTime: NSNotification.Name](./name-swift.struct/avplayeritemdidplaytoendtime.md)
- [static var AVPlayerItemFailedToPlayToEndTime: NSNotification.Name](./name-swift.struct/avplayeritemfailedtoplaytoendtime.md)
- [static var AVPlayerItemNewAccessLogEntry: NSNotification.Name](./name-swift.struct/avplayeritemnewaccesslogentry.md)
- [static var AVPlayerItemNewErrorLogEntry: NSNotification.Name](./name-swift.struct/avplayeritemnewerrorlogentry.md)
- [static var AVPlayerItemPlaybackStalled: NSNotification.Name](./name-swift.struct/avplayeritemplaybackstalled.md)
- [static let AVSampleBufferDisplayLayerReadyForDisplayDidChange: NSNotification.Name](./name-swift.struct/avsamplebufferdisplaylayerreadyfordisplaydidchange.md)
- [static var AXAnimatedImagesEnabledDidChange: NSNotification.Name](./name-swift.struct/axanimatedimagesenableddidchange.md)
- [static var AXPrefersHeadAnchorAlternativeDidChange: NSNotification.Name](./name-swift.struct/axprefersheadanchoralternativedidchange.md)
- [static var AXPrefersHorizontalTextLayoutDidChange: NSNotification.Name](./name-swift.struct/axprefershorizontaltextlayoutdidchange.md)
- [static let DRBurnProgressPanelDidFinish: NSNotification.Name](./name-swift.struct/drburnprogresspaneldidfinish.md)
- [static let DRBurnProgressPanelWillBegin: NSNotification.Name](./name-swift.struct/drburnprogresspanelwillbegin.md)
- [static let DRBurnStatusChanged: NSNotification.Name](./name-swift.struct/drburnstatuschanged.md)
- [static let DRDeviceAppeared: NSNotification.Name](./name-swift.struct/drdeviceappeared.md)
- [static let DRDeviceDisappeared: NSNotification.Name](./name-swift.struct/drdevicedisappeared.md)
- [static let DRDeviceStatusChanged: NSNotification.Name](./name-swift.struct/drdevicestatuschanged.md)
- [static let DREraseProgressPanelDidFinish: NSNotification.Name](./name-swift.struct/dreraseprogresspaneldidfinish.md)
- [static let DREraseProgressPanelWillBegin: NSNotification.Name](./name-swift.struct/dreraseprogresspanelwillbegin.md)
- [static let DREraseStatusChanged: NSNotification.Name](./name-swift.struct/drerasestatuschanged.md)
- [static let DRSetupPanelDeviceSelectionChanged: NSNotification.Name](./name-swift.struct/drsetuppaneldeviceselectionchanged.md)
- [static let GCSpatialAccessoryDidConnect: NSNotification.Name](./name-swift.struct/gcspatialaccessorydidconnect.md)
- [static let GCSpatialAccessoryDidDisconnect: NSNotification.Name](./name-swift.struct/gcspatialaccessorydiddisconnect.md)
- [static let GCStylusDidConnect: NSNotification.Name](./name-swift.struct/gcstylusdidconnect.md)
- [static let GCStylusDidDisconnect: NSNotification.Name](./name-swift.struct/gcstylusdiddisconnect.md)
- [static let HMCharacteristicPropertySupportsEvent: NSNotification.Name](./name-swift.struct/hmcharacteristicpropertysupportsevent.md)
- [static let MEVideoDecoderReadyForMoreMediaDataDidChange: NSNotification.Name](./name-swift.struct/mevideodecoderreadyformoremediadatadidchange.md)
- [static let NERelayConfigurationDidChange: NSNotification.Name](./name-swift.struct/nerelayconfigurationdidchange.md)
- [static let NEURLFilterConfigurationDidChange: Notification.Name](./name-swift.struct/neurlfilterconfigurationdidchange.md)
  Name of the NSNotification that is posted when the URL filter configuration changes.
- [static let NEURLFilterStatusDidChange: Notification.Name](./name-swift.struct/neurlfilterstatusdidchange.md)
  Name of the NSNotification that is posted when the URL filter status changes.
- [static let NSApplicationShouldBeginSuppressingHighDynamicRangeContent: NSNotification.Name](./name-swift.struct/nsapplicationshouldbeginsuppressinghighdynamicrangecontent.md)
- [static let NSApplicationShouldEndSuppressingHighDynamicRangeContent: NSNotification.Name](./name-swift.struct/nsapplicationshouldendsuppressinghighdynamicrangecontent.md)
- [static let NSProcessInfoPerformanceProfileDidChange: NSNotification.Name](./name-swift.struct/nsprocessinfoperformanceprofiledidchange.md)
- [static let NSSpellCheckerDidChangeAutomaticInlinePrediction: NSNotification.Name](./name-swift.struct/nsspellcheckerdidchangeautomaticinlineprediction.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating Notifications
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes a notification with the data from an unarchiver.
- [convenience init(name: NSNotification.Name, object: Any?)](./init%28name,object%29.md)
  Returns a new notification object with a specified name and object.
- [init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](./init%28name,object,userinfo%29.md)
  Initializes a notification with a specified name, object, and user information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct)*