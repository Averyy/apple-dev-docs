# NSUserActivityRestoring

**Framework**: AppKit  
**Kind**: protocol

A protocol that marks classes to restore the state of your app to continue a user activity.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSUserActivityRestoring : NSObjectProtocol
```

#### Overview

Don’t conform your classes to [`NSUserActivityRestoring`](nsuseractivityrestoring.md), as it’s a marker protocol adopted by [`NSResponder`](nsresponder.md) and [`NSDocument`](nsdocument.md) for user activity state restoration.

## Topics

### Restoring App State
- [func restoreUserActivityState(NSUserActivity)](nsuseractivityrestoring/restoreuseractivitystate(_:).md)
  Restores the state necessary to continue the specified user activity.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSApplication](nsapplication.md)
- [NSBox](nsbox.md)
- [NSBrowser](nsbrowser.md)
- [NSButton](nsbutton.md)
- [NSClipView](nsclipview.md)
- [NSCollectionView](nscollectionview.md)
- [NSCollectionViewItem](nscollectionviewitem.md)
- [NSColorPanel](nscolorpanel.md)
- [NSColorWell](nscolorwell.md)
- [NSComboBox](nscombobox.md)
- [NSComboButton](nscombobutton.md)
- [NSControl](nscontrol.md)
- [NSDatePicker](nsdatepicker.md)
- [NSDocument](nsdocument.md)
- [NSDrawer](nsdrawer.md)
- [NSFontPanel](nsfontpanel.md)
- [NSForm](nsform.md)
- [NSGridView](nsgridview.md)
- [NSImageView](nsimageview.md)
- [NSLevelIndicator](nslevelindicator.md)
- [NSMatrix](nsmatrix.md)
- [NSOpenGLView](nsopenglview.md)
- [NSOpenPanel](nsopenpanel.md)
- [NSOutlineView](nsoutlineview.md)
- [NSPageController](nspagecontroller.md)
- [NSPanel](nspanel.md)
- [NSPathControl](nspathcontrol.md)
- [NSPersistentDocument](nspersistentdocument.md)
- [NSPopUpButton](nspopupbutton.md)
- [NSPopover](nspopover.md)
- [NSPredicateEditor](nspredicateeditor.md)
- [NSProgressIndicator](nsprogressindicator.md)
- [NSResponder](nsresponder.md)
- [NSRuleEditor](nsruleeditor.md)
- [NSRulerView](nsrulerview.md)
- [NSSavePanel](nssavepanel.md)
- [NSScrollView](nsscrollview.md)
- [NSScroller](nsscroller.md)
- [NSScrubber](nsscrubber.md)
- [NSScrubberArrangedView](nsscrubberarrangedview.md)
- [NSScrubberImageItemView](nsscrubberimageitemview.md)
- [NSScrubberItemView](nsscrubberitemview.md)
- [NSScrubberSelectionView](nsscrubberselectionview.md)
- [NSScrubberTextItemView](nsscrubbertextitemview.md)
- [NSSearchField](nssearchfield.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSSegmentedControl](nssegmentedcontrol.md)
- [NSSlider](nsslider.md)
- [NSSplitView](nssplitview.md)
- [NSSplitViewController](nssplitviewcontroller.md)
- [NSStackView](nsstackview.md)
- [NSStatusBarButton](nsstatusbarbutton.md)
- [NSStepper](nsstepper.md)
- [NSSwitch](nsswitch.md)
- [NSTabView](nstabview.md)
- [NSTabViewController](nstabviewcontroller.md)
- [NSTableCellView](nstablecellview.md)
- [NSTableHeaderView](nstableheaderview.md)
- [NSTableRowView](nstablerowview.md)
- [NSTableView](nstableview.md)
- [NSText](nstext.md)
- [NSTextField](nstextfield.md)
- [NSTextInsertionIndicator](nstextinsertionindicator.md)
- [NSTextView](nstextview.md)
- [NSTitlebarAccessoryViewController](nstitlebaraccessoryviewcontroller.md)
- [NSTokenField](nstokenfield.md)
- [NSView](nsview.md)
- [NSViewController](nsviewcontroller.md)
- [NSVisualEffectView](nsvisualeffectview.md)
- [NSWindow](nswindow.md)
- [NSWindowController](nswindowcontroller.md)

## See Also

- [class NSUserActivity](../Foundation/NSUserActivity.md)
  A representation of the state of your app at a moment in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuseractivityrestoring)*