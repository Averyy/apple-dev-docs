# userActivityType

**Framework**: BrowserKit  
**Kind**: property

A constant that identifies the launch activity for data import requests.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
class let userActivityType: String
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Discussion

The system launches your browser app with this activity when someone initiates a data import request ([`requestImport(for:completionHandler:)`](bebrowserdataimportmanager/requestimport(for:completionhandler:).md)) from your browser.

First, the system launches the source browser with the [`BEBrowserDataExportManager`](bebrowserdataexportmanager.md) class’s [`userActivityType`](bebrowserdataexportmanager/useractivitytype-4ar5j.md) to retrieve the data, then the system launches your app with this activity to import the retrieved data.

> ❗ **Important**:  The system relaunches the browser that initiates an import using the `BEBrowserDataExchangeImportActivity`, regardless of whether the inititiating browser is currently running.

For more information, see [`Transferring browsing data to another browser`](transferring-browsing-data-to-another-browser.md).

## See Also

- [class let importTokenUserInfoKey: String](bebrowserdataimportmanager/importtokenuserinfokey-3bqve.md)
  A key for accessing the data transfer token in the import launch activity’s info dictionary.
- [static var importTokenUserInfoKey: String](bebrowserdataimportmanager/importtokenuserinfokey-3zzub.md)
  A key for accessing the data transfer token in the import launch activity’s info dictionary.
- [static var userActivityType: String](bebrowserdataimportmanager/useractivitytype-35jes.md)
  A constant that identifies the launch activity for data import requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager/useractivitytype-8xgjo)*