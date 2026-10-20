# BEBrowserDataReadingListItem

**Framework**: BrowserKit  
**Kind**: class  
**Role**: Class

A class that transfers reading list data between browsers.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEBrowserDataReadingListItem
```

```objc
@interface BEBrowserDataReadingListItem : BEBrowserData
```

#### Overview

This class represents an article or webpage in a reading list, including a URL, a title, and the date the item was last opened.

## Topics

### Creating a reading list item
- [init(title: String, url: URL, dateOfLastVisit: Date?)](./bebrowserdatareadinglistitem/init%28title,url,dateoflastvisit%29.md)
  Initializes a reading list item with the given content and access metadata.
### Accessing item properties
- [var dateOfLastVisit: Date?](./bebrowserdatareadinglistitem/dateoflastvisit.md)
  The date of the person’s last visit.
- [var title: String](./bebrowserdatareadinglistitem/title.md)
  A localized title for a reading list item.
- [var url: URL](./bebrowserdatareadinglistitem/url.md)
  A URL for the reading list item.

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
- [class BEBrowserDataBookmark](./bebrowserdatabookmark.md)
  A class that transfers bookmark information between browsers.
- [class BEBrowserDataExtension](./bebrowserdataextension.md)
  A class that transfers browser extension information between browsers.
- [class BEBrowserData](./bebrowserdata.md)
  A representation of browsing data from a source browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatareadinglistitem)*