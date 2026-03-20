# userActivityType

**Framework**: BrowserKit  
**Kind**: property

A constant that identifies the launch activity for data export requests.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
static var userActivityType: String { get }
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Discussion

The system launches your browser app with this activity when someone initiates a data import request ([`requestImport(for:completionHandler:)`](bebrowserdataimportmanager/requestimport(for:completionhandler:).md)) from within another browser, and chooses your app in the sheet as the browser to provide the exported data.

For more information, see [`Transferring browsing data to another browser`](transferring-browsing-data-to-another-browser.md).

## See Also

- [static var exportTokenUserInfoKey: String](bebrowserdataexportmanager/exporttokenuserinfokey-1y5l1.md)
  A key for accessing the data transfer token in the export launch activity’s info dictionary.
- [class let exportTokenUserInfoKey: String](bebrowserdataexportmanager/exporttokenuserinfokey-7e56u.md)
  A key for accessing the data transfer token in the export launch activity’s info dictionary.
- [class let userActivityType: String](bebrowserdataexportmanager/useractivitytype-g862.md)
  A constant that identifies the launch activity for data export requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager/useractivitytype-4ar5j)*