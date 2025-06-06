# SKStoreProductViewControllerDelegate

**Framework**: StoreKit  
**Kind**: protocol

A protocol to call when the customer dismisses the store screen.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
protocol SKStoreProductViewControllerDelegate : NSObjectProtocol
```

#### Overview

Typically, this protocol is implemented by the view controller in your application that originally displayed the store screen.

## Topics

### Responding to a Dismiss Action
- [func productViewControllerDidFinish(SKStoreProductViewController)](skstoreproductviewcontrollerdelegate/productviewcontrollerdidfinish(_:).md)
  Called when the user dismisses the store screen.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any SKStoreProductViewControllerDelegate)?](skstoreproductviewcontroller/delegate.md)
  The store view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductviewcontrollerdelegate)*