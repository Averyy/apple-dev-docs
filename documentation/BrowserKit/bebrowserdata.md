# BEBrowserData

**Framework**: BrowserKit  
**Kind**: class  
**Role**: Class

A representation of browsing data from a source browser app.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEBrowserData
```

```objc
@interface BEBrowserData : NSObject
```

## Overview

This class describes the source of browsing data that transfers between browsers. It identifies the browser that data originates from by providing its bundle ID and localized display name.

## Topics

### Creating a representation of browser data
- [init?(coder: NSCoder)](./bebrowserdata/init%28coder%29.md)
  Initializes browser data from a decoder.
- [init(sourceApplicationBundleIdentifier: String?, sourceApplicationLocalizedName: String?)](./bebrowserdata/init%28sourceapplicationbundleidentifier,sourceapplicationlocalizedname%29.md)
  Initializes browser data with the source app’s identifier and display name.
### Identifying the source browser app
- [var sourceApplicationBundleIdentifier: String?](./bebrowserdata/sourceapplicationbundleidentifier.md)
  The source browser app’s bundle identifier.
- [var sourceApplicationLocalizedName: String?](./bebrowserdata/sourceapplicationlocalizedname.md)
  The source browser app’s localized name.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [BEBrowserDataBookmark](./bebrowserdatabookmark.md)
- [BEBrowserDataExtension](./bebrowserdataextension.md)
- [BEBrowserDataHistoryVisit](./bebrowserdatahistoryvisit.md)
- [BEBrowserDataReadingListItem](./bebrowserdatareadinglistitem.md)
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
- [class BEBrowserDataExtension](./bebrowserdataextension.md)
  A class that transfers browser extension information between browsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdata)*