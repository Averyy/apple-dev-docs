# setBadgeIdentifier(_:for:)

**Framework**: Finder Sync  
**Kind**: method

Sets the badge for a file or directory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setBadgeIdentifier(_ badgeID: String, for url: URL)
```

#### Discussion

Adds the specified badge to the given file or directory. Setting the identifier to an empty string (`@""`) removes the badge.

Avoid adding badges to items that the Finder hasn’t displayed yet. When setting the initial badge, call this method from your Finder Sync extension’s [`requestBadgeIdentifier(for:)`](fifindersyncprotocol/requestbadgeidentifier(for:).md) method. When updating badges, call this method only for items that have already received a badge.

## Parameters

- `badgeID`: A unique ID, identifying the badge.
- `url`: The URL of the file or directory.

## See Also

- [func requestBadgeIdentifier(for: URL)](fifindersyncprotocol/requestbadgeidentifier(for:).md)
  Requests a badge for the given file or directory.
- [class func `default`() -> Self](fifindersynccontroller/default.md)
  Returns the shared Finder Sync controller object.
- [var directoryURLs: Set<URL>!](fifindersynccontroller/directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](fifindersynccontroller/selecteditemurls.md)
  Returns an array of selected items.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](fifindersynccontroller/setbadgeimage(_:label:forbadgeidentifier:).md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](fifindersynccontroller/targetedurl.md)
  Returns the URL of the Finder’s current target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/setbadgeidentifier(_:for:))*