# BEBrowserDataBookmark

**Framework**: BrowserKit  
**Kind**: class  
**Role**: Class

A class that transfers bookmark information between browsers.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEBrowserDataBookmark
```

```objc
@interface BEBrowserDataBookmark : BEBrowserData
```

## Overview

This class represents a single bookmark or bookmark folder with its associated metadata including title, URL, and relationship to other bookmarks. Bookmarks reside in a folder structure according to the [`parentIdentifier`](./bebrowserdatabookmark/parentidentifier.md) property.

## Topics

### Creating a bookmark
- [init(isFolder: Bool, title: String, identifier: String, url: URL?, parentIdentifier: String?)](./bebrowserdatabookmark/init%28isfolder,title,identifier,url,parentidentifier%29.md)
  Creates a bookmark.
### Accessing bookmark properties
- [var identifier: String](./bebrowserdatabookmark/identifier.md)
  A unique identifier for a bookmark.
- [var isFolder: Bool](./bebrowserdatabookmark/isfolder.md)
  A Boolean value that indicates whether a bookmark represents a folder.
- [var title: String](./bebrowserdatabookmark/title.md)
  A localized title for a bookmark.
- [var url: URL?](./bebrowserdatabookmark/url.md)
  A URL to which a bookmark points.
### Managing bookmark hierarchy
- [var parentIdentifier: String?](./bebrowserdatabookmark/parentidentifier.md)
  A string that identifies the bookmark’s parent folder.
### Initializers
- [init(asFolder: Bool, title: String, identifier: String, url: URL?, parentIdentifier: String?)](./bebrowserdatabookmark/init%28asfolder,title,identifier,url,parentidentifier%29.md)

## Relationships

### Inherits From
- [BEBrowserData](./bebrowserdata.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Browser data
- [class BEBrowserDataHistoryVisit](./bebrowserdatahistoryvisit.md)
  A class that transfers page visit history between browsers.
- [class BEBrowserDataReadingListItem](./bebrowserdatareadinglistitem.md)
  A class that transfers reading list data between browsers.
- [class BEBrowserDataExtension](./bebrowserdataextension.md)
  A class that transfers browser extension information between browsers.
- [class BEBrowserData](./bebrowserdata.md)
  A representation of browsing data from a source browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatabookmark)*