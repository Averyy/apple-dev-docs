# importBrowserData(token:)

**Framework**: BrowserKit  
**Kind**: method

Imports another app’s browsing data as a stream.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
@nonobjc
final func importBrowserData(token: UUID) -> AsyncThrowingStream<BEBrowserData, any Error>
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Return Value

An [`AsyncStream`](https://developer.apple.com/documentation/swift/asyncstream), in which you import the individual data types.

#### Discussion

Call this method from the [`userActivityType`](bebrowserdataimportmanager/useractivitytype-35jes.md) to begin receiving a stream of another app’s browsing data. For more information, see [`Transferring browsing data to another browser`](transferring-browsing-data-to-another-browser.md).

## Parameters

- `token`: A UUID that identifies the import operation. Pass the value from the activity’s info dictionary with the [`importTokenUserInfoKey`](bebrowserdataimportmanager/importtokenuserinfokey-3bqve.md) key.

## See Also

- [func requestImport(for: BEImportMetadata, completionHandler: (BEImportOptions?, (any Error)?) -> Void)](bebrowserdataimportmanager/requestimport(for:completionhandler:).md)
  Requests that the system display the sheet to import data from another browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager/importbrowserdata(token:))*