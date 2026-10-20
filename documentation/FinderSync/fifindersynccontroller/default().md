# default()

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Type Method

Returns the shared Finder Sync controller object.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func `default`() -> Self
```

```objc
+ (instancetype) defaultController;
```

#### Return Value

The default Finder Sync controller object for this extension.

## See Also

### Managing the Finder Sync Controller
- [var directoryURLs: Set<URL>!](./directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](./selecteditemurls%28%29.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](./setbadgeidentifier%28_,for%29.md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](./setbadgeimage%28_,label,forbadgeidentifier%29.md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](./targetedurl%28%29.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/default())*