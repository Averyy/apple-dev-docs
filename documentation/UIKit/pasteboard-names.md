# Pasteboard Names

**Framework**: UIKit

Names identifying the system pasteboards.

#### Overview

You can access the general system pasteboard by calling the class method [`init(name:create:)`](uipasteboard/init(name:create:).md), specifying the `UIPasteboardNameGeneral` constant as the first argument. You can alternatively access the general pasteboard by calling the [`general`](uipasteboard/general.md) class method. The general system pasteboard is persistent across device restarts, app uninstalls, and app restores.

## Topics

### Constants
- [static let general: UIPasteboard.Name](uipasteboard/name-swift.struct/general.md)
  The name identifying the general pasteboard, which you use for general copy-cut-paste operations.
- [let UIPasteboardNameFind: String](uipasteboardnamefind.md)
  A name that identifies the Find pasteboard.

## See Also

- [UIPasteboard.Name](uipasteboard/name-swift.struct.md)
  Constants that identify the name of a pasteboard.
- [UIPasteboard.OptionsKey](uipasteboard/optionskey.md)
  Options for describing pasteboard privacy.
- [Pasteboard Data Type Representations](pasteboard-data-type-representations.md)
  Pasteboard-item representation types, as for a given object value.
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md)
  Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/pasteboard-names)*