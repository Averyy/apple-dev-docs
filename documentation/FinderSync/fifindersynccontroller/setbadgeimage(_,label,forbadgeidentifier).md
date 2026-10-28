# setBadgeImage(_:label:forBadgeIdentifier:)

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

Sets the badge image and label for the given ID.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setBadgeImage(_ image: NSImage, label: String?, forBadgeIdentifier badgeID: String)
```

```objc
- (void) setBadgeImage:(NSImage *) image label:(NSString *) label forBadgeIdentifier:(NSString *) badgeID;
```

## Discussion

Use this method to configure your badges. Finder may display the image, the label or both. Your Finder Sync extension typically sets up a fixed number of badges during its `init` method.

## Parameters

- `image`: An [`NSImage`](../../AppKit/nsimage.md) object. The system may or may not draw this image on top of the item’s icon; when it does, the system determines the overlay position. Don’t add any padding to the image to adjust this positioning. The image draws at up to 320 x 320 points.
- `label`: A label describing the sync state represented by this badge. Each label should be a short localized string, such as “Waiting.”
- `badgeID`: A unique ID, identifying this badge.

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
- [func targetedURL() -> URL?](./targetedurl%28%29.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/setbadgeimage(_:label:forbadgeidentifier:))*