# SFSafariSettings

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

A class that provides your app access to several of Safari’s settings options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 26.0+

## Declaration

```swift
class SFSafariSettings
```

```objc
@interface SFSafariSettings : NSObject
```

## Mentions

- [Importing data exported from Safari](./importing-data-exported-from-safari.md)

## Overview

This class allows your app to present Safari’s extension settings pane or the Export Browsing Data sheet, which enables a person to export their Safari browsing data to a file.

## Topics

### Accessing Safari extensions
- [class func openExtensionsSettings(forIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](./sfsafarisettings/openextensionssettings%28foridentifiers,completionhandler%29.md)
  Presents the extensions pane from Safari Settings.
### Exporting browsing data to a file
- [class func openExportBrowsingDataSettings(completionHandler: (((any Error)?) -> Void)?)](./sfsafarisettings/openexportbrowsingdatasettings%28completionhandler%29.md)
  Presents the Export Browsing Data sheet from Safari Settings.
### Type Methods
- [class func checkAutoFillUserNamesAndPasswordsEnabled(completionHandler: (Bool, (any Error)?) -> Void)](./sfsafarisettings/checkautofillusernamesandpasswordsenabled%28completionhandler%29.md)
  Query the value of the Safari settings toggle for AutoFill > User names and passwords

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Safari content in your app
- [Importing data exported from Safari](./importing-data-exported-from-safari.md)
  Transfer bookmarks, saved passwords, and other information between browsers.
- [class SFSafariViewController](./sfsafariviewcontroller.md)
  An object that provides a visible standard interface for browsing the web.
- [SFAuthenticationSession.CompletionHandler](./sfauthenticationsession/completionhandler.md)
  The completion handler for an authentication session when the user cancels or finishes the login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings)*