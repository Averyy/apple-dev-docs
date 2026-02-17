# BEBrowserDataExtension

**Framework**: BrowserKit  
**Kind**: class

A class that transfers browser extension information between browsers.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
class BEBrowserDataExtension
```

#### Overview

This class represents an extension with its identifying metadata, including display name, developer information, and App Store identifier. The identifier allows browsers to help people discover and install equivalent extensions when transferring browsing data.

## Topics

### Creating an extension
- [init(displayName: String, developerName: String, identifier: String, storeIdentifier: String)](bebrowserdataextension/init(displayname:developername:identifier:storeidentifier:).md)
  Initializes an extension with its identifying information and App Store reference.
### Accessing extension metadata
- [var developerName: String](bebrowserdataextension/developername.md)
  An extension developer’s name.
- [var displayName: String](bebrowserdataextension/displayname.md)
  An extension’s localized display name.
- [var identifier: String](bebrowserdataextension/identifier.md)
  A unique identifier for an extension.
- [var storeIdentifier: String](bebrowserdataextension/storeidentifier.md)
  An identifier that locates the extension in the App Store.

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
- [class BEBrowserDataReadingListItem](bebrowserdatareadinglistitem.md)
  A class that transfers reading list data between browsers.
- [class BEBrowserData](bebrowserdata.md)
  A representation of browsing data from a source browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataextension)*