# NSAppearanceCustomization

**Framework**: AppKit  
**Kind**: protocol

A set of methods for getting and setting the appearance attributes of a view.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAppearanceCustomization : NSObjectProtocol
```

#### Overview

When an object adopts this protocol, assigning a value to the [`appearance`](nsappearancecustomization/appearance.md) property causes that object to use the appearance attributes you specified instead of any inherited attributes. You can access the current attributes for the object from the [`effectiveAppearance`](nsappearancecustomization/effectiveappearance.md) property, which reflects any inherited attributes.

## Topics

### Getting and Setting Appearance
- [Choosing a Specific Appearance for Your macOS App](choosing-a-specific-appearance-for-your-macos-app.md)
  Adopt a specific appearance for your windows, views, or app when it is inappropriate to support both light and dark variants.
- [var appearance: NSAppearance?](nsappearancecustomization/appearance.md)
  The appearance of the receiver, in an `NSAppearance` object.
- [var effectiveAppearance: NSAppearance](nsappearancecustomization/effectiveappearance.md)
  The appearance that will be used when the receiver is drawn onscreen, in an `NSAppearance` object. (read-only)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSApplication](nsapplication.md)
- [NSBackgroundExtensionView](nsbackgroundextensionview.md)
- [NSBox](nsbox.md)
- [NSBrowser](nsbrowser.md)
- [NSButton](nsbutton.md)
- [NSClipView](nsclipview.md)
- [NSCollectionView](nscollectionview.md)
- [NSColorPanel](nscolorpanel.md)
- [NSColorWell](nscolorwell.md)
- [NSComboBox](nscombobox.md)
- [NSComboButton](nscombobutton.md)
- [NSControl](nscontrol.md)
- [NSDatePicker](nsdatepicker.md)
- [NSFontPanel](nsfontpanel.md)
- [NSForm](nsform.md)
- [NSGlassEffectContainerView](nsglasseffectcontainerview.md)
- [NSGlassEffectView](nsglasseffectview.md)
- [NSGridView](nsgridview.md)
- [NSImageView](nsimageview.md)
- [NSLevelIndicator](nslevelindicator.md)
- [NSMatrix](nsmatrix.md)
- [NSMenu](nsmenu.md)
- [NSOpenGLView](nsopenglview.md)
- [NSOpenPanel](nsopenpanel.md)
- [NSOutlineView](nsoutlineview.md)
- [NSPanel](nspanel.md)
- [NSPathControl](nspathcontrol.md)
- [NSPopUpButton](nspopupbutton.md)
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
- [NSSecureTextField](nssecuretextfield.md)
- [NSSegmentedControl](nssegmentedcontrol.md)
- [NSSlider](nsslider.md)
- [NSSplitView](nssplitview.md)
- [NSStackView](nsstackview.md)
- [NSStatusBarButton](nsstatusbarbutton.md)
- [NSStepper](nsstepper.md)
- [NSSwitch](nsswitch.md)
- [NSTabView](nstabview.md)
- [NSTableCellView](nstablecellview.md)
- [NSTableHeaderView](nstableheaderview.md)
- [NSTableRowView](nstablerowview.md)
- [NSTableView](nstableview.md)
- [NSText](nstext.md)
- [NSTextField](nstextfield.md)
- [NSTextInsertionIndicator](nstextinsertionindicator.md)
- [NSTextView](nstextview.md)
- [NSTokenField](nstokenfield.md)
- [NSView](nsview.md)
- [NSVisualEffectView](nsvisualeffectview.md)
- [NSWindow](nswindow.md)

## See Also

- [class NSAppearance](nsappearance.md)
  An object that manages standard appearance attributes for UI elements in an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearancecustomization)*