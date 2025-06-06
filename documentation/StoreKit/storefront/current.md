# current

**Framework**: StoreKit  
**Kind**: property

The current App Store storefront for product purchases.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var current: Storefront? { get async }
```

#### Discussion

Use [`current`](storefront/current.md) to determine a customer’s current storefront region and offer in-app products suitable for that region. You maintain your own list of product identifiers and the storefronts in which you make them available.

## See Also

- [struct Storefront](storefront.md)
  The region and unique identifier of the App Store storefront for the device.
- [static var updates: Storefront.Storefronts](storefront/updates.md)
  The asynchronous sequence that emits storefront information when the system updates the storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storefront/current)*