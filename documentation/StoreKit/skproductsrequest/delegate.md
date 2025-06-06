# delegate

**Framework**: StoreKit  
**Kind**: property

The delegate that receives the response of the app’s products request.

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
weak var delegate: (any SKProductsRequestDelegate)? { get set }
```

## See Also

- [protocol SKProductsRequestDelegate](skproductsrequestdelegate.md)
  A set of methods the delegate implements so it receives the product information your app requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsrequest/delegate)*