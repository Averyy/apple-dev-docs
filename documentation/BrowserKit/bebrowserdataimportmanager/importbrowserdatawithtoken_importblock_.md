# importBrowserDataWithToken:importBlock:

**Framework**: BrowserKit  
**Kind**: method  
**Role**: Instance Method

Imports browser data using the given token and processes it the given block.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```objc
- (void) importBrowserDataWithToken:(NSUUID *) token importBlock:(void (^)(BEBrowserData *, BOOL , NSError *)) importBlock;
```

## Discussion

Call this method from the [`userActivityType`](./useractivitytype-35jes.md) to begin receiving a stream of another app’s browsing data. For more information, see [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md).

## Parameters

- `token`: A UUID that identifies the import operation. Pass that [`importTokenUserInfoKey`](./importtokenuserinfokey-3bqve.md) value that you receive while launching from the [`userActivityType`](./useractivitytype-35jes.md) activity.
- `importBlock`: A closure called for each imported browser data item.

## See Also

### Importing browser data
- [func requestImport(for: BEImportMetadata, completionHandler: (BEImportOptions?, (any Error)?) -> Void)](./requestimport%28for,completionhandler%29.md)
  Requests that the system display the sheet to import data from another browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager/importbrowserdatawithtoken:importblock:)*