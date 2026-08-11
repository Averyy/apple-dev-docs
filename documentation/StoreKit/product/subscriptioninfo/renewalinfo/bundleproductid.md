# bundleProductID

**Framework**: StoreKit  
**Kind**: property

Identifies the bundle product the next renewal is for. If the next renewal is created as part of a subscription bundle, this field will be populated with the product ID of the bundle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
var bundleProductID: String? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/bundleproductid)*