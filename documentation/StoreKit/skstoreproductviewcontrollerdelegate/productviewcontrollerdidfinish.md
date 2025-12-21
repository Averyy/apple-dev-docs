# productViewControllerDidFinish(_:)

**Framework**: StoreKit  
**Kind**: method

Called when the user dismisses the store screen.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
optional func productViewControllerDidFinish(_ viewController: SKStoreProductViewController)
```

#### Discussion

Your delegate should call the [`dismissModalViewControllerAnimated:`](https://developer.apple.com/documentation/UIKit/UIViewController/dismissModalViewControllerAnimated:) method on the view controller that originally presented the store screen. If your app paused any other activities before presenting the store, it can restart those services in this method.

## Parameters

- `viewController`: The store view controller whose interface was dismissed by the user.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductviewcontrollerdelegate/productviewcontrollerdidfinish(_:))*