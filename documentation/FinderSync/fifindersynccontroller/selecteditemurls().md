# selectedItemURLs()

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

Returns an array of selected items.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func selectedItemURLs() -> [URL]?
```

```objc
- (NSArray<NSURL *> *) selectedItemURLs;
```

#### Return Value

An array of items currently selected in the Finder window.

#### Discussion

Use this method when creating a shortcut menu or a menu for the extension’s toolbar button. You can then modify the menu’s content based on the items currently selected.

This method returns valid values only from the Finder Sync extension’s [`menu(for:)`](../fifindersyncprotocol/menu%28for%29.md) method or from one of the menu actions created in this method. If the selected items are outside the extension’s managed directories (for example, when the user clicks on the toolbar button), this method returns `nil`.

## See Also

### Managing the Finder Sync Controller
- [class func `default`() -> Self](./default%28%29.md)
  Returns the shared Finder Sync controller object.
- [var directoryURLs: Set<URL>!](./directoryurls.md)
  The directories managed by this extension.
- [func setBadgeIdentifier(String, for: URL)](./setbadgeidentifier%28_,for%29.md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](./setbadgeimage%28_,label,forbadgeidentifier%29.md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](./targetedurl%28%29.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/selecteditemurls())*