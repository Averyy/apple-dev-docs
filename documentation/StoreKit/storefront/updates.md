# updates

**Framework**: StoreKit  
**Kind**: property

The asynchronous sequence that emits storefront information when the system updates the storefront.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var updates: Storefront.Storefronts { get }
```

#### Discussion

The storefront value can change at any time. Use [`updates`](storefront/updates.md) to listen for changes in this value. Respond to storefront changes by refreshing the list of your available products.

## See Also

- [struct Storefront](storefront.md)
  The region and unique identifier of the App Store storefront for the device.
- [static var current: Storefront?](storefront/current.md)
  The current App Store storefront for product purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storefront/updates)*