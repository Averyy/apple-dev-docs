# delegate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The delegate that receives the response of the app’s products request.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.products(for:).

## Declaration

```swift
weak var delegate: (any SKProductsRequestDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<SKProductsRequestDelegate> delegate;
```

## See Also

### Setting the Delegate
- [protocol SKProductsRequestDelegate](../skproductsrequestdelegate.md)
  A set of methods the delegate implements so it receives the product information your app requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsrequest/delegate)*