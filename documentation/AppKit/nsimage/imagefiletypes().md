# imageFileTypes()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns an array of strings identifying the image types supported by the registered image representation objects.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`imageTypes`](./imagetypes.md) instead.

## Declaration

```swift
class func imageFileTypes() -> [String]
```

```objc
+ (NSArray<NSString *> *) imageFileTypes;
```

## Return Value

An array of `NSString` objects, each of which identifies a single supported file type. The array can include encoded HFS file types as well as filename extensions.

## Discussion

This list includes all file types supported by registered subclasses of [`NSImageRep`](../nsimagerep.md) plus those that can be converted to a supported type by a user-installed filter service. You can pass the array returned by this method directly to the [`runModalForTypes:`](../nsopenpanel/runmodalfortypes_.md) method of `NSOpenPanel`.

Do not override this method. If your app supports custom image types, create and register an [`NSImageRep`](../nsimagerep.md) subclass that handles those types.

## See Also

### Deprecated class methods
- [class func imageUnfilteredFileTypes() -> [String]](./imageunfilteredfiletypes%28%29.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./imagepasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](./imageunfilteredpasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/imagefiletypes())*