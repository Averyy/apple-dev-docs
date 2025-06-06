# default()

**Framework**: Finder Sync  
**Kind**: method

Returns the shared Finder Sync controller object.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func `default`() -> Self
```

#### Return Value

The default Finder Sync controller object for this extension.

## See Also

- [var directoryURLs: Set<URL>!](fifindersynccontroller/directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](fifindersynccontroller/selecteditemurls.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](fifindersynccontroller/setbadgeidentifier(_:for:).md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](fifindersynccontroller/setbadgeimage(_:label:forbadgeidentifier:).md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](fifindersynccontroller/targetedurl.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/default())*