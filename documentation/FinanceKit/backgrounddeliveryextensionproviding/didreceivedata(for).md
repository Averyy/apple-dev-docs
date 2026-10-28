# didReceiveData(for:)

**Framework**: FinanceKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handle changes to data within the finance store.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func didReceiveData(for types: [FinanceStore.BackgroundDataType]) async
```

## Discussion

The entry point of a `BackgroundDeliveryExtension`, called when data changes within the finance store. From here, use the FinanceKit API to query and process those changes.

Before you can receive changes, enable them for your extension using [`enableBackgroundDelivery(for:frequency:)`](../financestore/enablebackgrounddelivery%28for,frequency%29.md).

> **Note**:  Returning from this function closes the extension, ending any ongoing operations.

## Parameters

- `types`: An array of `BackgroundDataType` that indicates which types of data have changed in the Finance Store.

## See Also

### Instance Methods
- [func willTerminate() async](./willterminate%28%29.md)
  Get alerted when a `BackgroundDeliveryExtension` is about to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/backgrounddeliveryextensionproviding/didreceivedata(for:))*