# BackgroundDeliveryExtension

**Framework**: FinanceKit  
**Kind**: protocol  
**Role**: Protocol

An extension used to receive updates about changes to data within the finance store.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
protocol BackgroundDeliveryExtension : AppExtension, BackgroundDeliveryExtensionProviding
```

## Overview

Use [`enableBackgroundDelivery(for:frequency:)`](./financestore/enablebackgrounddelivery%28for,frequency%29.md) to enable updates for an extension and see [`BackgroundDeliveryExtensionProviding`](./backgrounddeliveryextensionproviding.md) to implement functions for an extension.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/appextension.md)
- [BackgroundDeliveryExtensionProviding](./backgrounddeliveryextensionproviding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/backgrounddeliveryextension)*