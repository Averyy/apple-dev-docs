# targetedURL()

**Framework**: Finder Sync  
**Kind**: method

Returns the URL of the Finder’s current target.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func targetedURL() -> URL?
```

#### Return Value

The URL of the Finder’s current target.

#### Discussion

Use this method when creating a custom shortcut menu for the Finder. This returns the URL of the item that the user Control-clicked, letting you customize the menu for that item.

This method returns valid values only from the Finder Sync extension’s [`menu(for:)`](fifindersyncprotocol/menu(for:).md) method or from one of the menu actions created in this method. If the selected items are outside the extension’s managed directories (for example, when the user clicks on the toolbar button), this method returns `nil`.

## See Also

- [class func `default`() -> Self](fifindersynccontroller/default.md)
  Returns the shared Finder Sync controller object.
- [var directoryURLs: Set<URL>!](fifindersynccontroller/directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](fifindersynccontroller/selecteditemurls.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](fifindersynccontroller/setbadgeidentifier(_:for:).md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](fifindersynccontroller/setbadgeimage(_:label:forbadgeidentifier:).md)
  Sets the badge image and label for the given ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/targetedurl())*