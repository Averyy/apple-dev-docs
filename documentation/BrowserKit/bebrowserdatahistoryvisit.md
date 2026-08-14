# BEBrowserDataHistoryVisit

**Framework**: BrowserKit  
**Kind**: class

A class that transfers page visit history between browsers.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEBrowserDataHistoryVisit
```

#### Overview

This class captures comprehensive information about a page visit, including metadata, the URL, redirect information, and success status. The redirect properties enable a browser to preserve full navigation context when transferring history.

## Topics

### Gathering data that creates the history of a visit
- [init(url: URL, dateOfLastVisit: Date, title: String?, loadedSuccessfully: Bool, httpGet: Bool, redirectSourceURL: URL?, redirectSourceDateOfVisit: Date?, redirectDestinationURL: URL?, redirectDestinationDateOfVisit: Date?, visitCount: Int)](bebrowserdatahistoryvisit/init(url:dateoflastvisit:title:loadedsuccessfully:httpget:redirectsourceurl:redirectsourcedateofvisit:redirectdestinationurl:redirectdestinationdateofvisit:visitcount:)-j2oc.md)
  Creates a record of a page visit that includes metadata and redirect information.
### Accessing visit properties
- [var dateOfLastVisit: Date](bebrowserdatahistoryvisit/dateoflastvisit.md)
  The date of the person’s last page visit.
- [var httpGet: Bool](bebrowserdatahistoryvisit/httpget.md)
  A Boolean value that indicates whether the visit is an HTTP GET request.
- [var loadedSuccessfully: Bool](bebrowserdatahistoryvisit/loadedsuccessfully.md)
  A Boolean value that indicates whether the page loads without errors.
- [var title: String?](bebrowserdatahistoryvisit/title.md)
  A localized title for a visited page.
- [var url: URL](bebrowserdatahistoryvisit/url.md)
  A URL for the visited page.
- [var visitCount: Int](bebrowserdatahistoryvisit/visitcount.md)
  A count of how many visits the page received.
### Managing redirect information
- [var redirectDestinationDateOfVisit: Date?](bebrowserdatahistoryvisit/redirectdestinationdateofvisit.md)
  The date of the redirect destination visit.
- [var redirectDestinationURL: URL?](bebrowserdatahistoryvisit/redirectdestinationurl.md)
  A URL to which the visit redirects.
- [var redirectSourceDateOfVisit: Date?](bebrowserdatahistoryvisit/redirectsourcedateofvisit.md)
  The date of the redirect source visit.
- [var redirectSourceURL: URL?](bebrowserdatahistoryvisit/redirectsourceurl.md)
  A URL that redirects to the visited page.
### Initializers
- [init(URL: URL, dateOfLastVisit: Date, title: String?, loadedSuccessfully: Bool, httpGet: Bool, redirectSourceURL: URL?, redirectSourceDateOfVisit: Date?, redirectDestinationURL: URL?, redirectDestinationDateOfVisit: Date?, visitCount: Int)](bebrowserdatahistoryvisit/init(url:dateoflastvisit:title:loadedsuccessfully:httpget:redirectsourceurl:redirectsourcedateofvisit:redirectdestinationurl:redirectdestinationdateofvisit:visitcount:)-hvhk.md)

## Relationships

### Inherits From
- [BEBrowserData](bebrowserdata.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class BEBrowserDataBookmark](bebrowserdatabookmark.md)
  A class that transfers bookmark information between browsers.
- [class BEBrowserDataReadingListItem](bebrowserdatareadinglistitem.md)
  A class that transfers reading list data between browsers.
- [class BEBrowserDataExtension](bebrowserdataextension.md)
  A class that transfers browser extension information between browsers.
- [class BEBrowserData](bebrowserdata.md)
  A representation of browsing data from a source browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatahistoryvisit)*