# directoryURLs

**Framework**: Finder Sync  
**Kind**: property

The directories managed by this extension.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var directoryURLs: Set<URL>! { get set }
```

#### Discussion

The extension receives [`beginObservingDirectory(at:)`](fifindersyncprotocol/beginobservingdirectory(at:).md) and [`endObservingDirectory(at:)`](fifindersyncprotocol/endobservingdirectory(at:).md) messages for every directory in this set and for all of their subdirectories.

Always set `directoryURLs` when the extension starts. If there are no directories to watch, set `directoryURLs` to an empty set.

## See Also

- [class func `default`() -> Self](fifindersynccontroller/default.md)
  Returns the shared Finder Sync controller object.
- [func selectedItemURLs() -> [URL]?](fifindersynccontroller/selecteditemurls.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](fifindersynccontroller/setbadgeidentifier(_:for:).md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](fifindersynccontroller/setbadgeimage(_:label:forbadgeidentifier:).md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](fifindersynccontroller/targetedurl.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/directoryurls)*