# simulatedError(forAPI:)

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
func simulatedError<API>(forAPI api: API) async -> API.Failure? where API : FailableStoreKitAPI
```

## See Also

- [func buyProduct(identifier: Product.ID, options: Set<Product.PurchaseOption>) async throws -> Transaction](sktestsession/buyproduct(identifier:options:).md)
- [func setSimulatedError<API>(API.Failure?, forAPI: API) async throws](sktestsession/setsimulatederror(_:forapi:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/simulatederror(forapi:))*