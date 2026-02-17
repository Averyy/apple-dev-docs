# BEBrowserDataReadingListItem

**Framework**: BrowserKit  
**Kind**: class

A class that transfers reading list data between browsers.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
class BEBrowserDataReadingListItem
```

#### Overview

This class represents an article or webpage in a reading list, including a URL, a title, and the date the item was last opened.

## Topics

### Creating a reading list item
- [init(title: String, url: URL, dateOfLastVisit: Date?)](bebrowserdatareadinglistitem/init(title:url:dateoflastvisit:).md)
  Initializes a reading list item with the given content and access metadata.
### Accessing item properties
- [var dateOfLastVisit: Date?](bebrowserdatareadinglistitem/dateoflastvisit.md)
  The date of the person’s last visit.
- [var title: String](bebrowserdatareadinglistitem/title.md)
  A localized title for a reading list item.
- [var url: URL](bebrowserdatareadinglistitem/url.md)
  A URL for the reading list item.

## Relationships

### Inherits From
- [BEBrowserData](bebrowserdata.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class BEBrowserDataHistoryVisit](bebrowserdatahistoryvisit.md)
  A class that transfers page visit history between browsers.
- [class BEBrowserDataBookmark](bebrowserdatabookmark.md)
  A class that transfers bookmark information between browsers.
- [class BEBrowserDataExtension](bebrowserdataextension.md)
  A class that transfers browser extension information between browsers.
- [class BEBrowserData](bebrowserdata.md)
  A representation of browsing data from a source browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatareadinglistitem)*