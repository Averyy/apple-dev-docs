# setBadgeIdentifier(_:for:)

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

Sets the badge for a file or directory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setBadgeIdentifier(_ badgeID: String, for url: URL)
```

```objc
- (void) setBadgeIdentifier:(NSString *) badgeID forURL:(NSURL *) url;
```

#### Discussion

Adds the specified badge to the given file or directory. Setting the identifier to an empty string (`@""`) removes the badge.

Avoid adding badges to items that the Finder hasn’t displayed yet. When setting the initial badge, call this method from your Finder Sync extension’s [`requestBadgeIdentifier(for:)`](../fifindersyncprotocol/requestbadgeidentifier%28for%29.md) method. When updating badges, call this method only for items that have already received a badge.

## Parameters

- `badgeID`: A unique ID, identifying the badge.
- `url`: The URL of the file or directory.

## See Also

### Related Documentation
- [func requestBadgeIdentifier(for: URL)](../fifindersyncprotocol/requestbadgeidentifier%28for%29.md)
  Requests a badge for the given file or directory.
### Managing the Finder Sync Controller
- [class func `default`() -> Self](./default%28%29.md)
  Returns the shared Finder Sync controller object.
- [var directoryURLs: Set<URL>!](./directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](./selecteditemurls%28%29.md)
  Returns an array of selected items.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](./setbadgeimage%28_,label,forbadgeidentifier%29.md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](./targetedurl%28%29.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/setbadgeidentifier(_:for:))*