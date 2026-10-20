# productsRequest(_:didReceive:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Accepts the App Store response that contains the app-requested product information.

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
func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse)
```

```objc
- (void) productsRequest:(SKProductsRequest *) request didReceiveResponse:(SKProductsResponse *) response;
```

## Parameters

- `request`: The product request sent to the Apple App Store.
- `response`: Detailed information about the list of products.

## See Also

### Related Documentation
- [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate/productsrequest(_:didreceive:))*