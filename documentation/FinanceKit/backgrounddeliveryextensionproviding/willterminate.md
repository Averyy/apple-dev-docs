# willTerminate()

**Framework**: FinanceKit  
**Kind**: method  
**Required**: Yes

Get alerted when a `BackgroundDeliveryExtension` is about to close.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func willTerminate() async
```

#### Discussion

This is called when the extension approaches the end of its time window and is about to be terminated by the system. It provides an opportunity to safely end any ongoing operations and save changes to data. When the time window is exceeded, the extension terminates even if execution is within `willTerminate`.

> ❗ **Important**:  For certain system events, `willTerminate` may not be called before the extension is terminated.

## See Also

- [func didReceiveData(for: [FinanceStore.BackgroundDataType]) async](backgrounddeliveryextensionproviding/didreceivedata(for:).md)
  Handle changes to data within the finance store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/backgrounddeliveryextensionproviding/willterminate())*