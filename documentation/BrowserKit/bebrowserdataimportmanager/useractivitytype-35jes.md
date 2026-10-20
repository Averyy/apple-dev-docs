# userActivityType

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Type Property

A constant that identifies the launch activity for data import requests.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
static var userActivityType: String { get }
```

## Mentions

- [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md)

#### Discussion

The system launches your browser app with this activity when someone initiates a data import request ([`requestImport(for:completionHandler:)`](./requestimport%28for,completionhandler%29.md)) from your browser.

First, the system launches the source browser with the [`BEBrowserDataExportManager`](../bebrowserdataexportmanager.md) class’s [`userActivityType`](../bebrowserdataexportmanager/useractivitytype-4ar5j.md) to retrieve the data, then the system launches your app with this activity to import the retrieved data.

> ❗ **Important**:  The system relaunches the browser that initiates an import using the `BEBrowserDataExchangeImportActivity`, regardless of whether the inititiating browser is currently running.

For more information, see [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md).

## See Also

### Managing import tokens
- [class let importTokenUserInfoKey: String](./importtokenuserinfokey-3bqve.md)
  A key for accessing the data transfer token in the import launch activity’s info dictionary.
- [static var importTokenUserInfoKey: String](./importtokenuserinfokey-3zzub.md)
  A key for accessing the data transfer token in the import launch activity’s info dictionary.
- [class let userActivityType: String](./useractivitytype-8xgjo.md)
  A constant that identifies the launch activity for data import requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager/useractivitytype-35jes)*