# openExportBrowsingDataSettings(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Presents the Export Browsing Data sheet from Safari Settings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
class func openExportBrowsingDataSettings() async throws
```

## Mentions

- [Importing data exported from Safari](importing-data-exported-from-safari.md)

#### Discussion

This method presents the same data export sheet accessible in Safari’s settings, which enables someone to export their browsing data to a file. The data includes page visit history, reading list information, bookmarks, passwords, payment cards, and browser extensions.

The method returns an error unless you call it while your app is in the foreground.

For information on the file format and steps to import the data, see [`Importing data exported from Safari`](importing-data-exported-from-safari.md).

## Parameters

- `completionHandler`: A block the system calls after the operation completes, with an optional error parameter. - **error**: `nil` if the export sheet opens successfully; otherwise, an error that indicates the reason for the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings/openexportbrowsingdatasettings(completionhandler:))*