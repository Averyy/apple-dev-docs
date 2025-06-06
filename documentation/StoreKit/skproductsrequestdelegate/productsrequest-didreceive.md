# productsRequest(_:didReceive:)

**Framework**: StoreKit  
**Kind**: method  
**Required**: Yes

Accepts the App Store response that contains the app-requested product information.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse)
```

## Parameters

- `request`: The product request sent to the Apple App Store.
- `response`: Detailed information about the list of products.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate/productsrequest(_:didreceive:))*