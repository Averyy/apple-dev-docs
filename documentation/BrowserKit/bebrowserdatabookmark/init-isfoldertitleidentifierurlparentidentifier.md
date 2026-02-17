# init(isFolder:title:identifier:url:parentIdentifier:)

**Framework**: BrowserKit  
**Kind**: init

Creates a bookmark.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
init(isFolder: Bool, title: String, identifier: String, url: URL?, parentIdentifier: String?)
```

## Parameters

- `isFolder`: A Boolean value that indicates whether a bookmark represents a folder.
- `title`: The title of the bookmark.
- `identifier`: A unique identifier for the bookmark.
- `url`: The URL that the bookmark points to, or   if the bookmark is a folder.
- `parentIdentifier`: The identifier of the parent folder, or   if the bookmark is a top-level bookmark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatabookmark/init(isfolder:title:identifier:url:parentidentifier:))*