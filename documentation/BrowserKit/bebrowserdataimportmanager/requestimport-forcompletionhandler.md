# requestImport(for:completionHandler:)

**Framework**: BrowserKit  
**Kind**: method

Requests that the system display the sheet to import data from another browser.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
func requestImport(for metadata: BEImportMetadata) async throws -> BEImportOptions
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Discussion

Call this method when someone interacts with your browser app’s UI to import browsing data from another browser app.

This method provides your completion handler an option that indicates whether the person requests loading browsing data from files rather than directly from another browser on the device.

## Parameters

- `metadata`: Metadata that describes the import capabilities, including file import support.
- `completionHandler`: A closure that the system calls and provides the import options, which contain the person’s selections in the sheet.

## See Also

- [func importBrowserData(token: UUID) -> AsyncThrowingStream<BEBrowserData, any Error>](bebrowserdataimportmanager/importbrowserdata(token:).md)
  Imports another app’s browsing data as a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager/requestimport(for:completionhandler:))*