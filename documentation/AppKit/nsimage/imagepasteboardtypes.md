# imagePasteboardTypes()

**Framework**: AppKit  
**Kind**: method

Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]
```

#### Return Value

An array of `NSString` objects, each of which identifies a single supported pasteboard type. By default, this list contains the  `NSPDFPboardType`, `NSPICTPboardType`, `NSPostScriptPboardType`, and `NSTIFFPboardType` types.

#### Discussion

This list includes all pasteboard types supported by registered subclasses of [`NSImageRep`](nsimagerep.md) plus those that can be converted to a supported type by a user-installed filter service.

Do not override this method. Instead, override the [`imageUnfilteredPasteboardTypes()`](nsimagerep/imageunfilteredpasteboardtypes().md) method to notify `NSImage` of the pasteboard types your class supports.

## See Also

- [class func imageFileTypes() -> [String]](nsimage/imagefiletypes.md)
  Returns an array of strings identifying the image types supported by the registered image representation objects.
- [class func imageUnfilteredFileTypes() -> [String]](nsimage/imageunfilteredfiletypes.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimage/imageunfilteredpasteboardtypes.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/imagepasteboardtypes())*