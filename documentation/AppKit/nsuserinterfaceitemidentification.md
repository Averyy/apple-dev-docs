# NSUserInterfaceItemIdentification

**Framework**: AppKit  
**Kind**: protocol

A set of methods used to associate a unique identifier with objects in your user interface.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSUserInterfaceItemIdentification
```

#### Overview

The protocol is adopted by AppKit interface objects to support window restoration, whereby information about window and other interface-related objects is preserved and used to restore the application’s interface during the next launch cycle.

## Topics

### Accessing the User Interface Identifier
- [var identifier: NSUserInterfaceItemIdentifier?](nsuserinterfaceitemidentification/identifier.md)
  A string that identifies the user interface item.
- [struct NSUserInterfaceItemIdentifier](nsuserinterfaceitemidentifier.md)

## Relationships

### Inherited By
- [NSCollectionViewElement](nscollectionviewelement.md)
- [NSCollectionViewSectionHeaderView](nscollectionviewsectionheaderview.md)
### Conforming Types
- [NSActionCell](nsactioncell.md)
- [NSBox](nsbox.md)
- [NSBrowser](nsbrowser.md)
- [NSBrowserCell](nsbrowsercell.md)
- [NSButton](nsbutton.md)
- [NSButtonCell](nsbuttoncell.md)
- [NSCell](nscell.md)
- [NSClipView](nsclipview.md)
- [NSCollectionView](nscollectionview.md)
- [NSCollectionViewItem](nscollectionviewitem.md)
- [NSColorPanel](nscolorpanel.md)
- [NSColorWell](nscolorwell.md)
- [NSComboBox](nscombobox.md)
- [NSComboBoxCell](nscomboboxcell.md)
- [NSComboButton](nscombobutton.md)
- [NSControl](nscontrol.md)
- [NSDatePicker](nsdatepicker.md)
- [NSDatePickerCell](nsdatepickercell.md)
- [NSFontPanel](nsfontpanel.md)
- [NSForm](nsform.md)
- [NSFormCell](nsformcell.md)
- [NSGridView](nsgridview.md)
- [NSImageCell](nsimagecell.md)
- [NSImageView](nsimageview.md)
- [NSLayoutGuide](nslayoutguide.md)
- [NSLevelIndicator](nslevelindicator.md)
- [NSLevelIndicatorCell](nslevelindicatorcell.md)
- [NSMatrix](nsmatrix.md)
- [NSMenu](nsmenu.md)
- [NSMenuItem](nsmenuitem.md)
- [NSMenuItemCell](nsmenuitemcell.md)
- [NSOpenGLView](nsopenglview.md)
- [NSOpenPanel](nsopenpanel.md)
- [NSOutlineView](nsoutlineview.md)
- [NSPageController](nspagecontroller.md)
- [NSPanel](nspanel.md)
- [NSPathCell](nspathcell.md)
- [NSPathComponentCell](nspathcomponentcell.md)
- [NSPathControl](nspathcontrol.md)
- [NSPopUpButton](nspopupbutton.md)
- [NSPopUpButtonCell](nspopupbuttoncell.md)
- [NSPredicateEditor](nspredicateeditor.md)
- [NSProgressIndicator](nsprogressindicator.md)
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
- [NSSearchFieldCell](nssearchfieldcell.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSSecureTextFieldCell](nssecuretextfieldcell.md)
- [NSSegmentedCell](nssegmentedcell.md)
- [NSSegmentedControl](nssegmentedcontrol.md)
- [NSSlider](nsslider.md)
- [NSSliderCell](nsslidercell.md)
- [NSSplitView](nssplitview.md)
- [NSSplitViewController](nssplitviewcontroller.md)
- [NSStackView](nsstackview.md)
- [NSStatusBarButton](nsstatusbarbutton.md)
- [NSStepper](nsstepper.md)
- [NSStepperCell](nssteppercell.md)
- [NSSwitch](nsswitch.md)
- [NSTabView](nstabview.md)
- [NSTabViewController](nstabviewcontroller.md)
- [NSTableCellView](nstablecellview.md)
- [NSTableColumn](nstablecolumn.md)
- [NSTableHeaderCell](nstableheadercell.md)
- [NSTableHeaderView](nstableheaderview.md)
- [NSTableRowView](nstablerowview.md)
- [NSTableView](nstableview.md)
- [NSText](nstext.md)
- [NSTextAttachmentCell](nstextattachmentcell-swift.class.md)
- [NSTextField](nstextfield.md)
- [NSTextFieldCell](nstextfieldcell.md)
- [NSTextInsertionIndicator](nstextinsertionindicator.md)
- [NSTextView](nstextview.md)
- [NSTitlebarAccessoryViewController](nstitlebaraccessoryviewcontroller.md)
- [NSTokenField](nstokenfield.md)
- [NSTokenFieldCell](nstokenfieldcell.md)
- [NSView](nsview.md)
- [NSViewController](nsviewcontroller.md)
- [NSVisualEffectView](nsvisualeffectview.md)
- [NSWindow](nswindow.md)

## See Also

- [protocol NSWindowRestoration](nswindowrestoration.md)
  A set of methods that restoration classes must implement to handle the recreation of windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemidentification)*