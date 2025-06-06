# NSAccessibilityElementProtocol

**Framework**: Appkit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary to interact with an assistive app.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityElementProtocol : NSObjectProtocol
```

#### Overview

This protocol provides the base behavior for more specific, role-based accessibility protocols. In general, your user interface elements shouldn’t adopt this protocol. They should adopt a more specific, role-based protocol instead. See [`Custom Controls`](custom-controls.md).

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityFrame() -> NSRect](nsaccessibilityelementprotocol/accessibilityframe.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func accessibilityIdentifier() -> String](nsaccessibilityelementprotocol/accessibilityidentifier.md)
  Returns the accessibility element’s identity.
- [func accessibilityParent() -> Any?](nsaccessibilityelementprotocol/accessibilityparent.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.
- [func isAccessibilityFocused() -> Bool](nsaccessibilityelementprotocol/isaccessibilityfocused.md)
  Returns a Boolean value that indicates whether the accessibility element has the keyboard focus.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSAccessibilityButton](nsaccessibilitybutton.md)
- [NSAccessibilityCheckBox](nsaccessibilitycheckbox.md)
- [NSAccessibilityContainsTransientUI](nsaccessibilitycontainstransientui.md)
- [NSAccessibilityGroup](nsaccessibilitygroup.md)
- [NSAccessibilityImage](nsaccessibilityimage.md)
- [NSAccessibilityLayoutArea](nsaccessibilitylayoutarea.md)
- [NSAccessibilityLayoutItem](nsaccessibilitylayoutitem.md)
- [NSAccessibilityList](nsaccessibilitylist.md)
- [NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
- [NSAccessibilityOutline](nsaccessibilityoutline.md)
- [NSAccessibilityProgressIndicator](nsaccessibilityprogressindicator.md)
- [NSAccessibilityRadioButton](nsaccessibilityradiobutton.md)
- [NSAccessibilityRow](nsaccessibilityrow.md)
- [NSAccessibilitySlider](nsaccessibilityslider.md)
- [NSAccessibilityStaticText](nsaccessibilitystatictext.md)
- [NSAccessibilityStepper](nsaccessibilitystepper.md)
- [NSAccessibilitySwitch](nsaccessibilityswitch.md)
- [NSAccessibilityTable](nsaccessibilitytable.md)
### Conforming Types
- [NSActionCell](nsactioncell.md)
- [NSApplication](nsapplication.md)
- [NSBox](nsbox.md)
- [NSBrowser](nsbrowser.md)
- [NSBrowserCell](nsbrowsercell.md)
- [NSButton](nsbutton.md)
- [NSButtonCell](nsbuttoncell.md)
- [NSCell](nscell.md)
- [NSClipView](nsclipview.md)
- [NSCollectionView](nscollectionview.md)
- [NSColorPanel](nscolorpanel.md)
- [NSColorWell](nscolorwell.md)
- [NSComboBox](nscombobox.md)
- [NSComboBoxCell](nscomboboxcell.md)
- [NSComboButton](nscombobutton.md)
- [NSControl](nscontrol.md)
- [NSDatePicker](nsdatepicker.md)
- [NSDatePickerCell](nsdatepickercell.md)
- [NSDrawer](nsdrawer.md)
- [NSFontPanel](nsfontpanel.md)
- [NSForm](nsform.md)
- [NSFormCell](nsformcell.md)
- [NSGridView](nsgridview.md)
- [NSImageCell](nsimagecell.md)
- [NSImageView](nsimageview.md)
- [NSLevelIndicator](nslevelindicator.md)
- [NSLevelIndicatorCell](nslevelindicatorcell.md)
- [NSMatrix](nsmatrix.md)
- [NSMenu](nsmenu.md)
- [NSMenuItem](nsmenuitem.md)
- [NSMenuItemCell](nsmenuitemcell.md)
- [NSOpenGLView](nsopenglview.md)
- [NSOpenPanel](nsopenpanel.md)
- [NSOutlineView](nsoutlineview.md)
- [NSPanel](nspanel.md)
- [NSPathCell](nspathcell.md)
- [NSPathComponentCell](nspathcomponentcell.md)
- [NSPathControl](nspathcontrol.md)
- [NSPopUpButton](nspopupbutton.md)
- [NSPopUpButtonCell](nspopupbuttoncell.md)
- [NSPopover](nspopover.md)
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
- [NSSliderAccessory](nsslideraccessory.md)
- [NSSliderCell](nsslidercell.md)
- [NSSplitView](nssplitview.md)
- [NSStackView](nsstackview.md)
- [NSStatusBarButton](nsstatusbarbutton.md)
- [NSStepper](nsstepper.md)
- [NSStepperCell](nssteppercell.md)
- [NSSwitch](nsswitch.md)
- [NSTabView](nstabview.md)
- [NSTableCellView](nstablecellview.md)
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
- [NSTokenField](nstokenfield.md)
- [NSTokenFieldCell](nstokenfieldcell.md)
- [NSView](nsview.md)
- [NSVisualEffectView](nsvisualeffectview.md)
- [NSWindow](nswindow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nsaccessibilityelementprotocol)*