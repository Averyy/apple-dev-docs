# directoryURLs

**Framework**: Finder Sync  
**Kind**: property  
**Role**: Instance Property

The directories managed by this extension.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var directoryURLs: Set<URL>! { get set }
```

```objc
@property (copy, null_resettable) NSSet<NSURL *> * directoryURLs;
```

#### Discussion

The extension receives [`beginObservingDirectory(at:)`](../fifindersyncprotocol/beginobservingdirectory%28at%29.md) and [`endObservingDirectory(at:)`](../fifindersyncprotocol/endobservingdirectory%28at%29.md) messages for every directory in this set and for all of their subdirectories.

Always set `directoryURLs` when the extension starts. If there are no directories to watch, set `directoryURLs` to an empty set.

## See Also

### Managing the Finder Sync Controller
- [class func `default`() -> Self](./default%28%29.md)
  Returns the shared Finder Sync controller object.
- [func selectedItemURLs() -> [URL]?](./selecteditemurls%28%29.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](./setbadgeidentifier%28_,for%29.md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](./setbadgeimage%28_,label,forbadgeidentifier%29.md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](./targetedurl%28%29.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/directoryurls)*