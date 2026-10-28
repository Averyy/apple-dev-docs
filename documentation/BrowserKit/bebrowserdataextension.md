# BEBrowserDataExtension

**Framework**: BrowserKit  
**Kind**: class  
**Role**: Class

A class that transfers browser extension information between browsers.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEBrowserDataExtension
```

```objc
@interface BEBrowserDataExtension : BEBrowserData
```

## Overview

This class represents an extension with its identifying metadata, including display name, developer information, and App Store identifier. The identifier allows browsers to help people discover and install equivalent extensions when transferring browsing data.

## Topics

### Creating an extension
- [init(displayName: String, developerName: String, identifier: String, storeIdentifier: String)](./bebrowserdataextension/init%28displayname,developername,identifier,storeidentifier%29.md)
  Initializes an extension with its identifying information and App Store reference.
### Accessing extension metadata
- [var developerName: String](./bebrowserdataextension/developername.md)
  An extension developer’s name.
- [var displayName: String](./bebrowserdataextension/displayname.md)
  An extension’s localized display name.
- [var identifier: String](./bebrowserdataextension/identifier.md)
  A unique identifier for an extension.
- [var storeIdentifier: String](./bebrowserdataextension/storeidentifier.md)
  An identifier that locates the extension in the App Store.

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
- [class BEBrowserDataReadingListItem](./bebrowserdatareadinglistitem.md)
  A class that transfers reading list data between browsers.
- [class BEBrowserData](./bebrowserdata.md)
  A representation of browsing data from a source browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataextension)*