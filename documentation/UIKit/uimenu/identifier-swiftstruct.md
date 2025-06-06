# UIMenu.Identifier

**Framework**: UIKit  
**Kind**: struct

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

#### Overview

Use these constants to identify [`UIMenu`](uimenu.md) objects containing standard configurations.

When creating a custom menu identifier, provide a reverse domain name string value, such as `UIMenu.Identifier("com.example.apple-samplecode.MenubarSample.reloadMenu")`.

## Topics

### Top-level menus
- [static let application: UIMenu.Identifier](uimenu/identifier-swift.struct/application.md)
  The standard app menu.
- [static let file: UIMenu.Identifier](uimenu/identifier-swift.struct/file.md)
  The standard File menu.
- [static let edit: UIMenu.Identifier](uimenu/identifier-swift.struct/edit.md)
  The standard Edit menu.
- [static let view: UIMenu.Identifier](uimenu/identifier-swift.struct/view.md)
  The standard View menu.
- [static let window: UIMenu.Identifier](uimenu/identifier-swift.struct/window.md)
  The standard Window menu.
- [static let help: UIMenu.Identifier](uimenu/identifier-swift.struct/help.md)
  The standard Help menu.
### App menu commands
- [static let about: UIMenu.Identifier](uimenu/identifier-swift.struct/about.md)
  The About menu.
- [static let preferences: UIMenu.Identifier](uimenu/identifier-swift.struct/preferences.md)
  The Preferences menu.
- [static let services: UIMenu.Identifier](uimenu/identifier-swift.struct/services.md)
  The Services menu.
- [static let hide: UIMenu.Identifier](uimenu/identifier-swift.struct/hide.md)
  The Hide menu.
- [static let quit: UIMenu.Identifier](uimenu/identifier-swift.struct/quit.md)
  The Quit menu.
### File menus
- [static let newScene: UIMenu.Identifier](uimenu/identifier-swift.struct/newscene.md)
  The New Scene menu.
- [static let openRecent: UIMenu.Identifier](uimenu/identifier-swift.struct/openrecent.md)
  The Open Recent menu.
- [static let open: UIMenu.Identifier](uimenu/identifier-swift.struct/open.md)
  The Open menu.
- [static let close: UIMenu.Identifier](uimenu/identifier-swift.struct/close.md)
  The Close menu.
- [static let print: UIMenu.Identifier](uimenu/identifier-swift.struct/print.md)
  The Print menu.
- [static let document: UIMenu.Identifier](uimenu/identifier-swift.struct/document.md)
  The Document menu.
### Edit menus
- [static let undoRedo: UIMenu.Identifier](uimenu/identifier-swift.struct/undoredo.md)
  The Undo/Redo menu.
- [static let standardEdit: UIMenu.Identifier](uimenu/identifier-swift.struct/standardedit.md)
  The standard Edit menu.
- [static let find: UIMenu.Identifier](uimenu/identifier-swift.struct/find.md)
  The Find menu.
- [static let replace: UIMenu.Identifier](uimenu/identifier-swift.struct/replace.md)
  The Replace menu.
- [static let share: UIMenu.Identifier](uimenu/identifier-swift.struct/share.md)
  The Share menu.
- [static let textStyle: UIMenu.Identifier](uimenu/identifier-swift.struct/textstyle.md)
  The Text Style menu.
- [static let spelling: UIMenu.Identifier](uimenu/identifier-swift.struct/spelling.md)
  The Spelling menu.
- [static let spellingPanel: UIMenu.Identifier](uimenu/identifier-swift.struct/spellingpanel.md)
  The Spelling Panel menu.
- [static let spellingOptions: UIMenu.Identifier](uimenu/identifier-swift.struct/spellingoptions.md)
  The Spelling Options menu.
- [static let substitutions: UIMenu.Identifier](uimenu/identifier-swift.struct/substitutions.md)
  The Substitutions menu.
- [static let substitutionsPanel: UIMenu.Identifier](uimenu/identifier-swift.struct/substitutionspanel.md)
  The Substitutions Panel menu.
- [static let substitutionOptions: UIMenu.Identifier](uimenu/identifier-swift.struct/substitutionoptions.md)
  The Substitutions Options menu.
- [static let transformations: UIMenu.Identifier](uimenu/identifier-swift.struct/transformations.md)
  The Transformations menu.
- [static let speech: UIMenu.Identifier](uimenu/identifier-swift.struct/speech.md)
  The Speech menu.
- [static let lookup: UIMenu.Identifier](uimenu/identifier-swift.struct/lookup.md)
  The Lookup menu.
- [static let learn: UIMenu.Identifier](uimenu/identifier-swift.struct/learn.md)
  The Learn menu.
- [static let format: UIMenu.Identifier](uimenu/identifier-swift.struct/format.md)
  The Format menu.
- [static let font: UIMenu.Identifier](uimenu/identifier-swift.struct/font.md)
  The Font menu.
- [static let textSize: UIMenu.Identifier](uimenu/identifier-swift.struct/textsize.md)
  The Text Size menu.
- [static let textColor: UIMenu.Identifier](uimenu/identifier-swift.struct/textcolor.md)
  The Text Color menu.
- [static let textStylePasteboard: UIMenu.Identifier](uimenu/identifier-swift.struct/textstylepasteboard.md)
  The Text Style Pasteboard menu.
- [static let text: UIMenu.Identifier](uimenu/identifier-swift.struct/text.md)
  The Text menu.
- [static let autoFill: UIMenu.Identifier](uimenu/identifier-swift.struct/autofill.md)
  The AutoFill menu.
- [static let writingDirection: UIMenu.Identifier](uimenu/identifier-swift.struct/writingdirection.md)
  The Writing Direction menu.
- [static let alignment: UIMenu.Identifier](uimenu/identifier-swift.struct/alignment.md)
  The Alignment menu.
### View menus
- [static let toolbar: UIMenu.Identifier](uimenu/identifier-swift.struct/toolbar.md)
  The Toolbar menu group.
- [static let sidebar: UIMenu.Identifier](uimenu/identifier-swift.struct/sidebar.md)
  The Sidebar menu group.
- [static let fullscreen: UIMenu.Identifier](uimenu/identifier-swift.struct/fullscreen.md)
  The Full Screen menu.
### Window menus
- [static let minimizeAndZoom: UIMenu.Identifier](uimenu/identifier-swift.struct/minimizeandzoom.md)
  The Minimize and Zoom menu.
- [static let bringAllToFront: UIMenu.Identifier](uimenu/identifier-swift.struct/bringalltofront.md)
  The Bring All to Front menu.
### Root menu
- [static let root: UIMenu.Identifier](uimenu/identifier-swift.struct/root.md)
  The root menu.
### Initializers
- [init(String)](uimenu/identifier-swift.struct/init(_:).md)
  Creates a menu identifier.
- [init(rawValue: String)](uimenu/identifier-swift.struct/init(rawvalue:).md)
  Creates a menu identifier with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init(title: String, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:image:identifier:options:children:).md)
  Creates a new menu with the specified values.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, preferredElementSize: UIMenu.ElementSize, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:preferredelementsize:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [UIMenu.Options](uimenu/options-swift.struct.md)
  Options you use to configure a menu’s appearance.
- [init?(coder: NSCoder)](uimenu/init(coder:).md)
  Creates a menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/identifier-swift.struct)*