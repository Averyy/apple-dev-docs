# imageFileTypes()

**Framework**: AppKit  
**Kind**: method

Returns an array of strings identifying the image types supported by the registered image representation objects.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func imageFileTypes() -> [String]
```

#### Return Value

An array of `NSString` objects, each of which identifies a single supported file type. The array can include encoded HFS file types as well as filename extensions.

#### Discussion

This list includes all file types supported by registered subclasses of [`NSImageRep`](nsimagerep.md) plus those that can be converted to a supported type by a user-installed filter service. You can pass the array returned by this method directly to the [`runModalForTypes:`](nsopenpanel/runmodalfortypes:.md) method of `NSOpenPanel`.

Do not override this method. If your app supports custom image types, create and register an [`NSImageRep`](nsimagerep.md) subclass that handles those types.

## See Also

- [class func imageUnfilteredFileTypes() -> [String]](nsimage/imageunfilteredfiletypes.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimage/imagepasteboardtypes.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimage/imageunfilteredpasteboardtypes.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/imagefiletypes())*