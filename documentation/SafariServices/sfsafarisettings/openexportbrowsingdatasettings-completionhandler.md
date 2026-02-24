# openExportBrowsingDataSettings(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Launches Settings and opens Safari’s export browsing data sheet

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func openExportBrowsingDataSettings() async throws
```

#### Discussion

Call this method when your app is in the foreground, otherwise it returns an error.

Launches Settings and opens Safari’s export browsing data sheet.

Call this method when your app is in the foreground, otherwise it returns an error.

## Parameters

- `completionHandler`: The block the system calls after the operation completes, with an optional error parameter if an error occurs. - **error**: An error object indicating the reason for the failure, or `nil` if the system successfully opens the sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings/openexportbrowsingdatasettings(completionhandler:))*