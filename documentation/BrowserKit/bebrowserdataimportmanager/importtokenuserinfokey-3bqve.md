# importTokenUserInfoKey

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Type Property

A key for accessing the data transfer token in the import launch activity’s info dictionary.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class let importTokenUserInfoKey: String
```

```c
extern NSString * const BEBrowserDataExchangeImportToken;
```

## Mentions

- [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md)

## Discussion

Use this key to access the token that validates the transfer of browsing data when the system launches your app to import the data. For more information, see [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md).

## See Also

### Managing import tokens
- [static var importTokenUserInfoKey: String](./importtokenuserinfokey-3zzub.md)
  A key for accessing the data transfer token in the import launch activity’s info dictionary.
- [static var userActivityType: String](./useractivitytype-35jes.md)
  A constant that identifies the launch activity for data import requests.
- [class let userActivityType: String](./useractivitytype-8xgjo.md)
  A constant that identifies the launch activity for data import requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager/importtokenuserinfokey-3bqve)*