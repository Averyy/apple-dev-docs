# openExportBrowsingDataSettings(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Launches Settings and opens Safari’s export browsing data sheet.

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

## Parameters

- `completionHandler`: The block the system calls after the operation completes, with an optional error parameter if an error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings/openexportbrowsingdatasettings(completionhandler:))*