# init(productIdentifiers:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Initializes the request with the set of product identifiers.

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
init(productIdentifiers: Set<String>)
```

```objc
- (instancetype) initWithProductIdentifiers:(NSSet<NSString *> *) productIdentifiers;
```

#### Return Value

The initialized request object.

## Parameters

- `productIdentifiers`: The list of product identifiers for the products you wish to retrieve descriptions of.

## See Also

### Related Documentation
- [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsrequest/init(productidentifiers:))*