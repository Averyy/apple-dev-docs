# setSimulatedError(_:forAPI:)

**Framework**: StoreKit Test  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func setSimulatedError<API>(_ error: API.Failure?, forAPI api: API) async throws where API : FailableStoreKitAPI
```

## See Also

- [func buyProduct(identifier: Product.ID, options: Set<Product.PurchaseOption>) async throws -> Transaction](sktestsession/buyproduct(identifier:options:).md)
- [func simulatedError<API>(forAPI: API) async -> API.Failure?](sktestsession/simulatederror(forapi:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/setsimulatederror(_:forapi:))*