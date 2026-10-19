# imageFileTypes()

**Framework**: AppKit  
**Kind**: method

Returns the file types supported by the image representation class or one of its subclasses.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func imageFileTypes() -> [String]
```

#### Return Value

An array of `NSString` objects, each of which contains a filename extension or HFS file type of a supported format.

#### Discussion

The list includes both those types returned by the [`imageUnfilteredFileTypes()`](nsimagerep/imageunfilteredfiletypes().md) class method plus those that can be converted to a supported type by a user-installed filter service. The returned file types can include encoded HFS file types as well as filename extensions.

Don’t override this method when subclassing `NSImageRep`—it always returns a valid list for any subclass of `NSImageRep` that correctly overrides the [`imageUnfilteredFileTypes()`](nsimagerep/imageunfilteredfiletypes().md) method.

## See Also

- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imagepasteboardtypes.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
- [class func imageUnfilteredFileTypes() -> [String]](nsimagerep/imageunfilteredfiletypes.md)
  Returns the list of file types supported directly by the image representation.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imageunfilteredpasteboardtypes.md)
  Returns the list of pasteboard types supported directly by the image representation.
- [class func `class`(forFileType: String) -> AnyClass?](nsimagerep/class(forfiletype:).md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](nsimagerep/class(forpasteboardtype:).md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/imagefiletypes())*