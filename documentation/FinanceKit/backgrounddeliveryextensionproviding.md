# BackgroundDeliveryExtensionProviding

**Framework**: FinanceKit  
**Kind**: protocol

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol BackgroundDeliveryExtensionProviding
```

## Topics

### Instance Methods
- [func didReceiveData(for: [FinanceStore.BackgroundDataType]) async](backgrounddeliveryextensionproviding/didreceivedata(for:).md)
  Handle changes to data within the finance store.
- [func willTerminate() async](backgrounddeliveryextensionproviding/willterminate.md)
  Get alerted when a `BackgroundDeliveryExtension` is about to close.

## Relationships

### Inherited By
- [BackgroundDeliveryExtension](backgrounddeliveryextension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/backgrounddeliveryextensionproviding)*