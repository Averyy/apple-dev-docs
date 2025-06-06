# products

**Framework**: StoreKit  
**Kind**: property

A list of products, one product for each valid product identifier provided in the original request.

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
var products: [SKProduct] { get }
```

#### Discussion

The array consists of a list of [`SKProduct`](skproduct.md) objects.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
- [var invalidProductIdentifiers: [String]](skproductsresponse/invalidproductidentifiers.md)
  An array of product identifier strings that the App Store doesn’t recognize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsresponse/products)*