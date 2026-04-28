# SafariBookmarksBookmarksItemObject

**Framework**: Device Management  
**Kind**: dictionary

A bookmark that specifies a title, and either a URL for the bookmark, or a nested folder of bookmarks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SafariBookmarksBookmarksItemObject
```

## Properties

- `Folder` ([SafariBookmarksBookmarksItemObject]): An array of bookmarks for each bookmark in the folder. Folders can include bookmark items and bookmark folders. Only one of `URL` or `Folder` must be present.
- `Title` (string) *(required)*: The title of the bookmark shown in Safari.
- `URL` (string): The URL for the bookmark item. Only one of `URL` or `Folder` must be present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safaribookmarksbookmarksitemobject)*