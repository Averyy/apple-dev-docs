# NSTouchBarProvider

**Framework**: AppKit  
**Kind**: protocol

A protocol that an object adopts to create a bar object in your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
protocol NSTouchBarProvider : NSObjectProtocol
```

## Topics

### Providing a Touch Bar
- [var touchBar: NSTouchBar?](nstouchbarprovider/touchbar.md)
  The property you implement to provide a Touch Bar object.

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
- [NSCollectionViewItem](nscollectionviewitem.md)
- [NSColorPanel](nscolorpanel.md)
- [NSColorWell](nscolorwell.md)
- [NSComboBox](nscombobox.md)
- [NSComboButton](nscombobutton.md)
- [NSControl](nscontrol.md)
- [NSDatePicker](nsdatepicker.md)
- [NSDrawer](nsdrawer.md)
- [NSFontPanel](nsfontpanel.md)
- [NSForm](nsform.md)
- [NSGlassEffectContainerView](nsglasseffectcontainerview.md)
- [NSGlassEffectView](nsglasseffectview.md)
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
- [NSSplitViewItemAccessoryViewController](nssplitviewitemaccessoryviewcontroller.md)
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

- [Integrating a Toolbar and Touch Bar into Your App](integrating-a-toolbar-and-touch-bar-into-your-app.md)
  Provide users quick access to your app’s features from a toolbar and corresponding Touch Bar.
- [Creating and Customizing the Touch Bar](creating-and-customizing-the-touch-bar.md)
  Adopt Touch Bar support by displaying interactive content and controls for your macOS apps.
- [class NSTouchBar](nstouchbar.md)
  An object that provides dynamic contextual controls in the Touch Bar of supported models of MacBook Pro.
- [protocol NSTouchBarDelegate](nstouchbardelegate.md)
  A protocol that allows you to provide the items for a bar dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbarprovider)*