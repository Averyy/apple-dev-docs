# exportTokenUserInfoKey

**Framework**: BrowserKit  
**Kind**: property

A key for accessing the data transfer token in the export launch activity’s info dictionary.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
static var exportTokenUserInfoKey: String { get }
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Discussion

Use this key to access the token that validates the transfer of browsing data when the system launches your app to export the data. For more information, see [`Transferring browsing data to another browser`](transferring-browsing-data-to-another-browser.md).

## See Also

- [class let exportTokenUserInfoKey: String](bebrowserdataexportmanager/exporttokenuserinfokey-7e56u.md)
  A key for accessing the data transfer token in the export launch activity’s info dictionary.
- [static var userActivityType: String](bebrowserdataexportmanager/useractivitytype-4ar5j.md)
  A constant that identifies the launch activity for data export requests.
- [class let userActivityType: String](bebrowserdataexportmanager/useractivitytype-g862.md)
  A constant that identifies the launch activity for data export requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager/exporttokenuserinfokey-1y5l1)*