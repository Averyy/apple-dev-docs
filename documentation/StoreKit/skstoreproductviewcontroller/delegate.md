# delegate

**Framework**: StoreKit  
**Kind**: property

The store view controller’s delegate.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
@MainActor
weak var delegate: (any SKStoreProductViewControllerDelegate)? { get set }
```

#### Discussion

Your application must set the delegate before presenting the store view controller.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
- [protocol SKStoreProductViewControllerDelegate](skstoreproductviewcontrollerdelegate.md)
  A protocol to call when the customer dismisses the store screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/delegate)*