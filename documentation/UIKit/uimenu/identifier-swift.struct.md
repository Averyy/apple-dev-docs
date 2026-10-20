# UIMenu.Identifier

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants you use to identify an app’s standard menus.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Identifier
```

```c
typedef NSString * UIMenuIdentifier;
```

#### Overview

Use these constants to identify [`UIMenu`](../uimenu.md) objects containing standard configurations.

When creating a custom menu identifier, provide a reverse domain name string value, such as `UIMenu.Identifier("com.example.apple-samplecode.MenubarSample.reloadMenu")`.

## Topics

### Top-level menus
- [static let application: UIMenu.Identifier](./identifier-swift.struct/application.md)
  The standard app menu.
- [static let file: UIMenu.Identifier](./identifier-swift.struct/file.md)
  The standard File menu.
- [static let edit: UIMenu.Identifier](./identifier-swift.struct/edit.md)
  The standard Edit menu.
- [static let view: UIMenu.Identifier](./identifier-swift.struct/view.md)
  The standard View menu.
- [static let window: UIMenu.Identifier](./identifier-swift.struct/window.md)
  The standard Window menu.
- [static let help: UIMenu.Identifier](./identifier-swift.struct/help.md)
  The standard Help menu.
### App menu commands
- [static let about: UIMenu.Identifier](./identifier-swift.struct/about.md)
  The About menu.
- [static let preferences: UIMenu.Identifier](./identifier-swift.struct/preferences.md)
  The Preferences menu.
- [static let services: UIMenu.Identifier](./identifier-swift.struct/services.md)
  The Services menu.
- [static let hide: UIMenu.Identifier](./identifier-swift.struct/hide.md)
  The Hide menu.
- [static let quit: UIMenu.Identifier](./identifier-swift.struct/quit.md)
  The Quit menu.
### File menus
- [static let newItem: UIMenu.Identifier](./identifier-swift.struct/newitem.md)
  New item menu
- [static let openRecent: UIMenu.Identifier](./identifier-swift.struct/openrecent.md)
  The Open Recent menu.
- [static let open: UIMenu.Identifier](./identifier-swift.struct/open.md)
  The Open menu.
- [static let close: UIMenu.Identifier](./identifier-swift.struct/close.md)
  The Close menu.
- [static let print: UIMenu.Identifier](./identifier-swift.struct/print.md)
  The Print menu.
- [static let document: UIMenu.Identifier](./identifier-swift.struct/document.md)
  The Document menu.
- [static let newScene: UIMenu.Identifier](./identifier-swift.struct/newscene.md)
  The New Scene menu.
### Edit menus
- [static let undoRedo: UIMenu.Identifier](./identifier-swift.struct/undoredo.md)
  The Undo/Redo menu.
- [static let standardEdit: UIMenu.Identifier](./identifier-swift.struct/standardedit.md)
  The standard Edit menu.
- [static let find: UIMenu.Identifier](./identifier-swift.struct/find.md)
  The Find menu.
- [static let findPanel: UIMenu.Identifier](./identifier-swift.struct/findpanel.md)
  Find panel menu (Find, Find and Replace, Find Next, Find Previous)
- [static let replace: UIMenu.Identifier](./identifier-swift.struct/replace.md)
  The Replace menu.
- [static let share: UIMenu.Identifier](./identifier-swift.struct/share.md)
  The Share menu.
- [static let textStyle: UIMenu.Identifier](./identifier-swift.struct/textstyle.md)
  The Text Style menu.
- [static let spelling: UIMenu.Identifier](./identifier-swift.struct/spelling.md)
  The Spelling menu.
- [static let spellingPanel: UIMenu.Identifier](./identifier-swift.struct/spellingpanel.md)
  The Spelling Panel menu.
- [static let spellingOptions: UIMenu.Identifier](./identifier-swift.struct/spellingoptions.md)
  The Spelling Options menu.
- [static let substitutions: UIMenu.Identifier](./identifier-swift.struct/substitutions.md)
  The Substitutions menu.
- [static let substitutionsPanel: UIMenu.Identifier](./identifier-swift.struct/substitutionspanel.md)
  The Substitutions Panel menu.
- [static let substitutionOptions: UIMenu.Identifier](./identifier-swift.struct/substitutionoptions.md)
  The Substitutions Options menu.
- [static let transformations: UIMenu.Identifier](./identifier-swift.struct/transformations.md)
  The Transformations menu.
- [static let speech: UIMenu.Identifier](./identifier-swift.struct/speech.md)
  The Speech menu.
- [static let lookup: UIMenu.Identifier](./identifier-swift.struct/lookup.md)
  The Lookup menu.
- [static let learn: UIMenu.Identifier](./identifier-swift.struct/learn.md)
  The Learn menu.
- [static let format: UIMenu.Identifier](./identifier-swift.struct/format.md)
  The Format menu.
- [static let font: UIMenu.Identifier](./identifier-swift.struct/font.md)
  The Font menu.
- [static let textSize: UIMenu.Identifier](./identifier-swift.struct/textsize.md)
  The Text Size menu.
- [static let textColor: UIMenu.Identifier](./identifier-swift.struct/textcolor.md)
  The Text Color menu.
- [static let textStylePasteboard: UIMenu.Identifier](./identifier-swift.struct/textstylepasteboard.md)
  The Text Style Pasteboard menu.
- [static let text: UIMenu.Identifier](./identifier-swift.struct/text.md)
  The Text menu.
- [static let autoFill: UIMenu.Identifier](./identifier-swift.struct/autofill.md)
  The AutoFill menu.
- [static let writingDirection: UIMenu.Identifier](./identifier-swift.struct/writingdirection.md)
  The Writing Direction menu.
- [static let alignment: UIMenu.Identifier](./identifier-swift.struct/alignment.md)
  The Alignment menu.
### View menus
- [static let toolbar: UIMenu.Identifier](./identifier-swift.struct/toolbar.md)
  The Toolbar menu group.
- [static let sidebar: UIMenu.Identifier](./identifier-swift.struct/sidebar.md)
  The Sidebar menu group.
- [static let fullscreen: UIMenu.Identifier](./identifier-swift.struct/fullscreen.md)
  The Full Screen menu.
### Window menus
- [static let minimizeAndZoom: UIMenu.Identifier](./identifier-swift.struct/minimizeandzoom.md)
  The Minimize and Zoom menu.
- [static let bringAllToFront: UIMenu.Identifier](./identifier-swift.struct/bringalltofront.md)
  The Bring All to Front menu.
### Root menu
- [static let root: UIMenu.Identifier](./identifier-swift.struct/root.md)
  The root menu.
### Initializers
- [init(String)](./identifier-swift.struct/init%28_%29.md)
  Creates a menu identifier.
- [init(rawValue: String)](./identifier-swift.struct/init%28rawvalue%29.md)
  Creates a menu identifier with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a menu object
- [convenience init(title: String, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](./init%28title,image,identifier,options,children%29.md)
  Creates a new menu with the specified values.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](./init%28title,subtitle,image,identifier,options,children%29.md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, preferredElementSize: UIMenu.ElementSize, children: [UIMenuElement])](./init%28title,subtitle,image,identifier,options,preferredelementsize,children%29.md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [UIMenu.Options](./options-swift.struct.md)
  Options you use to configure a menu’s appearance.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/identifier-swift.struct)*