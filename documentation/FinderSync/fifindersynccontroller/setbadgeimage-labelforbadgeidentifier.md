# setBadgeImage(_:label:forBadgeIdentifier:)

**Framework**: Finder Sync  
**Kind**: method

Sets the badge image and label for the given ID.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setBadgeImage(_ image: NSImage, label: String?, forBadgeIdentifier badgeID: String)
```

#### Discussion

Use this method to configure your badges. Finder may display the image, the label or both. Your Finder Sync extension typically sets up a fixed number of badges during its `init` method.

## Parameters

- `image`: An    object. The system may or may not draw this image on top of the item’s   icon; when it does, the system determines the overlay position. Don’t   add any padding to the image to adjust this positioning. The image draws   at up to 320 x 320 points.
- `label`: A label describing the sync state represented by this badge.   Each label should be a short localized string, such as “Waiting.”
- `badgeID`: A unique ID, identifying this badge.

## See Also

- [class func `default`() -> Self](fifindersynccontroller/default.md)
  Returns the shared Finder Sync controller object.
- [var directoryURLs: Set<URL>!](fifindersynccontroller/directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](fifindersynccontroller/selecteditemurls.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](fifindersynccontroller/setbadgeidentifier(_:for:).md)
  Sets the badge for a file or directory.
- [func targetedURL() -> URL?](fifindersynccontroller/targetedurl.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/setbadgeimage(_:label:forbadgeidentifier:))*