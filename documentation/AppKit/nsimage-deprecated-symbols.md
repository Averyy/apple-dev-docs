# Deprecated symbols

**Framework**: AppKit

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated class methods
- [class func imageFileTypes() -> [String]](nsimage/imagefiletypes.md)
  Returns an array of strings identifying the image types supported by the registered image representation objects.
- [class func imageUnfilteredFileTypes() -> [String]](nsimage/imageunfilteredfiletypes.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimage/imagepasteboardtypes.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimage/imageunfilteredpasteboardtypes.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
### Deprecated instance methods
- [func lockFocus()](nsimage/lockfocus.md)
  Prepares the image to receive drawing commands.
- [func lockFocusFlipped(Bool)](nsimage/lockfocusflipped(_:).md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [func unlockFocus()](nsimage/unlockfocus.md)
  Removes the focus from the image.
- [convenience init(iconRef: IconRef)](nsimage/init(iconref:).md)
  Initializes the image object with a Carbon-style icon resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage-deprecated-symbols)*