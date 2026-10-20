# products

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A list of products, one product for each valid product identifier provided in the original request.

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
var products: [SKProduct] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SKProduct *> * products;
```

#### Discussion

The array consists of a list of [`SKProduct`](../skproduct.md) objects.

## See Also

### Related Documentation
- [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
### Response Information
- [var invalidProductIdentifiers: [String]](./invalidproductidentifiers.md)
  An array of product identifier strings that the App Store doesn’t recognize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsresponse/products)*