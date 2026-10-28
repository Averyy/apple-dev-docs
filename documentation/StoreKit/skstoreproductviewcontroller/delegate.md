# delegate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The store view controller’s delegate.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
weak var delegate: (any SKStoreProductViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<SKStoreProductViewControllerDelegate> delegate;
```

## Discussion

Your application must set the delegate before presenting the store view controller.

## See Also

### Related Documentation
- [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
### Setting a delegate
- [protocol SKStoreProductViewControllerDelegate](../skstoreproductviewcontrollerdelegate.md)
  A protocol to call when the customer dismisses the store screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/delegate)*