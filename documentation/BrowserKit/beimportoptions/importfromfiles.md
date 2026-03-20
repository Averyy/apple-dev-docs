# importFromFiles

**Framework**: BrowserKit  
**Kind**: property

A Boolean value that indicates whether to import browser data from files.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var importFromFiles: Bool { get }
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Discussion

If the value of this property is `false`, the system retrieves browsing data from the other browser and provides the data to your app by invoking your handler for the [`BEBrowserDataImportManager`](bebrowserdataimportmanager.md) class’s [`userActivityType`](bebrowserdataimportmanager/useractivitytype-35jes.md).

If the value of this property is `true`, the system cancels the browser-to-browser data transfer, and your app imports the browsing data from disk according to your app’s unique workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beimportoptions/importfromfiles)*