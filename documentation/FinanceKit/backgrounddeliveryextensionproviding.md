# BackgroundDeliveryExtensionProviding

**Framework**: FinanceKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
protocol BackgroundDeliveryExtensionProviding
```

## Topics

### Instance Methods
- [func didReceiveData(for: [FinanceStore.BackgroundDataType]) async](./backgrounddeliveryextensionproviding/didreceivedata%28for%29.md)
  Handle changes to data within the finance store.
- [func willTerminate() async](./backgrounddeliveryextensionproviding/willterminate%28%29.md)
  Get alerted when a `BackgroundDeliveryExtension` is about to close.

## Relationships

### Inherited By
- [BackgroundDeliveryExtension](./backgrounddeliveryextension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/backgrounddeliveryextensionproviding)*