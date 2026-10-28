# imagePasteboardTypes()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use +imageTypes instead

## Declaration

```swift
class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]
```

```objc
+ (NSArray<NSString *> *) imagePasteboardTypes;
```

## Return Value

An array of `NSString` objects, each of which identifies a single supported pasteboard type. By default, this list contains the  `NSPDFPboardType`, `NSPICTPboardType`, `NSPostScriptPboardType`, and `NSTIFFPboardType` types.

## Discussion

This list includes all pasteboard types supported by registered subclasses of [`NSImageRep`](../nsimagerep.md) plus those that can be converted to a supported type by a user-installed filter service.

Do not override this method. Instead, override the [`imageUnfilteredPasteboardTypes()`](../nsimagerep/imageunfilteredpasteboardtypes%28%29.md) method to notify `NSImage` of the pasteboard types your class supports.

## See Also

### Deprecated class methods
- [class func imageFileTypes() -> [String]](./imagefiletypes%28%29.md)
  Returns an array of strings identifying the image types supported by the registered image representation objects.
- [class func imageUnfilteredFileTypes() -> [String]](./imageunfilteredfiletypes%28%29.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](./imageunfilteredpasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/imagepasteboardtypes())*