# SKProductsRequestDelegate

**Framework**: StoreKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods the delegate implements so it receives the product information your app requests.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Get products using Product.products(for:).

## Declaration

```swift
protocol SKProductsRequestDelegate : SKRequestDelegate
```

```objc
@protocol SKProductsRequestDelegate <SKRequestDelegate>
```

## Mentions

- [Fetching product information from the App Store](./fetching-product-information-from-the-app-store.md)

#### Overview

The [`SKProductsRequestDelegate`](./skproductsrequestdelegate.md) protocol declares methods that are implemented by the delegate of an [`SKProductsRequest`](./skproductsrequest.md) object. The delegate receives the product information that the product request referred to. Your app uses this information when presenting products to users in its in-app store.

> ⚠️ **Warning**:  Responses received by the `SKProductsRequestDelegate` may not be returned on a specific thread. If you make assumptions about which queue will handle delegate responses, you may encounter unintended performance and compatibility issues in the future.

## Topics

### Receiving the Response
- [func productsRequest(SKProductsRequest, didReceive: SKProductsResponse)](./skproductsrequestdelegate/productsrequest%28_,didreceive%29.md)
  Accepts the App Store response that contains the app-requested product information.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [SKRequestDelegate](./skrequestdelegate.md)

## See Also

### Setting the Delegate
- [var delegate: (any SKProductsRequestDelegate)?](./skproductsrequest/delegate.md)
  The delegate that receives the response of the app’s products request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate)*