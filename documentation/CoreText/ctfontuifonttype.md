# CTFontUIFontType

**Framework**: Core Text  
**Kind**: enum

Constants that represent the specific user-interface purpose to specify for font creation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CTFontUIFontType
```

#### Overview

Use these constants with the [`CTFontCreateUIFontForLanguage(_:_:_:)`](ctfontcreateuifontforlanguage(_:_:_:).md) function to indicate the intended user interface use of the font reference to be created.

## Topics

### Constants
- [CTFontUIFontType.none](ctfontuifonttype/none.md)
  The user-interface font type isn’t specified.
- [CTFontUIFontType.user](ctfontuifonttype/user.md)
  The default font for documents and other text whose font the user can typically change.
- [CTFontUIFontType.userFixedPitch](ctfontuifonttype/userfixedpitch.md)
  The default font for documents and other text under the user’s control when that font is fixed-pitch.
- [CTFontUIFontType.system](ctfontuifonttype/system.md)
  The system font for standard user-interface items, such as button labels and menu items.
- [CTFontUIFontType.emphasizedSystem](ctfontuifonttype/emphasizedsystem.md)
  The system font for emphasis in alerts.
- [CTFontUIFontType.smallSystem](ctfontuifonttype/smallsystem.md)
  The standard small system font for informative text in alerts, column headings in lists, help tags, and small controls.
- [CTFontUIFontType.smallEmphasizedSystem](ctfontuifonttype/smallemphasizedsystem.md)
  The small system font for emphasis.
- [CTFontUIFontType.miniSystem](ctfontuifonttype/minisystem.md)
  The standard miniature system font for mini controls and utility window labels and text.
- [CTFontUIFontType.miniEmphasizedSystem](ctfontuifonttype/miniemphasizedsystem.md)
  The miniature system font for emphasis.
- [CTFontUIFontType.views](ctfontuifonttype/views.md)
  The default view font for text in lists and tables.
- [CTFontUIFontType.application](ctfontuifonttype/application.md)
  The default font for text documents.
- [CTFontUIFontType.label](ctfontuifonttype/label.md)
  The font for labels and tick marks on full-size sliders.
- [CTFontUIFontType.menuTitle](ctfontuifonttype/menutitle.md)
  The font for menu titles.
- [CTFontUIFontType.menuItem](ctfontuifonttype/menuitem.md)
  The font for menu items.
- [CTFontUIFontType.menuItemMark](ctfontuifonttype/menuitemmark.md)
  The font to draw menu-item marks.
- [CTFontUIFontType.menuItemCmdKey](ctfontuifonttype/menuitemcmdkey.md)
  The font for menu-item command-key equivalents.
- [CTFontUIFontType.windowTitle](ctfontuifonttype/windowtitle.md)
  The font for window titles.
- [CTFontUIFontType.pushButton](ctfontuifonttype/pushbutton.md)
  The font for a push button, a rounded rectangular button with a text label on it.
- [CTFontUIFontType.utilityWindowTitle](ctfontuifonttype/utilitywindowtitle.md)
  The font for utility window titles.
- [CTFontUIFontType.alertHeader](ctfontuifonttype/alertheader.md)
  The font for alert headers.
- [CTFontUIFontType.systemDetail](ctfontuifonttype/systemdetail.md)
  The standard system font for details.
- [CTFontUIFontType.emphasizedSystemDetail](ctfontuifonttype/emphasizedsystemdetail.md)
  The system font for emphasis in details.
- [CTFontUIFontType.toolbar](ctfontuifonttype/toolbar.md)
  The font used for labels of toolbar items.
- [CTFontUIFontType.smallToolbar](ctfontuifonttype/smalltoolbar.md)
  The small font for labels of toolbar items.
- [CTFontUIFontType.message](ctfontuifonttype/message.md)
  The font for standard interface items, such as button labels and menu items.
- [CTFontUIFontType.palette](ctfontuifonttype/palette.md)
  The font in tool palettes.
- [CTFontUIFontType.toolTip](ctfontuifonttype/tooltip.md)
  The font for tool tips.
- [CTFontUIFontType.controlContent](ctfontuifonttype/controlcontent.md)
  The font for contents of user-interface controls.
### Deprecated
- [static var kCTFontNoFontType: CTFontUIFontType](ctfontuifonttype/kctfontnofonttype.md)
  The user-interface font type isn’t specified.
- [static var kCTFontUserFontType: CTFontUIFontType](ctfontuifonttype/kctfontuserfonttype.md)
  The font used by default for documents and other text under the user’s control.
- [static var kCTFontUserFixedPitchFontType: CTFontUIFontType](ctfontuifonttype/kctfontuserfixedpitchfonttype.md)
  The font used by default for documents and other text under the user’s control when that font is fixed-pitch.
- [static var kCTFontSystemFontType: CTFontUIFontType](ctfontuifonttype/kctfontsystemfonttype.md)
  The system font used for standard user-interface items, such as button labels and menu items.
- [static var kCTFontEmphasizedSystemFontType: CTFontUIFontType](ctfontuifonttype/kctfontemphasizedsystemfonttype.md)
  The system font used for emphasis in alerts.
- [static var kCTFontSmallSystemFontType: CTFontUIFontType](ctfontuifonttype/kctfontsmallsystemfonttype.md)
  The standard small system font used for informative text in alerts, column headings in lists, help tags, and small controls.
- [static var kCTFontSmallEmphasizedSystemFontType: CTFontUIFontType](ctfontuifonttype/kctfontsmallemphasizedsystemfonttype.md)
  The small system font used for emphasis.
- [static var kCTFontMiniSystemFontType: CTFontUIFontType](ctfontuifonttype/kctfontminisystemfonttype.md)
  The standard miniature system font used for mini controls and utility window labels and text.
- [static var kCTFontMiniEmphasizedSystemFontType: CTFontUIFontType](ctfontuifonttype/kctfontminiemphasizedsystemfonttype.md)
  The miniature system font used for emphasis.
- [static var kCTFontViewsFontType: CTFontUIFontType](ctfontuifonttype/kctfontviewsfonttype.md)
  The view font used as the default font of text in lists and tables.
- [static var kCTFontApplicationFontType: CTFontUIFontType](ctfontuifonttype/kctfontapplicationfonttype.md)
  The default font for text documents.
- [static var kCTFontLabelFontType: CTFontUIFontType](ctfontuifonttype/kctfontlabelfonttype.md)
  The font used for labels and tick marks on full-size sliders.
- [static var kCTFontMenuTitleFontType: CTFontUIFontType](ctfontuifonttype/kctfontmenutitlefonttype.md)
  The font used for menu titles.
- [static var kCTFontMenuItemFontType: CTFontUIFontType](ctfontuifonttype/kctfontmenuitemfonttype.md)
  The font used for menu items.
- [static var kCTFontMenuItemMarkFontType: CTFontUIFontType](ctfontuifonttype/kctfontmenuitemmarkfonttype.md)
  The font used to draw menu-item marks.
- [static var kCTFontMenuItemCmdKeyFontType: CTFontUIFontType](ctfontuifonttype/kctfontmenuitemcmdkeyfonttype.md)
  The font used for menu-item command-key equivalents.
- [static var kCTFontWindowTitleFontType: CTFontUIFontType](ctfontuifonttype/kctfontwindowtitlefonttype.md)
  The font used for window titles.
- [static var kCTFontPushButtonFontType: CTFontUIFontType](ctfontuifonttype/kctfontpushbuttonfonttype.md)
  The font used for a push button, a rounded rectangular button with a text label on it.
- [static var kCTFontUtilityWindowTitleFontType: CTFontUIFontType](ctfontuifonttype/kctfontutilitywindowtitlefonttype.md)
  The font used for utility window titles.
- [static var kCTFontAlertHeaderFontType: CTFontUIFontType](ctfontuifonttype/kctfontalertheaderfonttype.md)
  The font used for alert headers.
- [static var kCTFontSystemDetailFontType: CTFontUIFontType](ctfontuifonttype/kctfontsystemdetailfonttype.md)
  The standard system font used for details.
- [static var kCTFontEmphasizedSystemDetailFontType: CTFontUIFontType](ctfontuifonttype/kctfontemphasizedsystemdetailfonttype.md)
  The system font used for emphasis in details.
- [static var kCTFontToolbarFontType: CTFontUIFontType](ctfontuifonttype/kctfonttoolbarfonttype.md)
  The font used for labels of toolbar items.
- [static var kCTFontSmallToolbarFontType: CTFontUIFontType](ctfontuifonttype/kctfontsmalltoolbarfonttype.md)
  The small font used for labels of toolbar items.
- [static var kCTFontMessageFontType: CTFontUIFontType](ctfontuifonttype/kctfontmessagefonttype.md)
  The font used for standard interface items, such as button labels and menu items.
- [static var kCTFontPaletteFontType: CTFontUIFontType](ctfontuifonttype/kctfontpalettefonttype.md)
  The font used in tool palettes.
- [static var kCTFontToolTipFontType: CTFontUIFontType](ctfontuifonttype/kctfonttooltipfonttype.md)
  The font used for tool tips.
- [static var kCTFontControlContentFontType: CTFontUIFontType](ctfontuifonttype/kctfontcontrolcontentfonttype.md)
  The font used for contents of user-interface controls.
### Initializers
- [init?(rawValue: UInt32)](ctfontuifonttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CTFontTableTag](ctfonttabletag.md)
  Font table tags provide access to font table data.
- [struct CTFontTableOptions](ctfonttableoptions.md)
  Constants that describe font table options.
- [struct CTFontOptions](ctfontoptions.md)
  Options for font creation and descriptor matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontuifonttype)*