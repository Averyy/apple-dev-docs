# targetedURL()

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

Returns the URL of the Finder’s current target.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func targetedURL() -> URL?
```

```objc
- (NSURL *) targetedURL;
```

#### Return Value

The URL of the Finder’s current target.

#### Discussion

Use this method when creating a custom shortcut menu for the Finder. This returns the URL of the item that the user Control-clicked, letting you customize the menu for that item.

This method returns valid values only from the Finder Sync extension’s [`menu(for:)`](../fifindersyncprotocol/menu%28for%29.md) method or from one of the menu actions created in this method. If the selected items are outside the extension’s managed directories (for example, when the user clicks on the toolbar button), this method returns `nil`.

## See Also

### Managing the Finder Sync Controller
- [class func `default`() -> Self](./default%28%29.md)
  Returns the shared Finder Sync controller object.
- [var directoryURLs: Set<URL>!](./directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](./selecteditemurls%28%29.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](./setbadgeidentifier%28_,for%29.md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](./setbadgeimage%28_,label,forbadgeidentifier%29.md)
  Sets the badge image and label for the given ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/targetedurl())*