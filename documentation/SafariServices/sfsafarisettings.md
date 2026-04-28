# SFSafariSettings

**Framework**: Safari Services  
**Kind**: class

A class that provides your app access to several of Safari’s settings options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
class SFSafariSettings
```

## Mentions

- [Importing data exported from Safari](importing-data-exported-from-safari.md)

#### Overview

This class allows your app to present Safari’s extension settings pane or the Export Browsing Data sheet, which enables a person to export their Safari browsing data to a file.

## Topics

### Accessing Safari extensions
- [class func openExtensionsSettings(forIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](sfsafarisettings/openextensionssettings(foridentifiers:completionhandler:).md)
  Presents the extensions pane from Safari Settings.
### Exporting browsing data to a file
- [class func openExportBrowsingDataSettings(completionHandler: (((any Error)?) -> Void)?)](sfsafarisettings/openexportbrowsingdatasettings(completionhandler:).md)
  Presents the Export Browsing Data sheet from Safari Settings.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Importing data exported from Safari](importing-data-exported-from-safari.md)
  Transfer bookmarks, saved passwords, and other information between browsers.
- [class SFSafariViewController](sfsafariviewcontroller.md)
  An object that provides a visible standard interface for browsing the web.
- [SFAuthenticationSession.CompletionHandler](sfauthenticationsession/completionhandler.md)
  The completion handler for an authentication session when the user cancels or finishes the login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings)*